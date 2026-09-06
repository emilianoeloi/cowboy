# CLAUDE.md

Harness local do Claude Code para este repositório.

## Fonte de verdade do projeto

1. `AGENTS.md` (raiz do repo)
2. Specs / contratos de domínio, se houver

Se houver conflito, siga a ordem acima.

## Regras operacionais

- Toda escrita em filesystem deve respeitar os limites do projeto.
- Não fazer `git push` sem confirmação explícita do usuário.
- Não capturar exceções de forma ampla sem justificativa.
- Não expor secrets em logs, eventos ou artefatos.

## Fase da change

Este projeto usa gate de fase (planejamento vs. implementação). Antes de
implementar, declare a fase:

```bash
python3 scripts/harness/phase_cli.py set proposal <nome-da-mudanca>
# ... planejamento (specs, design, tasks) ...
python3 scripts/harness/phase_cli.py set apply <nome-da-mudanca>
# ... agora escrita em código é liberada ...
```

Enquanto a fase for `proposal`, o hook `pre-tool-write-guard.py` bloqueia
escrita em `src/` e `docs/` e o hook `pre-tool-bash-guard.py`
bloqueia `git commit`/`add`/`merge`/`rebase`. Consulte a fase atual com
`python3 scripts/harness/phase_cli.py show`.

## Quality gates mínimos

- Inicialização de hooks locais: `make init-hooks`
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
