"""Architecture Fitness Functions for COBOL source code.

Verifies mechanical architectural and structural rules documented in AGENTS.md:
1. Line length limit (columns 1-72 max).
2. Four standard divisions in canonical order.
3. Division headers in Area A (columns 8-11).
4. Working-Storage variables prefixed with 'WS-'.
5. Procedure division ends/contains STOP RUN.
6. Comments have indicator '*' in column 7.

Includes negative test fixtures to guarantee the detectors catch violations.
"""

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SRC_DIR = REPO_ROOT / "src"

CANONICAL_DIVISIONS = [
    "IDENTIFICATION DIVISION",
    "ENVIRONMENT DIVISION",
    "DATA DIVISION",
    "PROCEDURE DIVISION",
]

# Allowlist for files or directories with exceptions (if any)
ALLOWLIST_PATHS: set[Path] = set()


def scan_line_length(filepath: Path) -> list[str]:
    """Flag any line extending past column 72."""
    violations = []
    lines = filepath.read_text(encoding="utf-8", errors="replace").splitlines()
    for lineno, line in enumerate(lines, 1):
        if len(line) > 72:
            violations.append(
                f"{filepath}:{lineno}: linha com {len(line)} colunas (limite: 72 colunas). "
                f"Quebre o texto ou use continuação na Área B (colunas 12-72). "
                f"Trecho: '{line[:72]}>>>[EXCESSO: {line[72:]}]'"
            )
    return violations


def scan_four_divisions(filepath: Path) -> list[str]:
    """Check that the four divisions exist in canonical order."""
    violations = []
    content = filepath.read_text(encoding="utf-8", errors="replace")
    found_divisions: list[tuple[str, int]] = []

    for expected in CANONICAL_DIVISIONS:
        # Match division at beginning of statement (ignoring comments)
        pattern = re.compile(rf"^\s{{7,10}}{expected}\.", re.MULTILINE | re.IGNORECASE)
        match = pattern.search(content)
        if not match:
            violations.append(
                f"{filepath}: Divisão obrigatória '{expected}.' ausente. "
                "Todo programa COBOL deve conter as 4 divisões conforme AGENTS.md."
            )
        else:
            found_divisions.append((expected, match.start()))

    # Check order
    for i in range(len(found_divisions) - 1):
        curr_name, curr_pos = found_divisions[i]
        next_name, next_pos = found_divisions[i + 1]
        if curr_pos >= next_pos:
            violations.append(
                f"{filepath}: Ordem incorreta das divisões: '{curr_name}' aparece após '{next_name}'. "
                f"Ordem canônica: {', '.join(CANONICAL_DIVISIONS)}."
            )

    return violations


def scan_area_a_for_divisions(filepath: Path) -> list[str]:
    """Division headers must start in Area A (columns 8-11, index 7-10 in 0-based)."""
    violations = []
    lines = filepath.read_text(encoding="utf-8", errors="replace").splitlines()
    for lineno, line in enumerate(lines, 1):
        for div in CANONICAL_DIVISIONS:
            idx = line.upper().find(f"{div}.")
            if idx != -1:
                # 0-based index: Column 8 is index 7. Area A is index 7 to 10 (col 8 to 11).
                col_number = idx + 1
                if not (8 <= col_number <= 11):
                    violations.append(
                        f"{filepath}:{lineno}: '{div}.' inicia na coluna {col_number}. "
                        "Divisões devem iniciar na Área A (colunas 8 a 11, padrão coluna 8 com 7 espaços)."
                    )
    return violations


def scan_working_storage_variables(filepath: Path) -> list[str]:
    """Working-Storage variables (01, 77) must have prefix WS-."""
    violations = []
    lines = filepath.read_text(encoding="utf-8", errors="replace").splitlines()
    in_ws = False

    var_pattern = re.compile(r"^\s{7,11}(01|77)\s+([A-Z0-9\-]+)", re.IGNORECASE)

    for lineno, line in enumerate(lines, 1):
        line_clean = line.rstrip()
        # Check if in comment
        if len(line_clean) >= 7 and line_clean[6] in ("*", "/"):
            continue

        if "WORKING-STORAGE SECTION" in line.upper():
            in_ws = True
            continue

        # Exit WS if another section or division starts
        if in_ws and (
            "PROCEDURE DIVISION" in line.upper()
            or "LINKAGE SECTION" in line.upper()
            or "SCREEN SECTION" in line.upper()
            or "LOCAL-STORAGE SECTION" in line.upper()
        ):
            in_ws = False
            continue

        if in_ws:
            match = var_pattern.match(line)
            if match:
                level, var_name = match.group(1), match.group(2).upper()
                if not var_name.startswith("WS-"):
                    violations.append(
                        f"{filepath}:{lineno}: variável '{var_name}' (nível {level}) sem prefixo 'WS-'. "
                        "Variáveis de Working-Storage devem iniciar com 'WS-' conforme AGENTS.md."
                    )
    return violations


def scan_stop_run(filepath: Path) -> list[str]:
    """Program must include STOP RUN in Procedure Division."""
    violations = []
    content = filepath.read_text(encoding="utf-8", errors="replace")
    if "STOP RUN" not in content.upper():
        violations.append(
            f"{filepath}: Sentença 'STOP RUN.' não encontrada. "
            "Programas COBOL devem conter encerramento explícito com STOP RUN conforme AGENTS.md."
        )
    return violations


def scan_comments_indicator(filepath: Path) -> list[str]:
    """Comments starting with asterisk must have '*' in column 7."""
    violations = []
    lines = filepath.read_text(encoding="utf-8", errors="replace").splitlines()
    for lineno, line in enumerate(lines, 1):
        stripped = line.lstrip()
        if stripped.startswith("*"):
            # Check column 7 (index 6)
            if len(line) < 7 or line[6] != "*":
                violations.append(
                    f"{filepath}:{lineno}: Comentário com '*' fora da coluna 7 (está no índice {len(line) - len(stripped)}). "
                    "Em formato fixo COBOL, o indicador de comentário '*' deve estar exatamente na coluna 7."
                )
    return violations


class TestCobolArchitectureFitness(unittest.TestCase):
    """Fitness functions validating the production COBOL source code."""

    def setUp(self) -> None:
        self.cobol_files = [
            f for f in SRC_DIR.rglob("*.cbl") if f not in ALLOWLIST_PATHS
        ] + [
            f for f in SRC_DIR.rglob("*.cob") if f not in ALLOWLIST_PATHS
        ]
        self.assertTrue(self.cobol_files, f"Nenhum arquivo COBOL encontrado em {SRC_DIR}")

    def test_fitness_rule1_line_length_max_72(self) -> None:
        """Regra 1: Linhas não devem exceder 72 colunas."""
        all_violations = []
        for file in self.cobol_files:
            all_violations.extend(scan_line_length(file))
        self.assertFalse(
            all_violations,
            "Violação da Regra de Colunas (máx 72 colunas):\n" + "\n".join(all_violations),
        )

    def test_fitness_rule2_four_divisions_present(self) -> None:
        """Regra 2: Quatro divisões obrigatórias na ordem correta."""
        all_violations = []
        for file in self.cobol_files:
            all_violations.extend(scan_four_divisions(file))
        self.assertFalse(
            all_violations,
            "Violação da Regra das 4 Divisões:\n" + "\n".join(all_violations),
        )

    def test_fitness_rule3_divisions_in_area_a(self) -> None:
        """Regra 3: Nomes de divisões devem iniciar na Área A (colunas 8-11)."""
        all_violations = []
        for file in self.cobol_files:
            all_violations.extend(scan_area_a_for_divisions(file))
        self.assertFalse(
            all_violations,
            "Violação da Regra de Área A para Divisões:\n" + "\n".join(all_violations),
        )

    def test_fitness_rule4_working_storage_naming(self) -> None:
        """Regra 4: Variáveis de Working-Storage devem ter prefixo WS-."""
        all_violations = []
        for file in self.cobol_files:
            all_violations.extend(scan_working_storage_variables(file))
        self.assertFalse(
            all_violations,
            "Violação da Regra de Nomenclatura (prefixo WS-):\n" + "\n".join(all_violations),
        )

    def test_fitness_rule5_stop_run_present(self) -> None:
        """Regra 5: Deve haver STOP RUN na Procedure Division."""
        all_violations = []
        for file in self.cobol_files:
            all_violations.extend(scan_stop_run(file))
        self.assertFalse(
            all_violations,
            "Violação da Regra de Encerramento (STOP RUN):\n" + "\n".join(all_violations),
        )

    def test_fitness_rule6_comment_indicator_col7(self) -> None:
        """Regra 6: Indicador de comentário '*' na coluna 7."""
        all_violations = []
        for file in self.cobol_files:
            all_violations.extend(scan_comments_indicator(file))
        self.assertFalse(
            all_violations,
            "Violação da Regra de Indicador de Comentário (coluna 7):\n" + "\n".join(all_violations),
        )


class TestFitnessDetectorsNegative(unittest.TestCase):
    """Negative test fixtures to prove each detector catches violations."""

    def test_negative_detector_line_length(self) -> None:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".cbl", delete=False, encoding="utf-8") as tmp:
            tmp.write("       IDENTIFICATION DIVISION.\n")
            tmp.write("       * " + ("A" * 70) + "\n")  # Exceeds 72
            path = Path(tmp.name)
        try:
            violations = scan_line_length(path)
            self.assertTrue(violations, "Detector de linha longa falhou em detectar linha > 72")
            self.assertIn("limite: 72 colunas", violations[0])
        finally:
            path.unlink(missing_ok=True)

    def test_negative_detector_missing_division(self) -> None:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".cbl", delete=False, encoding="utf-8") as tmp:
            tmp.write("       IDENTIFICATION DIVISION.\n")
            tmp.write("       DATA DIVISION.\n")
            tmp.write("       PROCEDURE DIVISION.\n")
            path = Path(tmp.name)
        try:
            violations = scan_four_divisions(path)
            self.assertTrue(violations, "Detector falhou em detectar falta de ENVIRONMENT DIVISION")
            self.assertIn("ENVIRONMENT DIVISION", violations[0])
        finally:
            path.unlink(missing_ok=True)

    def test_negative_detector_divisions_order(self) -> None:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".cbl", delete=False, encoding="utf-8") as tmp:
            tmp.write("       ENVIRONMENT DIVISION.\n")
            tmp.write("       IDENTIFICATION DIVISION.\n")
            tmp.write("       DATA DIVISION.\n")
            tmp.write("       PROCEDURE DIVISION.\n")
            path = Path(tmp.name)
        try:
            violations = scan_four_divisions(path)
            self.assertTrue(violations, "Detector falhou em detectar ordem invertida")
            self.assertIn("Ordem incorreta", violations[0])
        finally:
            path.unlink(missing_ok=True)

    def test_negative_detector_division_area_b(self) -> None:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".cbl", delete=False, encoding="utf-8") as tmp:
            # 11 spaces -> column 12 (Area B)
            tmp.write("           IDENTIFICATION DIVISION.\n")
            path = Path(tmp.name)
        try:
            violations = scan_area_a_for_divisions(path)
            self.assertTrue(violations, "Detector falhou em detectar divisão na Área B")
            self.assertIn("Área A", violations[0])
        finally:
            path.unlink(missing_ok=True)

    def test_negative_detector_working_storage_naming(self) -> None:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".cbl", delete=False, encoding="utf-8") as tmp:
            tmp.write("       WORKING-STORAGE SECTION.\n")
            tmp.write("       01 NOME-INVALIDO   PIC X(10).\n")
            tmp.write("       PROCEDURE DIVISION.\n")
            path = Path(tmp.name)
        try:
            violations = scan_working_storage_variables(path)
            self.assertTrue(violations, "Detector falhou em detectar variável sem WS-")
            self.assertIn("NOME-INVALIDO", violations[0])
        finally:
            path.unlink(missing_ok=True)

    def test_negative_detector_missing_stop_run(self) -> None:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".cbl", delete=False, encoding="utf-8") as tmp:
            tmp.write("       PROCEDURE DIVISION.\n       DISPLAY 'OI'.\n")
            path = Path(tmp.name)
        try:
            violations = scan_stop_run(path)
            self.assertTrue(violations, "Detector falhou em detectar falta de STOP RUN")
            self.assertIn("STOP RUN", violations[0])
        finally:
            path.unlink(missing_ok=True)

    def test_negative_detector_comment_indicator(self) -> None:
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".cbl", delete=False, encoding="utf-8") as tmp:
            # * in column 8 instead of column 7
            tmp.write("       * Comentario desalinhado\n")
            path = Path(tmp.name)
        try:
            violations = scan_comments_indicator(path)
            self.assertTrue(violations, "Detector falhou em detectar comentário fora da coluna 7")
            self.assertIn("coluna 7", violations[0])
        finally:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
