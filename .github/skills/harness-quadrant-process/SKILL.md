---
name: harness-quadrant-process
description: >
  Executa um processo repetível em 4 fases (propose, analyze, canvas, geração)
  para evoluir harness de desenvolvimento e sempre entregar um documento
  objetivo/prático com diagrama de quadrante guias×sensores.
license: MIT
metadata:
  author: local
  version: "1.0"
---

# Skill — Harness Quadrant Process

Use este skill quando o usuário quiser repetir o mesmo fluxo em um ou mais
repositórios, com foco em melhorar harness e gerar uma saída documental
consistente.

## Objetivo

Entregar, ao fim do fluxo, um arquivo em `Docs/` com:
- Diagnóstico do harness atual
- Diagrama Mermaid `quadrantChart` (guias × sensores)
- Tabela de rastreabilidade (ponto -> arquivo-fonte -> justificativa)
- Backlog priorizado de lacunas de maior risco

## Fluxo obrigatório (4 fases)

1. **Propose**
2. **Analyze**
3. **Canvas**
4. **Geração**

Não pule fases. Se uma fase tiver ambiguidade material, pare e pergunte ao
usuário antes de seguir.

## Fase 1 — Propose

Objetivo: criar e validar os artefatos de planejamento sem implementar.

Passos:
1. Derivar um nome de change em kebab-case (ex.: `document-harness-quadrant-analysis`).
2. Executar o fluxo de proposal do OpenSpec (schema padrão, salvo pedido contrário).
3. Garantir que os artefatos mínimos existem: `proposal.md`, `design.md`, `tasks.md`.
4. Se for documentação pura de harness, marcar `skip_specs: true` em `.openspec.yaml`.
5. Validar com `openspec validate <change> --strict`.

Saída esperada da fase:
- Change válido no OpenSpec, pronto para implementação.

## Fase 2 — Analyze

Objetivo: produzir contexto enriquecido, estratégico e rastreável.

Passos:
1. Ler completamente os artefatos do change OpenSpec (`proposal.md`, `design.md`, `tasks.md`).
2. Fazer exploração orientada a conceito (não varrer o repositório inteiro):
   - Guias inferenciais: `AGENTS.md`, `CLAUDE.md`, `copilot-instructions`, skills e prompts.
   - Guias computacionais: manifests, configs de lint/type/editor.
   - Sensores computacionais: pre-commit/hooks/CI/fitness functions/guardrails.
   - Sensores inferenciais: code-review humano/segundo agente/skills de revisão.
3. Consolidar riscos, ambiguidades e cobertura de critérios.
4. Salvar em `spdd/analysis/` com convenção:
   - `GGQPA-XXX-YYYYMMDDHHmm-[Analysis]-<descricao>.md`

Saída esperada da fase:
- Documento de análise estratégica completo, sem placeholders.

## Fase 3 — Canvas

Objetivo: transformar análise em prompt estruturado acionável.

Passos:
1. Ler integralmente o arquivo da Fase 2.
2. Gerar REASONS Canvas completo (`Requirements`, `Entities`, `Approach`,
   `Structure`, `Operations`, `Norms`, `Safeguards`).
3. Garantir que `Operations` define tarefas executáveis para criar o documento
   final em `Docs/`.
4. Salvar em `spdd/prompt/` com convenção:
   - `GGQPA-XXX-YYYYMMDDHHmm-[Docs]-<descricao>.md`

Saída esperada da fase:
- Prompt estruturado pronto para execução, sem implementar ainda.

## Fase 4 — Geração

Objetivo: gerar o artefato final objetivo/prático no repositório.

Passos:
1. Ler o prompt REASONS completo.
2. Executar as operações na ordem definida, sem replanejar.
3. Criar o documento final em `Docs/` usando o template de referência:
   - `references/quadrant-doc-template.md`
4. Validar:
   - Sintaxe Mermaid do `quadrantChart`
   - Rastreabilidade: todo ponto cita arquivo real
   - Escopo: somente arquivos esperados alterados
   - OpenSpec: `openspec validate <change> --strict`

Saída esperada da fase:
- Documento final criado e tarefas do change atualizadas.

## Regras de qualidade

1. **Objetividade**: escrever curto, direto e orientado a ação.
2. **Rastreabilidade total**: nada no quadrante pode ser "achismo" sem arquivo-fonte.
3. **Priorização prática**: lacunas ordenadas por risco, com próximo passo claro.
4. **Sem implementação prematura**: código só na Fase 4.
5. **Consistência cross-repo**: manter o mesmo formato de saída em qualquer projeto.

## Regras de quadrante

- Eixo X: `Computacional --> Inferencial`
- Eixo Y: `Sensor feedback --> Guia feedforward`
- Quadrantes:
  - `quadrant-1 Guia Inferencial`
  - `quadrant-2 Guia Computacional`
  - `quadrant-3 Sensor Computacional`
  - `quadrant-4 Sensor Inferencial`

As coordenadas são qualitativas para priorização visual; documente isso na
seção de metodologia do artefato final.

## Skill chaining recomendada

- Para auditoria profunda do harness: usar `dev-harness-architect`.
- Para proposal robusta: usar `openspec-propose`.
- Para converter regra recorrente em teste: usar `architecture-fitness-functions`.
- Para gate de fase em novos projetos: usar `install-dev-harness`.

## Definition of Done

Considere concluído apenas quando todos os itens abaixo forem verdadeiros:
1. Change OpenSpec válido.
2. Arquivo em `spdd/analysis/` criado.
3. Arquivo em `spdd/prompt/` criado.
4. Documento final em `Docs/` criado com `quadrantChart`.
5. Tabela de rastreabilidade e backlog de lacunas presentes.
6. Resumo final com próximos passos de melhoria do harness.
