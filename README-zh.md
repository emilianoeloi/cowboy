<div align="center">

# 🤠 cowboy

### *"氛围编程就是在不理解代码的情况下编程"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![GnuCOBOL](https://img.shields.io/badge/COBOL-GnuCOBOL-blue)](https://gnucobol.sourceforge.io/)
[![GitHub Copilot](https://img.shields.io/badge/GitHub-Copilot%20Agent%20Mode-8A2BE2)](https://github.com/features/copilot)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

<br />

> 以最狂野的方式学习 **GitHub Copilot Agent Mode**：  
> 让 AI 写 COBOL，而你只需提问。

**[🇧🇷 Português](./README.md) | [🇺🇸 English](./README-en.md) | 🇨🇳 中文**

</div>

---

## 这是什么？🤔

**cowboy** 是一个关于 **GitHub Copilot Agent Mode** 的实践教程。

理念简单而激进：

> 你不需要了解 COBOL。  
> 你不需要理解代码。  
> 你只需要体验这个过程。

我们之所以使用 COBOL，正是出于这个原因。这是一门诞生于 1959 年、冗长而陌生的语言。如果 Agent Mode 能写出完美的 COBOL，它就能在你最喜欢的技术栈中干任何事情。

---

## 什么是"氛围编程"？🎸

**氛围编程（Vibe Coding）** 是世界对一种全新编程方式的称呼：

- 用自然语言描述你想要的
- AI 来编写代码
- 你测试、迭代、优化
- 代码可以运行——即使你不理解每一行

这不是"糟糕的代码"，这是**与 AI 的协作**。这是未来正在到来。

这个仓库是以诚实、实用的方式探索这一概念的沙盒。

---

## 你将学到什么 🎯

| 主题 | 描述 |
|------|------|
| 🤖 **Agent Mode** | 如何激活和使用 Copilot 的 Agent 模式 |
| 📋 **自定义指令** | 如何教 Copilot 了解你的项目 |
| 🧠 **Skills（技能）** | 如何为特定领域创建可复用的技能 |
| 👥 **Agents（代理）** | 如何创建专业代理（计划者、编程者、审查者） |
| 💬 **Prompts（提示词）** | 如何为重复任务创建可复用的提示词 |
| 🖥️ **COBOL** | COBOL 基础——附赠福利 |

---

## 快速演示 ⚡

```
========================================
       COBOL 计算器
       两数之和
========================================

请输入第一个数字 (0-99999): 
42
请输入第二个数字 (0-99999): 
58

========================================
计算结果
========================================
00042 + 00058 = 000100
```

> 这段代码由 GitHub Copilot Agent Mode 编写。  
> 本项目中没有人工手写过任何一行 COBOL。

---

## 前置条件 🛠️

- 安装了 [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot) 扩展的 [VS Code](https://code.visualstudio.com/)
- 用于编译程序的 [GnuCOBOL](https://gnucobol.sourceforge.io/)

### 安装 GnuCOBOL

```bash
# macOS
brew install gnucobol

# Ubuntu/Debian
sudo apt-get install gnucobol

# 验证安装
cobc --version
```

---

## 快速开始 🚀

```bash
# 1. 克隆仓库
git clone https://github.com/your-username/cowboy.git
cd cowboy

# 2. 在 VS Code 中打开
code .

# 3. 在 Copilot Chat 中激活 Agent Mode
# 点击 "Ask" 下拉菜单 → 选择 "Agent"

# 4. 编译 COBOL 程序
cobc -x -o calculadora src/CALCULADORA.cbl

# 5. 运行
./calculadora
```

---

## 项目结构 📁

```
cowboy/
├── README.md                           ← 葡萄牙语版本
├── README-en.md                        ← 英语版本
├── README-zh.md                        ← 本文件
├── AGENTS.md                           ← 全局代理指令
├── LICENSE                             ← MIT 许可证
├── CONTRIBUTING.md                     ← 贡献指南
├── SECURITY.md                         ← 安全政策
├── CODE_OF_CONDUCT.md                  ← 行为准则
├── src/
│   └── CALCULADORA.cbl                 ← COBOL 程序
├── docs/
│   ├── TUTORIAL.md                     ← 分步教程
│   └── LEITURA_VOZ_ALTA.md             ← 大声阅读版本
└── .github/
    ├── copilot-instructions.md         ← Copilot 指令
    ├── agents/
    │   ├── cobol-planner.agent.md          ← 计划代理
    │   ├── cobol-coder.agent.md            ← 编程代理
    │   ├── cobol-reviewer.agent.md         ← 审查代理
    │   └── readme-writer.agent.md          ← 文档代理
    ├── skills/
    │   ├── cobol-calculadora/
    │   │   └── SKILL.md                    ← COBOL 技能
    │   └── readme-manutencao/
    │       └── SKILL.md                    ← README 维护技能
    ├── prompts/
    │   ├── criar-programa.prompt.md        ← 提示词：创建程序
    │   ├── implementar-soma.prompt.md      ← 提示词：实现加法
    │   ├── implementar-subtracao.prompt.md ← 提示词：实现减法
    │   ├── testar-programa.prompt.md       ← 提示词：测试程序
    │   ├── atualizar-readme.prompt.md      ← 提示词：更新 README
    │   └── manutencao-repositorio.prompt.md ← 提示词：仓库维护
    ├── ISSUE_TEMPLATE/                 ← Issue 模板
    └── PULL_REQUEST_TEMPLATE/          ← PR 模板
```

---

## 如何使用教程 📖

### 第一步 — 准备环境

克隆仓库并在安装了 Copilot 的 VS Code 中打开。

### 第二步 — 激活 Agent Mode

在 Copilot Chat 中，将模式从 "Ask" 切换为 "Agent"。  
Copilot 会自动读取 `AGENTS.md` 和 `.github/` 中的指令。

### 第三步 — 按顺序执行提示词

```
.github/prompts/criar-programa.prompt.md
.github/prompts/implementar-soma.prompt.md
.github/prompts/implementar-subtracao.prompt.md
.github/prompts/testar-programa.prompt.md
.github/prompts/atualizar-readme.prompt.md
.github/prompts/manutencao-repositorio.prompt.md
```

### 第四步 — 观察并学习

看代理创建、编译并运行 COBOL 代码。  
一门 1959 年的语言，运行在 2026 年的 AI 上。

---

## 如何贡献 🤝

欢迎贡献！请查阅 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解详情。

有改进教程的想法？[提交一个 Issue](../../issues/new/choose)。

---

## 行为准则 📜

本项目遵循 [Contributor Covenant](./CODE_OF_CONDUCT.md)。  
友善待人，包容他人，共同振动。

---

## 许可证 📄

MIT © [cowboy contributors](./LICENSE)

---

<div align="center">

**由 🤠 和 GitHub Copilot Agent Mode 共同制作**

*本项目中没有人工手写过任何一行 COBOL。*

</div>
