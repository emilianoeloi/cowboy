# APM no Cowboy (versão compacta)

Detalhes em [apm.md](apm.md). Diagramas em [apm.view.md](apm.view.md).

## O que é
**APM (Agent Package Manager)**: gerenciador de dependências para contexto de agentes (skills, prompts, agents, hooks, instruções, MCP). `apm.yml` declara, `apm.lock.yaml` fixa, `apm install` implanta em `.claude/` e `.github/`.

## O que fizemos
- Criamos o pacote privado `emilianoeloi/apm` com o harness (7 skills, hooks, `phase_cli`, templates).
- Removemos o harness do `cowboy` e adicionamos `apm.yml` apontando para `emilianoeloi/apm#main`.
- Novos alvos de Makefile: `apm-install`, `apm-frozen`.
- O CI voltou a rodar só os gates de COBOL (o passo do APM quebrava por falta de lockfile e secret).

## Bom
- Uma fonte para o harness; corrige uma vez, vale para todos.
- Versionado, com lockfile e hashes.
- Funciona com Claude Code e Copilot; repositório privado sem registry.
- Varredura de Unicode oculto e bloqueio de MCP transitivo.

## Ruim
- Ferramenta jovem, docs com inconsistências.
- Novo pré-requisito (`apm install`) e dependência de credencial.
- Scripts de hooks: entrega não confirmada.
- Skills/hooks são código executável: risco de supply chain.

## Boas práticas
1. Tags semânticas no pacote; consumir por tag.
2. Commitar `apm.lock.yaml`; `--frozen` no CI só depois disso.
3. `.claude/` e `.github/` são saída de build; edite `.apm/`.
4. Pacote genérico, projeto específico.
5. PAT mínimo (`GITHUB_APM_PAT`); `apm update` em PR separado.
6. Ao remover hooks, reinicie a sessão antes de apagar scripts.

## Alternativas
| Opção | Use quando |
|---|---|
| APM | vários agentes, versionamento, privado |
| Plugins/marketplace Claude Code | time 100% Claude |
| `skills` CLI / OpenSkills | só skills, rápido |
| Ruler / rulesync | só regras de texto |
| `AGENTS.md` puro | zero ferramenta |
| Submodule | harness pequeno e estável |

## Pendências
1. Rodar `apm install` (nunca executado).
2. Resolver entrega dos scripts de hooks.
3. Gerar e commitar `apm.lock.yaml`; criar secret `APM_PAT`.
4. Corrigir agents `cobol-*` que citam `phase_cli.py`.
5. Publicar `v0.1.0` e trocar `#main` por tag.
6. Decidir divisão em `harness-core` e `sdlc`.
