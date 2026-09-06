#!/usr/bin/env python3
"""Minimal, dependency-free CLI to declare/read the current change phase.

The phase state file is the single source of truth shared with the
PreToolUse hooks in scripts/hooks/ — they read it independently (stdlib
only, no import of this module) so the *path* is the only contract. See
harness.config.json → "phase_state_path".

Usage:
    python3 scripts/harness/phase_cli.py set <phase> [change_name]
    python3 scripts/harness/phase_cli.py show

Typical phases: "proposal" (planning only, code writes gated) and "apply"
(implementation, gate lifted). Any other string is accepted — the hooks only
special-case the literal value "proposal".
"""

import json
import os
import sys
import tempfile
from pathlib import Path

DEFAULT_PHASE_STATE_PATH = ".harness/change-phase.json"


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


def _state_path(root: Path, config: dict) -> Path:
    relative = config.get("phase_state_path", DEFAULT_PHASE_STATE_PATH)
    resolved = (root / relative).resolve()
    if not str(resolved).startswith(str(root)):
        raise SystemExit(f"phase_state_path '{relative}' escapa da raiz do repositório — recuse.")
    return resolved


def _write_atomic(destination: Path, payload: dict) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, ensure_ascii=True, indent=2) + "\n"
    fd, tmp_name = tempfile.mkstemp(dir=destination.parent, prefix=".phase-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.replace(tmp_name, destination)
    except BaseException:
        Path(tmp_name).unlink(missing_ok=True)
        raise


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2

    root = _project_root()
    config = _load_config(root)
    state_path = _state_path(root, config)

    command = argv[1]

    if command == "show":
        if not state_path.exists():
            print("Fase: não declarada")
            return 0
        data = json.loads(state_path.read_text(encoding="utf-8"))
        print(f"Fase: {data.get('phase', '?')} (change: {data.get('change_name', '')})")
        return 0

    if command == "set":
        if len(argv) < 3:
            print("Uso: phase_cli.py set <phase> [change_name]")
            return 2
        phase = argv[2]
        change_name = argv[3] if len(argv) > 3 else ""
        _write_atomic(state_path, {"phase": phase, "change_name": change_name})
        print(f"Fase definida: {phase} (change: {change_name})")
        return 0

    print(f"Comando desconhecido: {command}")
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
