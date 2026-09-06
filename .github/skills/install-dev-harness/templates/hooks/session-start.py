#!/usr/bin/env python3
"""sessionStart hook — injects harness context into every new session.

Stdlib only — see pre-tool-write-guard.py for why.

Receives the session payload via stdin as JSON:
  {"sessionId": "...", "cwd": "...", "source": "startup"|"resume"|"new", ...}

Writes {"additionalContext": "..."} to stdout to prepend context to the session.
"""

import json
import os
import subprocess
import sys
from pathlib import Path

DEFAULT_PHASE_STATE_PATH = ".harness/change-phase.json"
DEFAULT_GUIDE_FILES = [
    {"path": "AGENTS.md", "label": "AGENTS.md"},
    {"path": ".pre-commit-config.yaml", "label": "pre-commit"},
]


def _project_root() -> Path:
    explicit = os.environ.get("CLAUDE_PROJECT_DIR")
    if explicit:
        return Path(explicit).resolve()
    current = Path.cwd().resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    return current


def _load_config(root: Path) -> dict:
    config_path = Path(os.environ.get("HARNESS_CONFIG_PATH", root / "harness.config.json"))
    try:
        with open(config_path, encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {}


def _phase_line(root: Path, phase_state_path: str) -> str:
    try:
        with open(root / phase_state_path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return "Fase da change: não declarada — use 'scripts/harness/phase_cli.py set' antes de implementar"
    phase = data.get("phase")
    change = data.get("change_name", "")
    if not isinstance(phase, str):
        return "Fase da change: estado inválido — use 'scripts/harness/phase_cli.py set' antes de implementar"
    return f"Fase da change: {phase} ({change})"


def _git_branch() -> str:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            timeout=3,
        )
        return result.stdout.strip() if result.returncode == 0 else "unknown"
    except OSError:
        return "unknown"


payload = json.load(sys.stdin)
source = payload.get("source", "new")

if source == "resume":
    print(json.dumps({}))
    sys.exit(0)

repo_root = _project_root()
config = _load_config(repo_root)
phase_state_path = config.get("phase_state_path", DEFAULT_PHASE_STATE_PATH)
guide_files = config.get("guide_files", DEFAULT_GUIDE_FILES)

branch = _git_branch()
harness_check = []
for entry in guide_files:
    status = "✓" if (repo_root / entry["path"]).exists() else "✗ MISSING"
    harness_check.append(f"  {status}  {entry.get('label', entry['path'])}")

context = f"""
=== Harness de Segurança ===

Branch atual: {branch}
{_phase_line(repo_root, phase_state_path)}

Guias verificados:
{chr(10).join(harness_check)}

Regras críticas (não negociáveis):
• Fase 'proposal' → escrita em código BLOQUEADA por hook (só artefatos de planejamento)
• git push → BLOQUEADO por hook — peça confirmação explícita ao usuário primeiro
• git reset --hard / rm -rf → BLOQUEADOS — peça confirmação explícita
• Credenciais → nunca como literal de string; use variáveis de ambiente

Consulte o arquivo raiz do agente para todas as regras antes de implementar código.
""".strip()

print(json.dumps({"additionalContext": context}))
