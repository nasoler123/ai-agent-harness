# Code tour

[Project](../README.md) · [Architecture](architecture.md) · [Design decisions](decisions.md)

## Start with executable code

1. Read [prompt_cache.py](../source/prompt_cache.py).
2. Inspect the synthetic inputs and assertions in [demo.py](../demo.py).
3. Compare [verification.json](../verification.json) with a fresh local run.

## Selected source from the wider system

| Component | Inspect | Form |
|---|---|---|
| Agent and session assembly | [Open excerpt](../evidence/E12.md) | Código |
| Co-loading cycle detection | [Open excerpt](../evidence/E13.md) | Código |
| Active tool surface | [Open excerpt](../evidence/E14.md) | Código |
| Tool dispatch guards | [Open excerpt](../evidence/E15.md) | Código |
| Context budget cascade | [Open excerpt](../evidence/E16.md) | Código |
| Prompt cache options | [Open excerpt](../evidence/E17.md) | Código |
| Durable event sequence | [Open excerpt](../evidence/E18.md) | Código |
| Sandbox feature and cost gate | [Open excerpt](../evidence/E39.md) | Código |

These excerpts retain original commit references. Incomplete classes, functions or integrations are presented as excerpts; the bounded executable module is separate. Redactions protect identifiers and are recorded in [provenance.json](../provenance.json).
