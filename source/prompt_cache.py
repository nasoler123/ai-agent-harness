"""Provider-side prompt-cache options for ``modeler_unified``.

This module does not cache conversations or prompt text in Chals. It only
attaches OpenAI request options that improve routing to OpenAI's automatic
prompt-prefix cache.
"""

from __future__ import annotations

import hashlib
import logging
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Iterable

logger = logging.getLogger(__name__)

_KEY_VERSION = "v1"
_FALSEY = {"", "0", "false", "no", "off", "disabled", "none"}
_TRUTHY = {"1", "true", "yes", "on", "enabled"}
_SUPPORTED_RETENTIONS = {"24h", "in_memory"}
_DATE_SUFFIX_RE = re.compile(r"-20\d{2}-\d{2}-\d{2}$")
_SAFE_KEY_PART_RE = re.compile(r"[^a-z0-9._:-]+")


def build_modeler_prompt_cache_body(
    *,
    model: str,
    channel: str,
    agent_id: str,
    prompt_template_path: Path,
    allowed_skill_ids: Iterable[str] | None,
) -> dict[str, str]:
    """Return ``extra_body`` fields for OpenAI prompt caching.

    The cache key deliberately omits account/user/conversation/sheet identifiers.
    Prompt caching is already exact-prefix checked by OpenAI and scoped to the
    organization; adding per-user identifiers would defeat reuse of the large,
    stable modeler root prompt and skill catalog.
    """

    if not _env_flag("MODELER_PROMPT_CACHE_ENABLED", default=True):
        return {}
    if not _model_supports_prompt_cache(model):
        return {}

    body: dict[str, str] = {}
    if _env_flag("MODELER_PROMPT_CACHE_KEY_ENABLED", default=True):
        body["prompt_cache_key"] = _prompt_cache_key(
            model=model,
            channel=channel,
            agent_id=agent_id,
            prompt_template_path=prompt_template_path,
            allowed_skill_ids=allowed_skill_ids,
        )

    retention = _prompt_cache_retention(model)
    if retention:
        body["prompt_cache_retention"] = retention
    return body


def _env_flag(name: str, *, default: bool) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    value = raw.strip().lower()
    if value in _FALSEY:
        return False
    if value in _TRUTHY:
        return True
    logger.warning(
        "modeler.prompt_cache.invalid_boolean_env name=%s value=%r default=%s",
        name,
        raw,
        default,
    )
    return default


def _prompt_cache_key(
    *,
    model: str,
    channel: str,
    agent_id: str,
    prompt_template_path: Path,
    allowed_skill_ids: Iterable[str] | None,
) -> str:
    skill_profile = (
        "*"
        if allowed_skill_ids is None
        else ",".join(sorted(str(skill_id) for skill_id in allowed_skill_ids))
    )
    digest = _digest_parts(
        "modeler_unified",
        _KEY_VERSION,
        _model_key_label(model),
        _safe_key_part(channel),
        _safe_key_part(agent_id),
        _file_digest(prompt_template_path),
        skill_profile,
    )
    return ":".join(
        [
            "mu",
            _safe_key_part(channel),
            _KEY_VERSION,
            _model_key_label(model),
            digest,
        ]
    )


def _prompt_cache_retention(model: str) -> str | None:
    raw = os.getenv("MODELER_PROMPT_CACHE_RETENTION", "24h")
    value = raw.strip().lower()
    if value in _FALSEY:
        return None
    if value not in _SUPPORTED_RETENTIONS:
        logger.warning(
            "modeler.prompt_cache.invalid_retention value=%r supported=%s",
            raw,
            sorted(_SUPPORTED_RETENTIONS),
        )
        return None
    if value == "24h" and not _model_supports_extended_retention(model):
        logger.info(
            "modeler.prompt_cache.retention_skipped model=%s retention=%s",
            model,
            value,
        )
        return None
    if value == "in_memory" and _model_requires_24h_retention(model):
        logger.info(
            "modeler.prompt_cache.retention_skipped model=%s retention=%s",
            model,
            value,
        )
        return None
    return value


def _model_supports_prompt_cache(model: str) -> bool:
    normalized = _normalize_model(model)
    return normalized.startswith(("gpt-", "o1", "o3", "o4"))


def _model_supports_extended_retention(model: str) -> bool:
    normalized = _normalize_model(model)
    return (
        _matches_versioned_model(normalized, "gpt-5.5")
        or _matches_versioned_model(normalized, "gpt-5.5-pro")
        or _matches_versioned_model(normalized, "gpt-5.4")
        or _matches_versioned_model(normalized, "gpt-5.2")
        or _matches_versioned_model(normalized, "gpt-5.1")
        or normalized.startswith("gpt-5.1-codex")
        or normalized == "gpt-5.1-chat-latest"
        or _matches_versioned_model(normalized, "gpt-5")
        or normalized == "gpt-5-codex"
        or _matches_versioned_model(normalized, "gpt-4.1")
    )


def _model_requires_24h_retention(model: str) -> bool:
    normalized = _normalize_model(model)
    return _matches_versioned_model(normalized, "gpt-5.5") or _matches_versioned_model(
        normalized,
        "gpt-5.5-pro",
    )


def _matches_versioned_model(model: str, family: str) -> bool:
    if model == family:
        return True
    if not model.startswith(family + "-"):
        return False
    suffix = model[len(family) + 1 :]
    # Date-stamped aliases such as ``gpt-5.4-2026-03-05`` are the same
    # family. Other suffixes (for example ``mini``/``nano``) are treated as
    # distinct models unless explicitly listed above.
    return bool(re.fullmatch(r"20\d{2}-\d{2}-\d{2}", suffix))


def _model_key_label(model: str) -> str:
    normalized = _normalize_model(model)
    normalized = _DATE_SUFFIX_RE.sub("", normalized)
    return _safe_key_part(normalized)[:28] or "unknown"


def _normalize_model(model: str) -> str:
    return str(model or "").strip().lower()


def _safe_key_part(value: str) -> str:
    cleaned = _SAFE_KEY_PART_RE.sub("-", str(value or "").strip().lower())
    return cleaned.strip("-") or "unknown"


def _digest_parts(*parts: str) -> str:
    digest = hashlib.sha256()
    for part in parts:
        encoded = str(part).encode("utf-8", errors="replace")
        digest.update(len(encoded).to_bytes(4, "big"))
        digest.update(encoded)
    return digest.hexdigest()[:12]


@lru_cache(maxsize=16)
def _file_digest(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()[:12]
