<div align="center">

# 🤠 cowboy

### *"Vibe Coding é programar sem entender o código"*

🇧🇷 Português | [🇺🇸 English](./README-en.md) | [🇨🇳 中文](./README-zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![GnuCOBOL](https://img.shields.io/badge/COBOL-GnuCOBOL-blue)](https://gnucobol.sourceforge.io/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot%20Agent%20Mode-8A2BE2)](https://github.com/features/copilot)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

<br />

> Aprenda **GitHub Copilot Agent Mode** do jeito mais selvagem:  
> deixando a IA escrever COBOL enquanto você só faz perguntas.

</div>

---

## O que é isso? 🤔

**cowboy** é um tutorial hands-on de **GitHub Copilot Agent Mode**.

A ideia é simples e radical:

> Você não precisa saber COBOL.  
> Você não precisa entender o código.  
> Você só precisa viver a experiência.

Usamos COBOL exatamente por isso. Uma linguagem de 1959, verbosa e estranha. Se o Agent Mode consegue escrever COBOL perfeito, ele consegue fazer qualquer coisa na sua stack favorita.

---

## Por que "Vibe Coding"? 🎸

**Vibe Coding** é o nome que o mundo deu para uma nova forma de programar:

- Você descreve o que quer em linguagem natural
- A IA escreve o código
- Você testa, itera e refina
- O código funciona — mesmo que você não entenda cada linha

Não é "código ruim". É **colaboração com IA**. É o futuro chegando agora.

Este repositório é uma sandbox para explorar esse conceito de forma honesta e prática.

---

## O que você vai aprender 🎯

| Tópico | Descrição |
|--------|-----------|
| 🤖 **Agent Mode** | Como ativar e usar o modo agente do Copilot |
| 📋 **Custom Instructions** | Como ensinar o Copilot sobre o seu projeto |
| 🧠 **Skills** | Como criar skills reutilizáveis para domínios específicos |
| 👥 **Agents** | Como criar agentes especializados (Planner, Coder, Reviewer) |
| 💬 **Prompts** | Como criar prompts reutilizáveis para tarefas recorrentes |
| 🖥️ **COBOL** | O básico de COBOL — de brinde |

---

## Demo rápida ⚡

```
========================================
       CALCULADORA COBOL
       Soma de Dois Numeros
========================================

Digite o primeiro numero (0-99999): 
42
Digite o segundo numero (0-99999): 
58

========================================
RESULTADO DA SOMA
========================================
00042 + 00058 = 000100
```

> Esse código foi escrito pelo GitHub Copilot Agent Mode.  
> Nenhum humano digitou COBOL neste projeto.

---

## Pré-requisitos 🛠️

- [VS Code](https://code.visualstudio.com/) com a extensão [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [GnuCOBOL](https://gnucobol.sourceforge.io/) para compilar o programa

### Instalar GnuCOBOL

```bash
# macOS
brew install gnucobol

# Ubuntu/Debian
sudo apt-get install gnucobol

# Verificar instalação
cobc --version
```

---

## Instalação e uso 🚀

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/cowboy.git
cd cowboy

# 2. Abra no VS Code
code .

# 3. Ative o Agent Mode no Copilot Chat
# Clique no dropdown "Ask" → selecione "Agent"

# 4. Compile o programa COBOL
cobc -x -o calculadora src/CALCULADORA.cbl

# 5. Execute
./calculadora
```

---

## Estrutura do projeto 📁

```
cowboy/
├── README.md                           ← Você está aqui
├── AGENTS.md                           ← Instruções globais para agentes
├── LICENSE                             ← Licença MIT
├── CONTRIBUTING.md                     ← Como contribuir
├── SECURITY.md                         ← Política de segurança
├── CODE_OF_CONDUCT.md                  ← Código de conduta
├── src/
│   └── CALCULADORA.cbl                 ← Programa COBOL
├── docs/
│   ├── TUTORIAL.md                     ← Tutorial passo a passo
│   └── LEITURA_VOZ_ALTA.md             ← Versão para leitura em voz alta
└── .github/
    ├── copilot-instructions.md         ← Instruções do Copilot
    ├── agents/
    │   ├── cobol-planner.agent.md      ← Agente planejador
    │   ├── cobol-coder.agent.md        ← Agente programador
    │   └── cobol-reviewer.agent.md     ← Agente revisor
    ├── skills/
    │   └── cobol-calculadora/
    │       └── SKILL.md                ← Skill de COBOL
    ├── prompts/
    │   ├── criar-programa.prompt.md    ← Prompt: criar programa
    │   ├── implementar-soma.prompt.md  ← Prompt: implementar soma
    │   └── testar-programa.prompt.md   ← Prompt: testar
    └── ISSUE_TEMPLATE/
        ├── bug_report.yml
        └── feature_request.yml
```

---

## Como usar o tutorial 📖

### Passo 1 — Prepare o ambiente

Clone o repositório e abra no VS Code com o Copilot instalado.

### Passo 2 — Ative o Agent Mode

No Copilot Chat, mude de "Ask" para "Agent".  
O Copilot vai ler automaticamente o `AGENTS.md` e as instruções em `.github/`.

### Passo 3 — Execute os prompts na ordem

```
.github/prompts/criar-programa.prompt.md
.github/prompts/implementar-soma.prompt.md
.github/prompts/testar-programa.prompt.md
```

### Passo 4 — Observe e aprenda

Veja o agente criar, compilar e executar código COBOL.  
Uma linguagem de 1959. Funcionando com IA de 2026.

---

## Contribuindo 🤝

Contribuições são bem-vindas! Consulte o [CONTRIBUTING.md](./CONTRIBUTING.md) para saber como.

Tem uma ideia para melhorar o tutorial? [Abra uma issue](../../issues/new/choose).

---

## Código de Conduta 📜

Este projeto adota o [Contributor Covenant](./CODE_OF_CONDUCT.md).  
Seja gentil. Seja inclusivo. Vibe together.

---

## Licença 📄

MIT © [cowboy contributors](./LICENSE)

---

<div align="center">

**Feito com 🤠 e GitHub Copilot Agent Mode**

*Nenhuma linha de COBOL foi digitada manualmente neste projeto.*

</div>
