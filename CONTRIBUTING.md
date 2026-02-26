# Como Contribuir com o cowboy 🤠

Obrigado por querer contribuir! Todo mundo é bem-vindo aqui, do cowboy experiente ao iniciante que está aprendendo Vibe Coding pela primeira vez.

---

## Tipos de contribuição

Há várias formas de contribuir com este projeto:

- 🐛 **Reportar bugs** — encontrou algo quebrado? Abra uma issue.
- 💡 **Sugerir features** — tem uma ideia para melhorar o tutorial? Compartilhe.
- 📝 **Melhorar documentação** — correção de erros, clareza, traduções.
- 🖥️ **Contribuir com código** — novos exemplos, novos exercícios.
- 🌍 **Traduzir conteúdo** — ajude a levar o Vibe Coding para mais pessoas.

---

## Antes de começar

1. Leia o [README.md](./README.md) para entender o projeto.
2. Leia o [AGENTS.md](./AGENTS.md) para entender as convenções de código COBOL.
3. Leia o [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) — seja gentil.

---

## Processo de contribuição

### 1. Fork o repositório

```bash
# Faça um fork pelo GitHub e depois clone o seu fork
git clone https://github.com/SEU-USUARIO/cowboy.git
cd cowboy
```

### 2. Crie uma branch

Use um nome descritivo para a sua branch:

```bash
# Para bugs
git checkout -b fix/descricao-do-bug

# Para novas features
git checkout -b feat/descricao-da-feature

# Para documentação
git checkout -b docs/descricao-da-mudanca
```

### 3. Faça suas alterações

Siga as convenções do projeto:

- Código COBOL deve seguir as regras do [AGENTS.md](./AGENTS.md)
- Documentação em português brasileiro
- Comentários em português

### 4. Compile e teste

Se você alterou o código COBOL:

```bash
# Verificar sintaxe
cobc -fsyntax-only src/CALCULADORA.cbl

# Compilar
cobc -x -o calculadora src/CALCULADORA.cbl

# Executar
./calculadora
```

### 5. Commit com mensagem clara

Siga o padrão [Conventional Commits](https://www.conventionalcommits.org/):

```bash
git add .
git commit -m "feat: adiciona operação de subtração"
git commit -m "fix: corrige overflow no cálculo de soma"
git commit -m "docs: melhora explicação do Agent Mode"
```

### 6. Abra um Pull Request

- Descreva claramente o que foi feito
- Referencie a issue relacionada (se houver): `Closes #42`
- Preencha o template de PR

---

## Convenções de código COBOL

```cobol
* ✅ BOM — código bem formatado
       01 WS-NUMERO-ENTRADA     PIC 9(5) VALUE ZEROS.

* ❌ RUIM — coluna errada ou nome pouco descritivo
       01 N1 PIC 9(5) VALUE ZEROS.
```

Regras principais:
- Nomes de variáveis com prefixo `WS-` para Working Storage
- Nomes descritivos, máximo 30 caracteres
- Comentários em português usando `*` na coluna 7
- Código na área B (colunas 12–72)
- Palavras reservadas em maiúsculas

---

## Relatando bugs

Abra uma issue usando o template **Bug Report** e inclua:

- Descrição clara do problema
- Passos para reproduzir
- Comportamento esperado vs. encontrado
- Versão do GnuCOBOL (`cobc --version`)
- Sistema operacional

---

## Sugerindo features

Abra uma issue usando o template **Feature Request** com:

- Descrição da ideia
- Qual problema ela resolve
- Como você imagina que funcionaria

---

## Dúvidas?

Abra uma issue com a label `question`. Sem formalidades, cowboy!

---

*Este guia é inspirado nas melhores práticas do [opensource.guide](https://opensource.guide/how-to-contribute/).*
