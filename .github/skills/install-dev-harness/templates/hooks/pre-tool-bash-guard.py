#!/usr/bin/env python3
"""preToolUse hook — blocks destructive and out-of-phase bash commands.

Stdlib only, on purpose — see pre-tool-write-guard.py for why.

Receives the hook payload via stdin as JSON. Two payload shapes are supported:
  Copilot:     {"toolName": "bash", "toolArgs": {"command": "..."}, ...}
  Claude Code: {"tool_name": "Bash", "tool_input": {"command": "..."}, ...}

Writes a decision JSON to stdout:
  {"permissionDecision": "deny", "permissionDecisionReason": "..."}
  {"permissionDecision": "allow"}

Config: reads "harness.config.json" at the repo root for the pattern lists
(see harness.config.json.template). Falls back to a safe built-in default
list of destructive commands even without a config file.
"""

import json
import os
import re
import sys
from pathlib import Path

DEFAULT_PHASE_STATE_PATH = ".harness/change-phase.json"

DEFAULT_BLOCKED = [
    {"pattern": r"\bgit\s+push\b", "reason": "git push requer confirmação explícita do usuário."},
    {"pattern": r"\bgit\s+reset\s+--hard\b", "reason": "git reset --hard é destrutivo — peça confirmação explícita."},
    {"pattern": r"\bgit\s+clean\s+-[a-z]*f", "reason": "git clean -f é destrutivo — peça confirmação explícita."},
    {"pattern": r"\brm\s+-[a-z]*r[a-z]*f\b", "reason": "rm -rf é destrutivo — use deleções explícitas ou git rm."},
    {"pattern": r"(>+|tee)\s+\.env\b", "reason": "escrita em .env é bloqueada — credenciais não devem ser commitadas."},
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


def _read_phase(root: Path, phase_state_path: str) -> "str | None":
    try:
        with open(root / phase_state_path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None
    phase = data.get("phase")
    return phase if isinstance(phase, str) else None


def _extract_command(payload: dict) -> str:
    for container_key in ("toolArgs", "tool_input"):
        container = payload.get(container_key)
        if isinstance(container, dict):
            value = container.get("command")
            if isinstance(value, str) and value:
                return value
    return ""


def _deny(reason: str) -> None:
    print(json.dumps({"permissionDecision": "deny", "permissionDecisionReason": reason}))
    sys.exit(0)


payload = json.load(sys.stdin)
command = _extract_command(payload)

repo_root = _project_root()
config = _load_config(repo_root)

for entry in config.get("blocked_bash_patterns", DEFAULT_BLOCKED):
    if re.search(entry["pattern"], command, re.IGNORECASE):
        _deny(entry.get("reason", f"Comando bloqueado pelo harness: {entry['pattern']}"))

phase_state_path = config.get("phase_state_path", DEFAULT_PHASE_STATE_PATH)
proposal_blocked = config.get("proposal_blocked_bash_patterns", [])

if proposal_blocked and _read_phase(repo_root, phase_state_path) == "proposal":
    for entry in proposal_blocked:
        if re.search(entry["pattern"], command, re.IGNORECASE):
            label = entry.get("label", entry["pattern"])
            _deny(
                f"{label} é bloqueado na fase 'proposal' — a proposta não muta o "
                "repositório. Conclua o handoff e promova a change para 'apply'."
            )

print(json.dumps({"permissionDecision": "allow"}))
