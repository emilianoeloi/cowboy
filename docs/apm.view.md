# APM no Cowboy (visão em diagramas)

Texto completo em [apm.md](apm.md); resumo em [apm.compacto.md](apm.compacto.md).

## 1. Antes e depois

```mermaid
flowchart LR
    subgraph ANTES["Antes: tudo no repositório"]
        A1[cowboy]
        A1 --> A2[src e tests COBOL]
        A1 --> A3[scripts de hooks]
        A1 --> A4[8 skills de harness]
        A1 --> A5[harness.config.json]
    end

    subgraph DEPOIS["Depois: harness como dependência"]
        B1[cowboy]
        B1 --> B2[src e tests COBOL]
        B1 --> B3[apm.yml]
        B3 -->|dependencies.apm| B4[(emilianoeloi/apm)]
        B4 --> B5[skills]
        B4 --> B6[hooks e scripts]
        B4 --> B7[templates]
    end

    ANTES ==> DEPOIS
```

## 2. Fluxo de instalação

```mermaid
sequenceDiagram
    actor Dev as Desenvolvedor
    participant CLI as apm CLI
    participant Pkg as emilianoeloi/apm
    participant Proj as cowboy
    participant Ag as Claude Code ou Copilot

    Dev->>CLI: apm install
    CLI->>Proj: lê apm.yml
    CLI->>Pkg: clona referência (PAT ou SSH)
    Pkg-->>CLI: pacote com .apm/
    CLI->>CLI: varredura de segurança e política
    CLI->>Proj: grava apm.lock.yaml
    CLI->>Proj: implanta em .claude/ e .github/
    Ag->>Proj: lê skills, agents, regras e hooks
```

## 3. Do pacote ao agente

```mermaid
flowchart TD
    S[".apm/ no pacote (fonte)"]
    S --> I[instructions]
    S --> P[prompts]
    S --> G[agents]
    S --> K[skills]
    S --> H[hooks json]

    I --> CI1[".claude/rules/"]
    P --> CP1[".claude/commands/"]
    G --> CG1[".claude/agents/"]
    K --> CK1[".claude/skills/"]
    H --> CH1[".claude/settings.json (mesclado)"]

    I --> GI1[".github/ nativo"]
    P --> GP1[".github/prompts/"]
    G --> GG1[".github/agents/"]
    K --> GK1[".github/skills/"]
    H --> GH1[".github/ nativo"]
```

## 4. Linha do tempo da migração

```mermaid
flowchart TD
    T1[Explorar cowboy e docs do APM] --> T2[Criar pacote local em Pessoal/apm]
    T2 --> T3[Remover harness do cowboy]
    T3 --> T4{Hooks em cache da sessão}
    T4 -->|scripts apagados| T5[Bash e Write bloqueados]
    T5 --> T6[Stubs temporários e depois reinício]
    T3 --> T7[Commit do pacote e push]
    T7 --> T8[PR 17 no cowboy]
    T8 --> T9{CI}
    T9 -->|apm-frozen sem lockfile| T10[CI falhou]
    T10 --> T11[Remover passos do APM do workflow]
    T11 --> T12[CI verde e merge]
```

## 5. Escolha de ferramenta

```mermaid
flowchart TD
    Q1{O que você precisa distribuir?}
    Q1 -->|só texto de regras| R1[AGENTS.md com Ruler ou rulesync]
    Q1 -->|só skills| R2[skills CLI ou OpenSkills]
    Q1 -->|skills, agents, hooks, MCP| Q2{Quantos agentes?}
    Q2 -->|só Claude Code| R3[Plugins e marketplace do Claude]
    Q2 -->|vários e versionado| Q3{Precisa de governança e lockfile?}
    Q3 -->|sim| R4[APM]
    Q3 -->|não, harness estável| R5[Submodule ou cópia]
```

## 6. Pendências por prioridade

```mermaid
flowchart LR
    A[1. Rodar apm install] --> B[2. Resolver scripts dos hooks]
    B --> C[3. Commitar apm.lock.yaml]
    C --> D[4. Criar secret APM_PAT]
    D --> E[5. apm-frozen de volta no CI]
    B --> F[6. Ajustar agents cobol]
    C --> G[7. Tag v0.1.0 e trocar main]
```
