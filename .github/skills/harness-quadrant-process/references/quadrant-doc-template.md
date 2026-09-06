# <Nome do projeto> — Análise de Harness por Quadrante Guias × Sensores

## Metodologia

Harness de desenvolvimento é a combinação de guias e sensores que governa como
o agente de codificação atua no projeto.

Este documento usa o quadrante guias×sensores:
- X: Computacional --> Inferencial
- Y: Sensor feedback --> Guia feedforward

As coordenadas são qualitativas (priorização visual), não métrica exata.

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
