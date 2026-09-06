"""Testes unitários funcionais da Calculadora COBOL via subprocess e unittest.

Executa o binário compilado './calculadora' injetando entradas simuladas via stdin
e validando as respostas formatadas em stdout/stderr para todas as operações
matemáticas e tratamentos de exceção.
"""

import os
import shutil
import subprocess
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
BIN_PATH = REPO_ROOT / "calculadora"
SRC_PATH = REPO_ROOT / "src" / "CALCULADORA.cbl"


class TestCalculadoraCOBOL(unittest.TestCase):
    """Suíte de testes unitários funcionais para o executável da Calculadora COBOL."""

    @classmethod
    def setUpClass(cls) -> None:
        """Garante que o executável da calculadora existe; compila se necessário."""
        if not BIN_PATH.exists():
            cobc = shutil.which("cobc")
            if not cobc:
                raise unittest.SkipTest(
                    "Binário 'calculadora' não encontrado e compilador 'cobc' não disponível no PATH."
                )
            cmd = [cobc, "-x", "-o", str(BIN_PATH), str(SRC_PATH)]
            proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_ROOT))
            if proc.returncode != 0:
                raise unittest.SkipTest(
                    f"Falha ao compilar {SRC_PATH} durante o setup dos testes:\n{proc.stderr}"
                )

    def executar(self, inputs: list[str]) -> str:
        """Executa o binário fornecendo inputs via stdin e retorna stdout normalizado."""
        payload = "\n".join(inputs) + "\n"
        proc = subprocess.run(
            [str(BIN_PATH)],
            input=payload,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=5,
            cwd=str(REPO_ROOT),
        )
        return proc.stdout.replace("\r\n", "\n")

    # ==========================================================================
    # Operação 1: Soma
    # ==========================================================================

    def test_soma_dois_numeros_positivos(self) -> None:
        """Valida a soma de dois números inteiros positivos (10 + 20 = 30)."""
        output = self.executar(["1", "10", "20"])
        self.assertIn("RESULTADO DA SOMA", output)
        self.assertIn("00010 + 00020 =         30", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    def test_soma_com_zero(self) -> None:
        """Valida a soma com operando zero (0 + 50 = 50)."""
        output = self.executar(["1", "0", "50"])
        self.assertIn("RESULTADO DA SOMA", output)
        self.assertIn("00000 + 00050 =         50", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    # ==========================================================================
    # Operação 2: Subtração
    # ==========================================================================

    def test_subtracao_resultado_positivo(self) -> None:
        """Valida a subtração com resultado positivo (50 - 20 = 30)."""
        output = self.executar(["2", "50", "20"])
        self.assertIn("RESULTADO DA SUBTRACAO", output)
        self.assertIn("00050 - 00020 =         30", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    def test_subtracao_resultado_negativo(self) -> None:
        """Valida a subtração com resultado negativo com sinal explícito (20 - 50 = -30)."""
        output = self.executar(["2", "20", "50"])
        self.assertIn("RESULTADO DA SUBTRACAO", output)
        self.assertIn("00020 - 00050 =        -30", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    # ==========================================================================
    # Operação 3: Multiplicação
    # ==========================================================================

    def test_multiplicacao_valores_regulares(self) -> None:
        """Valida a multiplicação entre números inteiros (25 x 4 = 100)."""
        output = self.executar(["3", "25", "4"])
        self.assertIn("RESULTADO DA MULTIPLICACAO", output)
        self.assertIn("00025 x 00004 =        100", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    def test_multiplicacao_por_zero(self) -> None:
        """Valida a multiplicação por zero (100 x 0 = 0)."""
        output = self.executar(["3", "100", "0"])
        self.assertIn("RESULTADO DA MULTIPLICACAO", output)
        self.assertIn("00100 x 00000 =          0", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    # ==========================================================================
    # Operação 4: Divisão
    # ==========================================================================

    def test_divisao_exata(self) -> None:
        """Valida a divisão exata com 2 casas decimais (20 / 4 = 5.00)."""
        output = self.executar(["4", "20", "4"])
        self.assertIn("RESULTADO DA DIVISAO", output)
        self.assertIn("00020 / 00004 =          5.00", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    def test_divisao_com_casas_decimais(self) -> None:
        """Valida a divisão com resultado decimal formatado (10 / 4 = 2.50)."""
        output = self.executar(["4", "10", "4"])
        self.assertIn("RESULTADO DA DIVISAO", output)
        self.assertIn("00010 / 00004 =          2.50", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    def test_divisao_por_zero_bloqueio(self) -> None:
        """Valida o bloqueio gracioso e mensagem clara em caso de divisão por zero."""
        output = self.executar(["4", "10", "0"])
        self.assertIn("ERRO: Divisao por zero nao e permitida!", output)
        self.assertNotIn("RESULTADO DA DIVISAO", output)

    # ==========================================================================
    # Operação 5: Logaritmo (Base 10)
    # ==========================================================================

    def test_logaritmo_numero_positivo(self) -> None:
        """Valida o cálculo do logaritmo base 10 com 6 casas decimais (log10(100) = 2.000000)."""
        output = self.executar(["5", "100"])
        self.assertIn("RESULTADO DO LOGARITMO", output)
        self.assertIn("LOG10(00100) =     2.000000", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    def test_logaritmo_zero_bloqueio(self) -> None:
        """Valida o bloqueio gracioso ao tentar calcular logaritmo de zero."""
        output = self.executar(["5", "0"])
        self.assertIn("ERRO: Logaritmo de zero nao e permitido!", output)
        self.assertNotIn("RESULTADO DO LOGARITMO", output)

    # ==========================================================================
    # Operação 6: Juros Simples
    # ==========================================================================

    def test_juros_simples_calculo_sucesso(self) -> None:
        """Valida o cálculo de juros simples e montante (C=1000, i=5%, t=2 -> J=100.00, M=1100.00)."""
        output = self.executar(["6", "1000.00", "5.00", "2"])
        self.assertIn("RESULTADO DOS JUROS SIMPLES", output)
        self.assertIn("Capital:  +0001000.00", output)
        self.assertIn("Taxa (%): +005.00", output)
        self.assertIn("Tempo:    +002", output)
        self.assertIn("Juros:           100.00", output)
        self.assertIn("Montante:       1100.00", output)
        self.assertIn("Programa encerrado com sucesso!", output)

    def test_juros_simples_bloqueio_valores_negativos(self) -> None:
        """Valida a recusa e mensagem de erro caso parâmetros de juros sejam negativos."""
        output = self.executar(["6", "-100.00", "5.00", "2"])
        self.assertIn("ERRO: Valores negativos nao sao permitidos!", output)
        self.assertNotIn("RESULTADO DOS JUROS SIMPLES", output)

    # ==========================================================================
    # Controle de Menu e Validações
    # ==========================================================================

    def test_opcao_menu_invalida(self) -> None:
        """Valida que uma opção fora do menu (ex: 9) encerra com mensagem de erro amigável."""
        output = self.executar(["9"])
        self.assertIn("Opcao invalida! Encerrando.", output)
        self.assertNotIn("RESULTADO", output)


if __name__ == "__main__":
    unittest.main()
