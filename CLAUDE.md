# CLAUDE.md

@AGENTS.md

As instruções do projeto estão em `AGENTS.md`, importado acima. Este arquivo
traz só o que é específico do Claude Code.

## Regras operacionais (Claude Code)

- Não fazer `git push` sem confirmação explícita do usuário.
- Não capturar exceções de forma ampla sem justificativa.
- Não expor secrets em logs, eventos ou artefatos.

## Harness (APM)

Agentes, comandos e skills do Claude Code são gerados pelo APM a partir do
pacote `emilianoeloi/apm`, declarado em `apm.yml`:

- `.claude/agents/`, `.claude/commands/`, `.claude/skills/`, `.claude/rules/`
- Não edite esses arquivos nem as cópias em `.github/` à mão: edite o pacote.

```bash
make apm-install   # instala o harness (requer gh auth login ou GITHUB_APM_PAT)
```

## Quality gates mínimos

- Instalação do harness: `make apm-install`
- Fitness functions de arquitetura: `make fitness` (ou `python3 -m unittest discover -s tests/fitness`)
- Testes unitários funcionais da calculadora: `make test-unit` (ou `python3 -m unittest discover -s tests/unit`)
- Bateria completa de testes: `make test`
- Checagem de sintaxe: `make syntax` (ou `cobc -fsyntax-only src/CALCULADORA.cbl`)
- Compilação: `make build` (ou `cobc -x -o calculadora src/CALCULADORA.cbl`)
- Execução: `make run` (ou `./calculadora`)
- Smoke test automatizado: `make smoke-test`

## Escopo

Este arquivo é um guia básico para o Claude Code. Detalhes de arquitetura,
segurança e convenções estão em `AGENTS.md`.
