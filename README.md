# Calculadora COBOL 🖥️

## Tutorial Completo de GitHub Copilot Agent Mode

Este projeto ensina Agent Mode do zero.
Você vai criar uma calculadora de soma.
Em COBOL.
A linguagem que roda o mundo financeiro.

---

## Por Que COBOL?

COBOL é histórico.
Criado em 1959.
Ainda roda 95% das transações ATM.
Ainda processa 80% das transações financeiras.

Aprender COBOL é entender as raízes.
E o Agent Mode funciona com qualquer linguagem.
Até as mais antigas.

---

## O Que Você Vai Aprender

Este tutorial cobre tudo.
Skills.
Agents.
Prompts.
Custom Instructions.

Tudo aplicado ao COBOL.
Uma linguagem que você talvez nunca usou.
Mas que o Copilot conhece bem.

---

## Estrutura do Projeto

```
calculadora-cobol/
├── README.md                           ← Você está aqui
├── AGENTS.md                           ← Instruções globais para o agente
├── TUTORIAL.md                         ← Tutorial passo a passo
├── LEITURA_VOZ_ALTA.md                 ← Otimizado para leitura em voz alta
├── .github/
│   ├── copilot-instructions.md         ← Instruções do Copilot
│   ├── agents/
│   │   ├── cobol-planner.agent.md      ← Agente que planeja
│   │   ├── cobol-coder.agent.md        ← Agente que implementa
│   │   └── cobol-reviewer.agent.md     ← Agente que revisa
│   ├── skills/
│   │   └── cobol-calculadora/
│   │       └── SKILL.md                ← Skill de COBOL
│   └── prompts/
│       ├── criar-programa.prompt.md    ← Prompt para criar programa
│       ├── implementar-soma.prompt.md  ← Prompt para implementar soma
│       └── testar-programa.prompt.md   ← Prompt para testar
└── .vscode/
    └── settings.json                   ← Configurações do VS Code
```

---

## Pré-requisitos

Para compilar COBOL, você precisa de um compilador.
O mais comum é o GnuCOBOL.

### Instalação no macOS
```bash
brew install gnucobol
```

### Instalação no Ubuntu/Debian
```bash
sudo apt-get install gnucobol
```

### Verificar instalação
```bash
cobc --version
```

---

## Como Usar Este Tutorial

### Passo 1: Abra no VS Code

Abra esta pasta no VS Code.
Certifique-se de ter o GitHub Copilot instalado.

### Passo 2: Mude para Agent Mode

Abra o Copilot Chat.
Clique no dropdown "Ask".
Mude para "Agent".

### Passo 3: Use os Prompts

Na pasta .github/prompts você encontra prompts prontos.
Execute na ordem:
1. criar-programa.prompt.md
2. implementar-soma.prompt.md
3. testar-programa.prompt.md

### Passo 4: Observe e Aprenda

Observe o agente criar código COBOL.
Uma linguagem de 1959.
Funcionando com IA de 2026.
Incrível, não é?

---

## Resultado Esperado

Ao final você terá:

- Um programa COBOL funcional
- Que soma dois números
- Compilado com GnuCOBOL
- E muito conhecimento sobre Agent Mode!

Vamos começar! 🖥️
