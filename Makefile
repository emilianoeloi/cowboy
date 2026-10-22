# ==============================================================================
# Makefile - Cowboy (Calculadora COBOL & Dev Harness)
# ==============================================================================
# Comandos para inicialização de hooks, execução de fitness functions,
# verificação de sintaxe e compilação do projeto.
# ==============================================================================

PYTHON ?= python3
COBC ?= cobc
BIN ?= calculadora
SRC ?= src/CALCULADORA.cbl

.PHONY: help apm-install apm-frozen fitness test test-unit syntax build run smoke-test clean check

help: ## Exibe a lista de comandos disponíveis
	@echo "=================================================================="
	@echo "🤠 Cowboy - Comandos do Makefile"
	@echo "=================================================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'
	@echo "=================================================================="

apm-install: ## Instala o harness via APM (apm.yml)
	@apm install

apm-frozen: ## Instala o harness a partir do apm.lock.yaml (CI)
	@apm install --frozen

fitness: ## Executa as fitness functions de arquitetura (sensores estruturais)
	@echo "==> Executando Fitness Functions de Arquitetura..."
	@$(PYTHON) -m unittest discover -s tests/fitness -v

test-unit: build ## Executa a suíte de testes unitários funcionais da calculadora
	@echo "==> Executando Testes Unitários Funcionais..."
	@$(PYTHON) -m unittest discover -s tests/unit -v

test: fitness test-unit ## Executa todos os testes (fitness de arquitetura e unitários)

syntax: ## Valida a sintaxe do código COBOL com GnuCOBOL (cobc)
	@if command -v $(COBC) >/dev/null 2>&1; then \
		echo "==> Verificando sintaxe com $(COBC)..."; \
		$(COBC) -fsyntax-only $(SRC); \
		echo "✔ Sintaxe válida em $(SRC)."; \
	else \
		echo "⚠ GnuCOBOL ($(COBC)) não encontrado no PATH."; \
		echo "Instale via 'brew install gnu-cobol' (macOS) ou 'sudo apt install gnucobol' (Linux)."; \
		exit 1; \
	fi

build: ## Compila o programa COBOL para binário executável
	@if command -v $(COBC) >/dev/null 2>&1; then \
		echo "==> Compilando $(SRC) -> $(BIN)..."; \
		$(COBC) -x -o $(BIN) $(SRC); \
		echo "✔ Compilação concluída: ./$(BIN)"; \
	else \
		echo "⚠ GnuCOBOL ($(COBC)) não encontrado no PATH."; \
		echo "Instale via 'brew install gnu-cobol' (macOS) ou 'sudo apt install gnucobol' (Linux)."; \
		exit 1; \
	fi

run: ## Executa o binário compilado da calculadora
	@if [ -f "./$(BIN)" ]; then \
		./$(BIN); \
	else \
		echo "⚠ Binário './$(BIN)' não encontrado. Execute 'make build' primeiro."; \
		exit 1; \
	fi

smoke-test: build ## Compila e executa teste automatizado de fumaça (soma 10 + 20)
	@echo "==> Executando smoke test (Operação: Soma 10 + 20)..."
	@printf "1\n10\n20\n" | ./$(BIN)

check: fitness ## Executa bateria completa de verificações de qualidade
	@if command -v $(COBC) >/dev/null 2>&1; then \
		$(MAKE) syntax; \
	else \
		echo "ℹ cobc não disponível localmente; verificação de sintaxe pulada."; \
	fi
	@echo "✔ Quality gate local aprovado!"

clean: ## Limpa binários compilados e caches temporários
	@echo "==> Limpando artefatos..."
	@rm -f $(BIN) *.o
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "✔ Limpeza concluída."

