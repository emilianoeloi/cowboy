<div align="center">

# 🤠 cowboy

### *"Vibe Coding is programming without understanding the code"*

[🇧🇷 Português](./README.md) | 🇺🇸 English | [🇨🇳 中文](./README-zh.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![GnuCOBOL](https://img.shields.io/badge/COBOL-GnuCOBOL-blue)](https://gnucobol.sourceforge.io/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot%20Agent%20Mode-8A2BE2)](https://github.com/features/copilot)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

<br />

> Learn **GitHub Copilot Agent Mode** the wildest way:  
> letting AI write COBOL while you just ask questions.

</div>

---

## What is this? 🤔

**cowboy** is a hands-on tutorial for **GitHub Copilot Agent Mode**.

The idea is simple and radical:

> You don't need to know COBOL.  
> You don't need to understand the code.  
> You just need to live the experience.

We use COBOL exactly because of that. A language from 1959, verbose and strange. If Agent Mode can write perfect COBOL, it can do anything in your favorite stack.

---

## Why "Vibe Coding"? 🎸

**Vibe Coding** is the name the world gave to a new way of programming:

- You describe what you want in natural language
- The AI writes the code
- You test, iterate, and refine
- The code works — even if you don't understand every line

It's not "bad code". It's **AI collaboration**. It's the future arriving now.

This repository is a sandbox to explore this concept honestly and practically.

---

## What you will learn 🎯

| Topic | Description |
|-------|-------------|
| 🤖 **Agent Mode** | How to activate and use Copilot's agent mode |
| 📋 **Custom Instructions** | How to teach Copilot about your project |
| 🧠 **Skills** | How to create reusable skills for specific domains |
| 👥 **Agents** | How to create specialized agents (Planner, Coder, Reviewer) |
| 💬 **Prompts** | How to create reusable prompts for recurring tasks |
| 🖥️ **COBOL** | The basics of COBOL — as a bonus |

---

## Quick demo ⚡

```
========================================
       CALCULADORA COBOL
   Soma, Subtracao, Multiplicacao, Divisao e Log
========================================

Escolha a operacao:
  1 - Soma
  2 - Subtracao
  3 - Multiplicacao
  4 - Divisao
  5 - Logaritmo (base 10)

Digite sua opcao (1, 2, 3, 4 ou 5): 
5

Digite o numero (deve ser maior que zero): 
1000

========================================
RESULTADO DO LOGARITMO
========================================
LOG10(01000) =     3.000000
========================================

Programa encerrado com sucesso!
```

> This code was written by GitHub Copilot Agent Mode.  
> No human typed COBOL in this project.

---

## Prerequisites 🛠️

- [VS Code](https://code.visualstudio.com/) with the [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) extension
- [GnuCOBOL](https://gnucobol.sourceforge.io/) to compile the program

### Install GnuCOBOL

```bash
# macOS
brew install gnucobol

# Ubuntu/Debian
sudo apt-get install gnucobol

# Verify installation
cobc --version
```

---

## Installation and usage 🚀

```bash
# 1. Clone the repository
git clone https://github.com/your-username/cowboy.git
cd cowboy

# 2. Open in VS Code
code .

# 3. Enable Agent Mode in Copilot Chat
# Click the "Ask" dropdown → select "Agent"

# 4. Compile the COBOL program
cobc -x -o calculadora src/CALCULADORA.cbl

# 5. Run it
./calculadora
```

---

## Project structure 📁

```
cowboy/
├── README.md                           ← Portuguese README
├── README-en.md                        ← You are here
├── AGENTS.md                           ← Global agent instructions
├── LICENSE                             ← MIT License
├── CONTRIBUTING.md                     ← How to contribute
├── SECURITY.md                         ← Security policy
├── CODE_OF_CONDUCT.md                  ← Code of conduct
├── src/
│   └── CALCULADORA.cbl                 ← COBOL program
├── docs/
│   ├── TUTORIAL.md                     ← Step-by-step tutorial (PT)
│   └── LEITURA_VOZ_ALTA.md             ← Read-aloud version (PT)
└── .github/
    ├── copilot-instructions.md         ← Copilot instructions
    ├── agents/
    │   ├── cobol-planner.agent.md          ← Planner agent
    │   ├── cobol-coder.agent.md            ← Coder agent
    │   ├── cobol-reviewer.agent.md         ← Reviewer agent
    │   └── readme-writer.agent.md          ← Documentation agent
    ├── skills/
    │   ├── cobol-calculadora/
    │   │   └── SKILL.md                    ← COBOL skill
    │   └── readme-manutencao/
    │       └── SKILL.md                    ← README maintenance skill
    ├── prompts/
    │   ├── criar-programa.prompt.md        ← Prompt: create program
    │   ├── implementar-soma.prompt.md      ← Prompt: implement sum
    │   ├── implementar-subtracao.prompt.md ← Prompt: implement subtraction
    │   ├── implementar-divisao.prompt.md   ← Prompt: implement division
    │   ├── implementar-log.prompt.md       ← Prompt: implement logarithm
    │   ├── testar-programa.prompt.md       ← Prompt: test program
    │   ├── atualizar-readme.prompt.md      ← Prompt: update READMEs
    │   └── manutencao-repositorio.prompt.md ← Prompt: repository maintenance
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.yml
    │   └── feature_request.yml
    └── PULL_REQUEST_TEMPLATE/
        └── pull_request_template.md        ← PR template
```

---

## How to use the tutorial 📖

### Step 1 — Set up your environment

Clone the repository and open it in VS Code with Copilot installed.

### Step 2 — Enable Agent Mode

In Copilot Chat, switch from "Ask" to "Agent".  
Copilot will automatically read `AGENTS.md` and the instructions in `.github/`.

### Step 3 — Run the prompts in order

```
.github/prompts/criar-programa.prompt.md
.github/prompts/implementar-soma.prompt.md
.github/prompts/implementar-subtracao.prompt.md
.github/prompts/implementar-divisao.prompt.md
.github/prompts/implementar-log.prompt.md
.github/prompts/testar-programa.prompt.md
.github/prompts/atualizar-readme.prompt.md
```

### Step 4 — Watch and learn

See the agent create, compile and run COBOL code.  
A language from 1959. Running with AI from 2026.

---

## Contributing 🤝

Contributions are welcome! Check [CONTRIBUTING.md](./CONTRIBUTING.md) to get started.

Have an idea to improve the tutorial? [Open an issue](../../issues/new/choose).

---

## Code of Conduct 📜

This project follows the [Contributor Covenant](./CODE_OF_CONDUCT.md).  
Be kind. Be inclusive. Vibe together.

---

## License 📄

MIT © [cowboy contributors](./LICENSE)

---

<div align="center">

**Made with 🤠 and GitHub Copilot Agent Mode**

*Not a single line of COBOL was typed manually in this project.*

*"Science gathers knowledge faster than society gathers wisdom."* — Isaac Asimov

</div>
