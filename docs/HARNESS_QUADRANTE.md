# Calculadora COBOL — Análise de Harness por Quadrante Guias × Sensores

## Metodologia

Harness de desenvolvimento é a combinação de guias e sensores que governa como
o agente de codificação atua no projeto, estabelecendo limites operacionais e
sensores de validação contínua.

Este documento utiliza o quadrante bidimensional guias × sensores:
- **Eixo X**: Computacional (0.0) --> Inferencial (1.0)
- **Eixo Y**: Sensor feedback (0.0) --> Guia feedforward (1.0)

Distribuição dos quatro quadrantes:
- **quadrant-1 Guia Inferencial** (Superior Direito): Orientações e regras expressas em linguagem natural.
- **quadrant-2 Guia Computacional** (Superior Esquerdo): Restrições formais e configurações estruturadas de máquina.
- **quadrant-3 Sensor Computacional** (Inferior Esquerdo): Validações mecânicas determinísticas e guardrails automatizados.
- **quadrant-4 Sensor Inferencial** (Inferior Direito): Revisões semânticas, agentes avaliadores e julgamento humano.

As coordenadas informadas no diagrama são qualitativas para suporte à priorização visual e estratégica, não métricas quantitativas rígidas.

## Diagrama

```mermaid
quadrantChart
    title Harness Calculadora COBOL — Quadrante Guias x Sensores
    x-axis Computacional --> Inferencial
    y-axis Sensor feedback --> Guia feedforward

    quadrant-1 Guia Inferencial
    quadrant-2 Guia Computacional
    quadrant-3 Sensor Computacional
    quadrant-4 Sensor Inferencial

    AGENTS.md (Fonte Unica): [0.85, 0.90]
    CLAUDE.md: [0.80, 0.82]
    copilot-instructions: [0.78, 0.76]
    Agentes Especializados: [0.88, 0.72]
    Skills de Dominio: [0.75, 0.65]
    Prompts Situacionais: [0.70, 0.60]
    harness.config.json: [0.22, 0.85]
    openspec config: [0.30, 0.70]
    PreToolUse Write Guard: [0.18, 0.35]
    PreToolUse Bash Guard: [0.20, 0.30]
    Fitness Functions COBOL: [0.12, 0.22]
    phase_cli.py: [0.25, 0.40]
    session-start.py: [0.32, 0.45]
    Agente Revisor COBOL: [0.80, 0.35]
    Revisao Humana: [0.90, 0.25]
```

## Rastreabilidade

| Ponto | Arquivo-fonte | Quadrante | Justificativa |
|---|---|---|---|
| AGENTS.md (Fonte Única) | [AGENTS.md](AGENTS.md) | Guia Inferencial | Fonte única da verdade contendo regras arquiteturais, convenções de colunas e quality gates. |
| CLAUDE.md | [CLAUDE.md](CLAUDE.md) | Guia Inferencial | Arquivo raiz fino para o Claude Code com hierarquia de instrução e regras operacionais. |
| copilot-instructions | [.github/copilot-instructions.md](.github/copilot-instructions.md) | Guia Inferencial | Diretrizes para o GitHub Copilot Agent Mode com templates e exemplos de código COBOL. |
| Agentes Especializados | [.github/agents/cobol-coder.agent.md](.github/agents/cobol-coder.agent.md) | Guia Inferencial | Personas de IA com escopos delimitados (Planner, Coder, Reviewer, Vibecoder, README Writer). |
| Skills de Domínio | [.github/skills/cobol-calculadora/SKILL.md](.github/skills/cobol-calculadora/SKILL.md) | Guia Inferencial | Conhecimento procedimental empacotado para COBOL, arquitetura, fitness functions e harness. |
| Prompts Situacionais | [.github/prompts/criar-programa.prompt.md](.github/prompts/criar-programa.prompt.md) | Guia Inferencial | Instruções prontas e parametrizadas para operações frequentes de implementação e teste. |
| harness.config.json | [harness.config.json](harness.config.json) | Guia Computacional | Contrato declarativo de caminhos, prefixos de escrita autorizados por fase e padrões bloqueados. |
| openspec config | [openspec/config.yaml](openspec/config.yaml) | Guia Computacional | Configuração de schema e regras de ciclo de vida de mudanças dirigidas por especificação. |
| PreToolUse Write Guard | [scripts/hooks/pre-tool-write-guard.py](scripts/hooks/pre-tool-write-guard.py) | Sensor Computacional | Bloqueia mecanicamente escrita fora da fase permitida, path traversal e alteração de segredos. |
| PreToolUse Bash Guard | [scripts/hooks/pre-tool-bash-guard.py](scripts/hooks/pre-tool-bash-guard.py) | Sensor Computacional | Intercepta comandos de shell perigosos (git push, rm -rf) e mutações git durante fase proposal. |
| Fitness Functions COBOL | [tests/fitness/test_cobol_architecture.py](tests/fitness/test_cobol_architecture.py) | Sensor Computacional | Testes determinísticos via unittest stdlib que validam 6 regras estruturais com fixtures negativas. |
| phase_cli.py | [scripts/harness/phase_cli.py](scripts/harness/phase_cli.py) | Sensor Computacional | CLI para gerenciamento atômico do estado de fase (proposal vs apply). |
| session-start.py | [scripts/hooks/session-start.py](scripts/hooks/session-start.py) | Sensor Computacional | Injeta verificação determinística de integridade de guias e contexto da change na inicialização. |
| Agente Revisor COBOL | [.github/agents/cobol-reviewer.agent.md](.github/agents/cobol-reviewer.agent.md) | Sensor Inferencial | Avaliação qualitativa de legibilidade, comentários e clareza do código COBOL produzido. |
| Revisão Humana | Processo de Pull Request | Sensor Inferencial | Avaliação semântica final e decisão de aprovação de merge realizada pelo desenvolvedor. |

## Lacunas priorizadas

| # | Lacuna | Risco | Próximo passo |
|---|---|---|---|
| 1 | Ausência de CI Remoto Automatizado | Alto | Criar workflow em [.github/workflows/ci.yml](.github/workflows) com execução de fitness functions e checagem de sintaxe cobc em tiers. |
| 2 | Ausência de Pre-commit Hook Git Nativo | Médio | Configurar hook local em [.git/hooks/pre-commit](.git/hooks) para disparar as fitness functions antes de qualquer commit via terminal. |
| 3 | Ausência de Configuração de Editor (.editorconfig) | Médio | Criar arquivo de configuração de editor fixando indentação por espaços e réguas visuais nas colunas 7, 11 e 72 para formato fixo COBOL. |
| 4 | Ausência de Linter de Shell e Scripts de Hook | Baixo | Adicionar verificação de conformidade sintática e de tipos com flake8/ruff para os scripts Python do harness. |

## Próximas ações recomendadas

1. **Implementar Pipeline de CI Mínimo**: Configurar GitHub Actions para rodar `python3 -m unittest discover -s tests/fitness` em cada push/PR.
2. **Ativar Pre-commit Local**: Instalar script disparador leve que bloqueia commits locais caso a regra de 72 colunas ou das 4 divisões seja violada.
3. **Padronizar Configuração do Editor**: Adicionar `.editorconfig` garantindo consistência de espaços e réguas visuais para todos os colaboradores humanos e agentes.
