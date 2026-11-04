# <Nome do projeto> — Análise de Harness por Quadrante Guias × Sensores

## Metodologia

Harness de desenvolvimento é a combinação de guias e sensores que governa como
o agente de codificação atua no projeto.

Este documento usa o quadrante guias×sensores:
- X: Computacional --> Inferencial
- Y: Sensor feedback --> Guia feedforward

As coordenadas são qualitativas (priorização visual), não métrica exata.

## Notas do Harness

- **Data da avaliação**: `<YYYY-MM-DD>`
- **Escopo**: `<repositório(s) ou área avaliada>`
- **Confiança**: `<alta|média|baixa>` — `<justificativa curta>`

### Nota de eficácia: `<0–10>` (média das dimensões conhecidas x 2)

| Dimensão | Pontuação (0–5) | Evidência (arquivo-fonte) | Justificativa |
|---|---|---|---|
| Clareza das guias | `<n ou desconhecida>` | `<path>` | `<texto objetivo>` |
| Automação | `<n ou desconhecida>` | `<path>` | `<texto objetivo>` |
| Cobertura de feedback | `<n ou desconhecida>` | `<path>` | `<texto objetivo>` |
| Rastreabilidade/evolução | `<n ou desconhecida>` | `<path>` | `<texto objetivo>` |
| Adoção/baixo atrito | `<n ou desconhecida>` | `<path>` | `<texto objetivo>` |

> Dimensões marcadas como "desconhecida" são excluídas do cálculo da média,
> não zeradas.

### Nota de complexidade/tamanho: `<0–10>` (`<minimalista|leve|médio|pesado|extremo>`)

- **Evidência**: `<artefatos e gates que geram o custo observado>`

### Limitações e próximos passos

- **Limitações**: `<o que não pôde ser avaliado ou verificado nesta rodada>`
- **Próximos passos**: `<o que revisar na próxima avaliação>`

## Contexto de Mercado

| Fonte | Data/versão | Prática observada | Evidência | Aplicabilidade | Aderência do repositório |
|---|---|---|---|---|---|
| `<fonte real ou "não verificado">` | `<data/versão>` | `<prática>` | `<evidência>` | `<aplicabilidade>` | `<aderência>` |

> Se nenhuma fonte externa verificável foi identificada, use a linha:
> "Contexto de mercado não verificado nesta avaliação — nenhuma fonte externa
> identificada." A nota interna (eficácia/complexidade) nunca equivale a uma
> média estatística do mercado.

## Diagrama

```mermaid
quadrantChart
    title Harness <Nome do projeto> — Quadrante Guias × Sensores
    x-axis Computacional --> Inferencial
    y-axis Sensor feedback --> Guia feedforward

    quadrant-1 Guia Inferencial
    quadrant-2 Guia Computacional
    quadrant-3 Sensor Computacional
    quadrant-4 Sensor Inferencial

    <Ponto 1>: [0.80, 0.90]
    <Ponto 2>: [0.30, 0.70]
    <Ponto 3>: [0.20, 0.25]
    <Ponto 4>: [0.75, 0.30]
```

## Rastreabilidade

| Ponto | Arquivo-fonte | Quadrante | Justificativa |
|---|---|---|---|
| <Ponto 1> | `<path/arquivo-1>` | Guia Inferencial | <texto objetivo> |
| <Ponto 2> | `<path/arquivo-2>` | Guia Computacional | <texto objetivo> |
| <Ponto 3> | `<path/arquivo-3>` | Sensor Computacional | <texto objetivo> |
| <Ponto 4> | `<processo ou arquivo>` | Sensor Inferencial | <texto objetivo> |

## Lacunas priorizadas

| # | Lacuna | Risco | Próximo passo |
|---|---|---|---|
| 1 | <lacuna de maior risco> | Alto | <ação concreta + arquivo/skill> |
| 2 | <lacuna> | Médio | <ação concreta + arquivo/skill> |
| 3 | <lacuna> | Médio | <ação concreta + arquivo/skill> |
| 4 | <lacuna> | Baixo | <ação concreta + arquivo/skill> |

## Próximas ações recomendadas

1. <ação 1>
2. <ação 2>
3. <ação 3>
