# Validação da estrutura APM — Cowboy

Relatório da auditoria de agentes, skills, referências e documentação após a migração do harness para o pacote APM (`emilianoeloi/apm`, commit `77c3ba6`).

## OK — o que está certo

- **Manifesto:** `apm.yml` é válido (`name`, `version`, `targets: [claude, copilot]`, dependência `emilianoeloi/apm#main`).
- **Alvos do Makefile:** `apm-install` e `apm-frozen` existem e apontam para o manifesto.
- **Remoção do harness antigo:** nenhum arquivo do harness antigo (`.claude/`, `scripts/`, `harness.config.json`) restou no repositório.
- **Agentes:** os cinco arquivos em `.github/agents/` têm papel claro, descrição e handoffs que apontam para agentes existentes.
- **Skills em uso:** `cobol-calculadora` e `readme-manutencao` são referenciadas por agentes e prompts.
- **Testes:** `make fitness` (13 testes) e `make test-unit` (14 testes) passam.
- **CI:** `.github/workflows/ci.yml` roda fitness, syntax, build e smoke test sem depender do APM.
- **Falso positivo:** `CONTRIBUTING.md` cita `docs/descricao-da-mudanca`, mas é um nome de branch em um exemplo de `git checkout -b`, não um arquivo.

## CORRIGIDO — ajustado neste PR

Commit `fe29d24` — `docs: remove referencias a skills e prompt inexistentes`:
- Removidas as linhas de `openspec-workflow`, `openspdd-workflow`, `vibe-coding-fundamentals` e `architecture-fitness-functions` das tabelas de skills e da árvore de `AGENTS.md`, `.github/copilot-instructions.md` e README (PT, EN e ZH). Esses arquivos foram apagados na migração e os links estavam quebrados.
- Removido o prompt `implementar-divisao.prompt.md` das tabelas, listas e árvores. O arquivo não existe, e a divisão já está implementada em `src/CALCULADORA.cbl`.
- Incluído `cobol-vibecoder.agent.md` na árvore do README (PT, EN e ZH). O agente existe e estava fora da documentação.
- Ajustados os conectores da árvore de skills no README e em `AGENTS.md`, já que a última skill mudou.

Commit `89e1c11` — `docs(readme): documentar o harness via APM nos 3 idiomas`:
- Nova seção sobre o harness APM nos três READMEs: o que é, `make apm-install`, e que `.claude/` e `.github/` gerados são saída de build.

## PENDENTE — precisa de decisão

1. **Fonte da verdade.** `CLAUDE.md` diz que `.claude/` e `.github/` são saída de build e que se deve editar o pacote. Mas agentes, skills e prompts do projeto estão escritos direto em `.github/`, sem diretório `.apm/` de origem. Mover o conteúdo para `.apm/` é uma mudança grande; fica como sugestão.
2. **Skills de SDLC ausentes.** A metodologia OpenSpec/OpenSPDD (`AGENTS.md`, seção "Metodologia SDLC", e `cobol-planner`/`cobol-coder`) depende de skills que não existem mais no repositório (`opsx-propose`, `spdd-analysis`, `spdd-reasons-canvas`, `spdd-generate`). Decidir: restaurar essas skills (do pacote APM ou do histórico) ou remover a metodologia dos agentes.
3. **Órfãos.** `.github/skills/conversa-release/SKILL.md` não é referenciada por nenhum agente, prompt ou documento. Decidir: apagar ou integrar.
4. **Prompts sem tabela.** `.github/prompts/sdlc.prompt.md` não está listado em lugar nenhum e é uma nota de trabalho com erros de digitação. `manutencao-repositorio.prompt.md` está em `AGENTS.md`, mas não em `copilot-instructions.md`. Decidir: apagar, integrar ou documentar.
5. **`apm.lock.yaml` ausente.** `docs/apm.md` diz que `apm install` ainda não foi executado. Sem o lockfile, `make apm-frozen` falha e o CI não consegue reproduzir o harness. Rodar `make apm-install` exige `GITHUB_APM_PAT` ou `gh auth login`.
6. **`.gitignore` amplo demais.** Os padrões `*openspec*`, `*spdd*` e `*opsx-*` vão ignorar em silêncio qualquer artefato futuro com esses nomes. Só `.github/skills/**` está reincluído. Sugestão: trocar por caminhos específicos.
7. **CI não roda testes unitários.** O job roda `make fitness`, `make syntax`, `make build` e `make smoke-test`, mas não `make test-unit`. Sugestão: incluir.
