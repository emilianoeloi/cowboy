# AGENTS.md - Instruções Globais para Agentes

## Sobre Este Projeto

Este é o projeto Calculadora COBOL.
Uma calculadora com soma, subtração, multiplicação e divisão.
Escrita em COBOL.
Para aprender Agent Mode.

---

## Sobre COBOL

COBOL significa Common Business-Oriented Language.
Foi criada em 1959.
É uma das linguagens mais antigas ainda em uso.
Roda sistemas bancários no mundo todo.

### Características do COBOL
- Linguagem verbosa e legível
- Estrutura em divisões (DIVISIONS)
- Colunas fixas (área A e área B)
- Nomes descritivos em inglês

---

## Estrutura de um Programa COBOL

Todo programa COBOL tem 4 divisões:

```cobol
IDENTIFICATION DIVISION.
    (identifica o programa)

ENVIRONMENT DIVISION.
    (configurações de ambiente)

DATA DIVISION.
    (declaração de variáveis)

PROCEDURE DIVISION.
    (lógica do programa)
```

---

## Convenções de Código

### Formatação
- Colunas 1-6: números de linha (opcional)
- Coluna 7: indicador (* para comentário)
- Colunas 8-11: Área A (divisões, seções, parágrafos)
- Colunas 12-72: Área B (código)
- Colunas 73-80: ignoradas

### Estilo
- Use MAIÚSCULAS para palavras reservadas
- Nomes descritivos com hífens (WS-NUMERO-1)
- Comentários em português
- Um ponto final em cada sentença

### Nomenclatura de Variáveis
- Prefixo WS- para Working Storage
- Nomes descritivos
- Máximo 30 caracteres
- Exemplo: WS-NUMERO-PRIMEIRO

---

## Estrutura de Pastas

```
cowboy/
├── AGENTS.md                         ← Este arquivo
├── src/
│   └── CALCULADORA.cbl                     ← Programa principal
├── docs/
│   ├── TUTORIAL.md                         ← Tutorial passo a passo
│   └── LEITURA_VOZ_ALTA.md                 ← Versão para leitura em voz alta
└── .github/
    ├── copilot-instructions.md             ← Instruções do Copilot
    ├── agents/
    │   ├── cobol-planner.agent.md          ← Agente planejador
    │   ├── cobol-coder.agent.md            ← Agente programador
    │   ├── cobol-reviewer.agent.md         ← Agente revisor
    │   └── readme-writer.agent.md          ← Agente de documentação
    ├── skills/
    │   ├── cobol-calculadora/SKILL.md      ← Skill de COBOL
    │   ├── readme-manutencao/SKILL.md      ← Skill de READMEs
    │   └── vibe-coding-fundamentals/SKILL.md ← Skill de Vibe Coding
    └── prompts/
        ├── criar-programa.prompt.md
        ├── implementar-soma.prompt.md
        ├── implementar-subtracao.prompt.md
        ├── implementar-divisao.prompt.md
        ├── testar-programa.prompt.md
        ├── atualizar-readme.prompt.md
        └── manutencao-repositorio.prompt.md
```

---

## Regras para Agentes

### Sempre Faça
- Use a estrutura padrão de 4 divisões
- Declare todas as variáveis na DATA DIVISION
- Comente o código em português
- Termine sentenças com ponto final
- Use STOP RUN para encerrar

### Nunca Faça
- Não use colunas além da 72
- Não esqueça os pontos finais
- Não misture áreas A e B
- Não use caracteres especiais em nomes

---

## Comandos Disponíveis

```bash
# Instalar o harness (hooks, skills, gate de fase) via APM
make apm-install

# Executar fitness functions de arquitetura (sensores estruturais)
make fitness
# ou: python3 -m unittest discover -s tests/fitness

# Executar testes unitários funcionais da calculadora
make test-unit
# ou: python3 -m unittest discover -s tests/unit

# Executar bateria completa de testes (fitness e unitários)
make test

# Compilar o programa
make build
# ou: cobc -x -o calculadora src/CALCULADORA.cbl

# Executar o programa
make run
# ou: ./calculadora

# Executar teste automatizado (smoke test)
make smoke-test

# Compilar com debug
cobc -x -debug -o calculadora src/CALCULADORA.cbl

# Verificar sintaxe sem compilar
make syntax
# ou: cobc -fsyntax-only src/CALCULADORA.cbl
```

---

## Harness e fase da change

Hooks, gate de fase (proposal/apply) e skills de SDLC vêm do pacote APM
`emilianoeloi/apm` (ver `apm.yml`). Rode `make apm-install` após clonar.
---

## Tipos de Dados Comuns

```cobol
* Número inteiro de 5 dígitos
01 WS-NUMERO        PIC 9(5).

* Número com sinal
01 WS-VALOR         PIC S9(5).

* Número decimal (2 casas)
01 WS-PRECO         PIC 9(5)V99.

* Texto de 20 caracteres
01 WS-NOME          PIC X(20).

* Número editado para display
01 WS-DISPLAY       PIC Z(4)9.
```

---

## Metodologia SDLC (OpenSpec + OpenSPDD)

O ciclo de vida de desenvolvimento (SDLC) segue estritamente o pipeline de 5 fases:

```
[0] explorar ──> [1] propose ──> [1] analysis ──> [1] reasons-canvas ──> [2] generate
(cobol-vibecoder) (cobol-planner) (cobol-planner)   (cobol-planner)      (cobol-coder)
```

1. **[0] Explorar (`cobol-vibecoder`)**: Exploração de contexto, definição da change em kebab-case e ativação da fase `proposal`.
2. **[1] Propose (`cobol-planner` / `opsx-propose`)**: Criação da proposta formal em `openspec/changes/<change>/` e validação com `openspec validate <change> --strict`.
3. **[1] Analysis (`cobol-planner` / `spdd-analysis`)**: Análise técnica e de risco das 4 divisões COBOL em `spdd/analysis/`.
4. **[1] Reasons-Canvas (`cobol-planner` / `spdd-reasons-canvas`)**: Estruturação do contrato executável de 7 dimensões em `spdd/prompt/`.
5. **[2] Generate (`cobol-coder` / `spdd-generate`)**: Promoção da fase para `apply`, implementação estrita em `src/CALCULADORA.cbl`, compilação, teste funcional e validação dos 13 testes de arquitetura (`make fitness`).

---

## Agentes Disponíveis

| Agente | Arquivo | Uso |
|--------|---------|-----|
| COBOL Vibecoder | `.github/agents/cobol-vibecoder.agent.md` | Orquestrador: [0] Explorar & Conectar Planner → Coder → Reviewer → README |
| COBOL Planner | `.github/agents/cobol-planner.agent.md` | Planejador SDLC: [1] Propose (opsx), Analysis (spdd) e REASONS Canvas (spdd) |
| COBOL Coder | `.github/agents/cobol-coder.agent.md` | Implementador: [2] Generate (spdd-generate), compilação e fitness gates |
| COBOL Reviewer | `.github/agents/cobol-reviewer.agent.md` | Revisor: [3] Revisar qualidade do código COBOL e conformidade do SDLC |
| README Writer | `.github/agents/readme-writer.agent.md` | Documentador: [4] Sincronizar READMEs em PT-BR, EN e ZH |

---

## Skills Disponíveis

| Skill | Arquivo | Uso |
|-------|---------|-----|
| cobol-calculadora | `.github/skills/cobol-calculadora/SKILL.md` | Criar calculadoras e operações em COBOL |
| openspec-workflow | `.github/skills/openspec-workflow/SKILL.md` | Governança SDLC com OpenSpec (opsx-propose, tasks, validação) |
| openspdd-workflow | `.github/skills/openspdd-workflow/SKILL.md` | Metodologia OpenSPDD e REASONS Canvas (analysis, canvas, generate) |
| readme-manutencao | `.github/skills/readme-manutencao/SKILL.md` | Manter READMEs sincronizados em 3 idiomas |
| vibe-coding-fundamentals | `.github/skills/vibe-coding-fundamentals/SKILL.md` | Entender Vibe Coding, Agent Mode e customizações Copilot |
| architecture-fitness-functions | `.github/skills/architecture-fitness-functions/SKILL.md` | Fitness functions de arquitetura como sensores |

---

## Prompts Disponíveis

| Prompt | Arquivo | Uso |
|--------|---------|-----|
| Criar Programa | `.github/prompts/criar-programa.prompt.md` | Criar o programa COBOL do zero |
| Implementar Soma | `.github/prompts/implementar-soma.prompt.md` | Adicionar operação de soma |
| Implementar Subtração | `.github/prompts/implementar-subtracao.prompt.md` | Adicionar operação de subtração |
| Testar Programa | `.github/prompts/testar-programa.prompt.md` | Compilar e testar o programa |
| Atualizar README | `.github/prompts/atualizar-readme.prompt.md` | Sincronizar os 3 READMEs |
| Implementar Divisão | `.github/prompts/implementar-divisao.prompt.md` | Adicionar operação de divisão |
| Implementar Logaritmo | `.github/prompts/implementar-log.prompt.md` | Adicionar operação de logaritmo (base 10) |
| Manutenção do Repositório | `.github/prompts/manutencao-repositorio.prompt.md` | Manutenção geral do projeto |

---

## Contexto para o Agente

Este projeto é didático.
O objetivo é aprender Agent Mode.
Usando COBOL como exemplo.

Mantenha o código simples.
Explique cada parte.
O aprendizado é mais importante que a eficiência.
