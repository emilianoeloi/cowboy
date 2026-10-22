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

## Harness (APM)

O harness (hooks, gate de fase, skills de SDLC) não vive mais neste repositório:
é distribuído pelo pacote privado `emilianoeloi/apm`, declarado em `apm.yml`.

```bash
apm install   # ou: make apm-install
```

Arquivos em `.claude/` e `.github/` gerados pelo APM são saída de build;
edite o pacote, não a cópia instalada. Requer `GITHUB_APM_PAT` (ou `gh auth login`).

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
