# exportSkills — Dev Harness Kit (stack-agnostic)

> Nota: este arquivo é referência, não uma skill. Não segue o padrão
> `<dir>/SKILL.md` nem tem front-matter de skill, então não é descoberto pelo
> Claude Code — não confundir com a skill ativa [`harness/SKILL.md`](../SKILL.md).

Extraído do harness de desenvolvimento do **UIMaker ADK** — a parte que governa
o *agente de codificação* (Claude Code, Copilot, Codex), não o runtime de
agentes LLM do produto (ADK/Python específico). O que está aqui é o padrão, não
a implementação Python: cada peça foi generalizada para funcionar em qualquer
stack — iOS/Swift, Android/Kotlin, Node/TS, Go, Rust, etc.

## O que é um "harness de dev"

Tudo que envolve o agente de codificação além do próprio modelo: instruções,
configuração e sensores que aumentam a qualidade e a segurança das ações dele.
Modelo mental completo em [`dev-harness-architect/reference/harness-model.md`](dev-harness-architect/reference/harness-model.md).

Resumo em uma frase: **Guias** (o que o agente sabe antes de agir) × **Sensores**
(o que verifica o que ele produziu) — cada eixo tem uma variante inferencial
(linguagem natural) e uma computacional (mecânica, determinística).

## Os 3 skills

| Skill | Quando usar |
|---|---|
| [`dev-harness-architect`](../../dev-harness-architect/SKILL.md) | Diagnosticar um harness existente ou desenhar um do zero, em qualquer stack. Ponto de partida. |
| [`install-dev-harness`](../../install-dev-harness/SKILL.md) | Instalar o esqueleto do harness (CLAUDE.md, hooks de fase, config) num projeto novo ou existente. |
| [`architecture-fitness-functions`](../../architecture-fitness-functions/SKILL.md) | Transformar uma regra de arquitetura em um teste automatizado e determinístico, em qualquer stack de teste. |

## Como usar em outro projeto

1. Copie a pasta `exportSkills/` inteira para o novo repositório, em
   `.claude/skills/` (ou `.github/skills/` se o alvo for Copilot).
2. Rode `/dev-harness-architect` (ou invoque o skill) para auditar o que já
   existe e decidir o que falta.
3. Rode `/install-dev-harness` para materializar o esqueleto (CLAUDE.md,
   `harness.config.json`, hooks de fase, wiring em `settings.json`).
4. Use `/architecture-fitness-functions` sempre que uma regra de arquitetura
   for violada duas vezes por revisão manual — é o sinal de promovê-la a
   sensor computacional.

## O que fica de fora (por design)

Este pacote cobre **só o harness de dev**. Duas camadas do projeto de origem
ficam de fora porque não são o harness de dev e já são portáveis por conta
própria:

- **OpenSpec** (`openspec-propose`, `openspec-apply-change`, `openspec-explore`,
  `openspec-sync-specs`, `openspec-archive-change`) — já é uma ferramenta/skill
  set genérico e stack-agnostic (`openspec init` num projeto Swift funciona
  igual a um projeto Python). Instale-o à parte; os hooks de fase deste pacote
  foram desenhados para conversar com ele (gate de escrita durante a fase
  `proposal`).
- **SPDD / REASONS Canvas** (`spdd-analysis`, `spdd-reasons-canvas`,
  `spdd-generate`) — é a camada de geração de prompt estruturado do UIMaker
  ADK, específica demais do domínio (Figma → Android/iOS) para generalizar
  aqui sem perder substância. Fica como referência, não como skill exportado.

## Proveniência

Extraído de `.github/skills/harness/SKILL.md`, `docs/harness.md`,
`.claude/settings.json` (hooks), `scripts/hooks/*.py`,
`tests/structural/test_architecture.py` e `AGENTS.md` do UIMaker ADK
(commit `98e3236`, 2026-08-23).
