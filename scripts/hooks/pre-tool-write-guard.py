#!/usr/bin/env python3
"""preToolUse hook — blocks writes to sensitive, out-of-repo or out-of-phase paths.

Stdlib only, on purpose: this script runs as an external process under its own
interpreter and must never import project code, so it works identically for
any stack (Python, Swift, Kotlin, Node, ...) being edited in the repo.

Receives the hook payload via stdin as JSON. Two payload shapes are supported:
  Copilot:     {"toolName": "create"|"edit", "toolArgs": {"path": "..."}, ...}
  Claude Code: {"tool_name": "Write"|"Edit", "tool_input": {"file_path": "..."}, ...}

Writes a decision JSON to stdout.

Config: reads "harness.config.json" at the repo root (see
install-dev-harness/templates/harness.config.json.template for the schema).
A missing or corrupt config never blocks — it just disables the checks that
depend on it (phase gating). Path-traversal and blocked-filename checks use
built-in safe defaults even without a config file.
"""

import json
import os
import sys
from pathlib import Path

DEFAULT_PHASE_STATE_PATH = ".harness/change-phase.json"
DEFAULT_BLOCKED_FILENAMES = {".env", "service_account.json", "id_rsa", "id_ed25519"}
DEFAULT_BLOCKED_SUFFIXES = (".pem", ".p12", ".keystore", ".jks")


def _project_root() -> Path:
    """Repo root, independent of the session's cwd.

    A session's cwd can be any subdirectory; resolving config/phase state
    relative to it would make the guardrail read the wrong file — or none.
    """
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


def _decide(decision: str, reason: str = "") -> None:
    payload = {"permissionDecision": decision}
    if reason:
        payload["permissionDecisionReason"] = reason
    print(json.dumps(payload))
    sys.exit(0)


def _read_phase(root: Path, phase_state_path: str) -> "tuple[str, str] | None":
    """Reads (phase, change_name) from shared state; absence never blocks."""
    try:
        with open(root / phase_state_path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None
    phase = data.get("phase")
    if not isinstance(phase, str):
        return None
    change = data.get("change_name")
    return phase, change if isinstance(change, str) else ""


def _extract_path(payload: dict) -> str:
    for container_key in ("toolArgs", "tool_input"):
        container = payload.get(container_key)
        if not isinstance(container, dict):
            continue
        for path_key in ("path", "file_path", "notebook_path"):
            value = container.get(path_key)
            if isinstance(value, str) and value:
                return value
    return ""


payload = json.load(sys.stdin)
raw_path = _extract_path(payload)

if not raw_path:
    _decide("allow")

repo_root = _project_root()
config = _load_config(repo_root)

file_path = Path(raw_path)
filename = file_path.name

blocked_filenames = set(config.get("blocked_filenames", DEFAULT_BLOCKED_FILENAMES))
blocked_suffixes = tuple(config.get("blocked_filename_suffixes", DEFAULT_BLOCKED_SUFFIXES))

if filename in blocked_filenames or filename.endswith(blocked_suffixes):
    _decide(
        "deny",
        f"Escrita em '{filename}' é bloqueada — "
        "credenciais não devem ser armazenadas no repositório.",
    )

try:
    resolved = (repo_root / file_path).resolve()
except OSError:
    resolved = None  # If we can't resolve, let the project's own tooling handle it.

if resolved is not None and not str(resolved).startswith(str(repo_root)):
    _decide(
        "deny",
        f"O caminho '{raw_path}' escapa da raiz do repositório — "
        "path traversal bloqueado pelo harness de segurança.",
    )

# Phase gating: during 'proposal', only planning-artifact prefixes may be written.
planning_prefixes = tuple(config.get("planning_write_prefixes", []))
code_prefixes = tuple(config.get("code_prefixes", []))
phase_state_path = config.get("phase_state_path", DEFAULT_PHASE_STATE_PATH)

if planning_prefixes:
    state = _read_phase(repo_root, phase_state_path)
    if state is not None and state[0] == "proposal":
        phase, change_name = state
        if resolved is not None:
            relative = resolved.relative_to(repo_root).as_posix()
        else:
            relative = file_path.as_posix()

        if not relative.startswith(planning_prefixes):
            scope = "código" if relative.startswith(code_prefixes) else "fora do escopo de planejamento"
            allowed = ", ".join(planning_prefixes)
            _decide(
                "deny",
                f"Escrita em '{relative}' bloqueada: a change '{change_name}' está na fase "
                f"'proposal' e o caminho é {scope}. Na proposta só é permitido escrever "
                f"artefatos de planejamento ({allowed}). Conclua o handoff e promova a "
                "change para 'apply' antes de alterar código.",
            )

_decide("allow")
