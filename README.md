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
    │   ├── cobol-planner.agent.md          ← Agente planejador
    │   ├── cobol-coder.agent.md            ← Agente programador
    │   ├── cobol-reviewer.agent.md         ← Agente revisor
    │   └── readme-writer.agent.md          ← Agente de documentação
    ├── skills/
    │   ├── cobol-calculadora/
    │   │   └── SKILL.md                    ← Skill de COBOL
    │   └── readme-manutencao/
    │       └── SKILL.md                    ← Skill de READMEs
    ├── prompts/
    │   ├── criar-programa.prompt.md        ← Prompt: criar programa
    │   ├── implementar-soma.prompt.md      ← Prompt: implementar soma
    │   ├── implementar-subtracao.prompt.md ← Prompt: implementar subtração
    │   ├── implementar-divisao.prompt.md   ← Prompt: implementar divisão
    │   ├── implementar-log.prompt.md       ← Prompt: implementar logaritmo
    │   ├── testar-programa.prompt.md       ← Prompt: testar programa
    │   ├── atualizar-readme.prompt.md      ← Prompt: atualizar READMEs
    │   └── manutencao-repositorio.prompt.md ← Prompt: manutenção do repositório
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.yml
    │   └── feature_request.yml
    └── PULL_REQUEST_TEMPLATE/
        └── pull_request_template.md        ← Template de PR
```

---

## Como usar o tutorial 📖

Este tutorial pode ser feito de **3 formas**, cada uma explorando um nível distinto do GitHub Copilot. Escolha a que mais combina com você — ou faça as três.

---

### 💬 Modo 1 — Chat

> Converse com o Copilot e peça para ele criar o código.

No Copilot Chat, use o modo **Ask** e descreva o que quer implementar.  
O Copilot vai sugerir o código. Você revisa, aceita e aprende.

---

### 📋 Modo 2 — Prompts

> Use um prompt específico para cada operação já criada no projeto.

Execute os prompts na ordem, um por um:

```
.github/prompts/criar-programa.prompt.md
.github/prompts/implementar-soma.prompt.md
.github/prompts/implementar-subtracao.prompt.md
.github/prompts/implementar-divisao.prompt.md
.github/prompts/implementar-log.prompt.md
.github/prompts/testar-programa.prompt.md
.github/prompts/atualizar-readme.prompt.md
```

Cada prompt é um roteiro pronto. Você executa, o Copilot implementa.

---

### 🤖 Modo 3 — Agent

> Um agente especializado orquestra todo o fluxo por você.

No Copilot Chat, mude de "Ask" para **Agent** e invoque o `COBOL Vibecoder`.  
Ele vai ler o `AGENTS.md`, planejar, codar, revisar e atualizar a documentação — sozinho.

```
@COBOL Vibecoder implemente a operação de multiplicação na calculadora
```

Veja um agente criar, compilar e executar código COBOL.  
Uma linguagem de 1959. Funcionando com IA de 2026.

---

### 🌱 Bônus — Roots

> Só uma mente de programador e um arquivo de texto. Sem IA, sem internet.

Leia o código COBOL manualmente. Entenda a estrutura. Escreva com as próprias mãos.  
Para quem quer sentir o peso de 1959.

Útil também quando o [Downdetector](https://downdetector.com.br/) confirmar que a IA caiu. 😄

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

*"A ciência reúne conhecimento mais rápido do que a sociedade reúne sabedoria."* — Isaac Asimov

</div>
