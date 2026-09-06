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

.PHONY: help init-hooks setup-hooks fitness test syntax build run smoke-test clean check phase-show phase-proposal phase-apply

help: ## Exibe a lista de comandos disponíveis
	@echo "=================================================================="
	@echo "🤠 Cowboy - Comandos do Makefile"
	@echo "=================================================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'
	@echo "=================================================================="

init-hooks: setup-hooks ## Inicializa e configura os hooks locais (Git e Claude Code)

setup-hooks: ## Instala o hook pre-commit do Git e valida os hooks do Claude Code
	@echo "==> Configurando Git pre-commit hook..."
	@mkdir -p .git/hooks
	@cp scripts/git-hooks/pre-commit .git/hooks/pre-commit
	@chmod +x .git/hooks/pre-commit
	@echo "✔ Git hook instalado em .git/hooks/pre-commit"
	@echo "==> Ajustando permissões dos scripts de hooks e harness..."
	@chmod +x scripts/hooks/*.py scripts/harness/*.py 2>/dev/null || true
	@echo "==> Verificando configuração do Claude Code (.claude/settings.json)..."
	@if [ ! -f .claude/settings.json ]; then \
		mkdir -p .claude; \
		printf '{\n  "hooks": {\n    "PreToolUse": [\n      {\n        "matcher": "Write|Edit|NotebookEdit",\n        "hooks": [\n          {\n            "type": "command",\n            "command": "python3 \\"$$CLAUDE_PROJECT_DIR/scripts/hooks/pre-tool-write-guard.py\\"",\n            "timeout": 5\n          }\n        ]\n      },\n      {\n        "matcher": "Bash",\n        "hooks": [\n          {\n            "type": "command",\n            "command": "python3 \\"$$CLAUDE_PROJECT_DIR/scripts/hooks/pre-tool-bash-guard.py\\"",\n            "timeout": 5\n          }\n        ]\n      }\n    ],\n    "SessionStart": [\n      {\n        "hooks": [\n          {\n            "type": "command",\n            "command": "python3 \\"$$CLAUDE_PROJECT_DIR/scripts/hooks/session-start.py\\"",\n            "timeout": 5\n          }\n        ]\n      }\n    ]\n  }\n}\n' > .claude/settings.json; \
		echo "✔ .claude/settings.json criado com sucesso."; \
	else \
		echo "✔ .claude/settings.json já existente."; \
	fi
	@echo "==> Testando integridade dos hooks..."
	@echo '{"source":"make-init-hooks"}' | $(PYTHON) scripts/hooks/session-start.py > /dev/null
	@echo "✔ Teste de integridade de hooks concluído com sucesso!"
	@echo "✔ Todos os hooks foram configurados com sucesso."

fitness: ## Executa as fitness functions de arquitetura (sensores estruturais)
	@echo "==> Executando Fitness Functions de Arquitetura..."
	@$(PYTHON) -m unittest discover -s tests/fitness -v

test: fitness ## Alias para fitness functions

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

phase-show: ## Exibe a fase atual da change no harness
	@$(PYTHON) scripts/harness/phase_cli.py show

phase-proposal: ## Define a fase da change como proposal (Uso: make phase-proposal CHANGE=<nome>)
	@if [ -z "$(CHANGE)" ]; then echo "Erro: informe CHANGE=<nome>"; exit 1; fi
	@$(PYTHON) scripts/harness/phase_cli.py set proposal $(CHANGE)

phase-apply: ## Define a fase da change como apply (Uso: make phase-apply CHANGE=<nome>)
	@if [ -z "$(CHANGE)" ]; then echo "Erro: informe CHANGE=<nome>"; exit 1; fi
	@$(PYTHON) scripts/harness/phase_cli.py set apply $(CHANGE)
