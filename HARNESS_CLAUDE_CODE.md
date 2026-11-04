# Harness do Cowboy no Claude Code via APM

Relatório da migração do harness para o Claude Code, com o pacote APM como fonte da verdade.

- Pacote: `emilianoeloi/apm`, tag `v0.1.0` (commit `335a22e`).
- Branch no Cowboy: `feat/harness-claude-code`.

## Mapeamento (Fase 0)

| Origem (Copilot) | Primitiva APM | Destino no Claude Code | Adaptação |
|---|---|---|---|
| `.github/copilot-instructions.md` | instructions | Fora do Claude (`.apm/_pending/`) | Específico do Copilot. Duplicaria o conteúdo do `AGENTS.md` |
| `AGENTS.md` | sem primitiva | Importado por `CLAUDE.md` (`@AGENTS.md`) | Fonte da verdade; não copiado |
| `.github/agents/*.agent.md` (5) | agents | `.claude/agents/<nome>.md` | `tools` e `handoffs` no formato Copilot (ver PENDENTE) |
| `.github/prompts/*.prompt.md` (7; `sdlc` fica fora do pacote) | prompts | `.claude/commands/<nome>.md` | `mode` e `name` descartados pelo APM |
| `.github/skills/*/SKILL.md` (3; `conversa-release` fica fora do pacote) | skills | `.claude/skills/` e `.agents/skills/` | Sem alteração de conteúdo |
| Fitness functions (13) | sem primitiva | Hook `Stop` (H1) | `make fitness`; falha vira `exit 2` |
| Bloqueio de envio ao remoto | hook | `PreToolUse` em Bash (H2) | Regra do `CLAUDE.md` |
| `.github/workflows/ci.yml` | fora do harness | Sem equivalente | Mantido; não usa APM |
| Fase proposal/apply | sem primitiva | Sem equivalente | Código do harness antigo não está no repo |

## OK

- Fitness functions (13) e testes unitários (14) passam em cada etapa.
- `make syntax` e `make smoke-test` passam.
- Os arquivos rastreados do Copilot em `.github/` não mudaram. A saída do APM gera os mesmos arquivos.
- `apm install --frozen` funciona com o lockfile commitado.
- `CLAUDE.md` tem 19 linhas e importa `@AGENTS.md`, sem duplicar o conteúdo.
- Hooks H1 e H2 foram testados com 7 casos: push direto, push encadeado, texto citando o comando, `ls`, Stop com loop guard, Stop verde e Stop com fitness falhando.

## CORRIGIDO

- `main`: removidas referências a skills e prompts inexistentes (`4785e60`, cherry-pick de `fe29d24`).
- `.gitignore`: os padrões amplos `*spdd*` e `*openspec*` escondiam as skills geradas. Trocados por `/openspec/` e `/spdd/`.
- Pacote, `cobol-vibecoder`: YAML inválido na `description` (faltavam aspas, por causa de `: `).
- Pacote, prompts: removido o variation selector (U+FE0F) dos títulos com emoji, que o APM sinalizava.
- Pacote, hooks: os scripts em `scripts/hooks/` não são entregues pelo APM. Os hooks antigos foram para `.apm/_pending/`.
- Pacote, instruções: `copilot-instructions.md` duplicaria o contexto do Claude. Foi para `.apm/_pending/`.
- Pacote, hook H2: a regex bloqueava qualquer comando que citasse `git push`, inclusive mensagens de commit. Agora só casa no início do comando ou depois de `;`, `&`, `|` ou `(` (PR #2).
- Lockfile: com um branch como referência, o APM reaproveita o commit travado. Foi preciso `apm install --update`.

## PENDENTE

1. **Tools dos agentes (D5).** Os `tools` estão no formato do Copilot (`['read', 'edit', ...]`). Não confirmei se o Claude Code aplica esses nomes ou os ignora. Opções: remover a linha (todos herdam as ferramentas) ou manter.
2. **Skills antigas (D6).** Sete skills do harness antigo entram em `.claude/skills/` e `.agents/skills/`. Algumas citam `opsx-*` e `spdd-*`, que não existem no repo.
3. **Duplicação no Copilot (D8).** `cobol-calculadora` e `readme-manutencao` existem em `.github/skills/` e em `.agents/skills/`.
4. **Hooks no Copilot.** O APM também gera `.github/hooks/apm-cowboy.json`. O Copilot não tem `CLAUDE_PROJECT_DIR` nem `stop_hook_active`, então o loop guard pode não valer lá. Não testado.
5. **CI com `--frozen`.** Não adicionado. Exige o secret `APM_PAT`, que não existe. Sem o secret, o job quebra.
6. **Validação no Claude Code.** Agentes, comandos e hooks foram validados por geração e testes de script, não por uma sessão real de agente.
7. **Fase 5 (limpeza).** Nada foi removido. Candidatos: `.github/agents/`, `.github/prompts/`, `.github/skills/` (depois da migração), `.github/copilot-instructions.md`, `docs/apm*.md`, `VALIDACAO_APM.md`, `.apm/_pending/` no pacote e `conversa-release` (órfã, sem frontmatter, fora do pacote). Cada item precisa de aprovação.
8. **Ambiente local.** O `GITHUB_TOKEN` em `~/.zshrc` está inválido e sobrescreve o login do `gh`.
9. **Limite de commits.** Os arquivos gerados e o lockfile ficaram fora do limite de 400 linhas, como você aprovou. Com a Fase 5, o PR pode passar de 6 commits.

## Decisão de versionamento (revisada)

A saída gerada pelo APM (`.claude/`, `.agents/` e `.github/hooks/apm-*.json`) **não é versionada** no Cowboy. Ela é regenerada com `make apm-install` a partir do lockfile (`apm.lock.yaml`, commitado). Motivo: o harness deve morar só no pacote `emilianoeloi/apm`, e versionar as cópias duplicaria o conteúdo. A decisão anterior (D3) foi revertida. As fontes antigas em `.github/agents/`, `.github/prompts/` e `.github/skills/` continuam no repo até a Fase 5.
