from pathlib import Path
import importlib.util
import json
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
def offline(event, args):
    if event.startswith("socket.") or event in {"subprocess.Popen", "os.system", "os.exec", "os.posix_spawn"}:
        raise RuntimeError("Demo offline: conexión o proceso externo rechazado")
sys.addaudithook(offline)
spec = importlib.util.spec_from_file_location("original_sample", HERE / "source" / "prompt_cache.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
checks = []
def check(name, condition):
    assert condition, name
    checks.append({"case": name, "passed": True})
template = HERE / "fixtures" / "prompt.txt"
other = HERE / "fixtures" / "prompt-other.txt"
def key(skills=("read", "model"), channel="demo", path=template):
    return module._prompt_cache_key(model="demo-model", channel=channel, agent_id="demo-agent", prompt_template_path=path, allowed_skill_ids=skills)
base = key()
check("Prefijo estable conserva clave", key() == base)
check("Orden del catálogo no cambia clave", key(("model", "read")) == base)
check("Cambiar capacidades cambia clave", key(("read",)) != base)
check("Cambiar canal cambia clave", key(channel="other") != base)
check("Cambiar plantilla cambia clave", key(path=other) != base)
print(json.dumps({"checks": checks, "passed": len(checks), "network": "forbidden"}, ensure_ascii=False))
