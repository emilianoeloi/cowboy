---
name: Criar Programa COBOL
description: Cria a estrutura inicial do programa COBOL para a calculadora
mode: agent
---

# 🖥️ Missão: Criar Estrutura do Programa COBOL

## Contexto

Você está criando o projeto Calculadora COBOL.
Uma calculadora simples de soma.
Em COBOL, a linguagem que roda o mundo financeiro.

## Sua Tarefa

Crie a estrutura inicial do projeto com:

### 1. Verificar Ambiente

Primeiro, verifique se o GnuCOBOL está instalado:
```bash
cobc --version
```

Se não estiver instalado, informe o usuário como instalar:
- macOS: `brew install gnucobol`
- Ubuntu: `sudo apt-get install gnucobol`

### 2. Criar Estrutura de Pastas

```bash
mkdir -p src
```

### 3. Criar Arquivo COBOL Inicial

Crie o arquivo `src/CALCULADORA.cbl` com:
- As 4 divisões obrigatórias
- Estrutura básica mas ainda sem lógica
- Comentários explicativos

O arquivo deve conter:
- IDENTIFICATION DIVISION com PROGRAM-ID
- ENVIRONMENT DIVISION básica
- DATA DIVISION com WORKING-STORAGE vazia
- PROCEDURE DIVISION com apenas STOP RUN

## Template Inicial

```cobol
      ******************************************************************
      * Programa: CALCULADORA
      * Descrição: Calculadora de soma em COBOL
      * Autor: Copilot Agent
      * Data: 2026
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCULADORA.
       AUTHOR. COPILOT-AGENT.
      
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. PC.
       OBJECT-COMPUTER. PC.
      
       DATA DIVISION.
       WORKING-STORAGE SECTION.
      * Variáveis serão adicionadas no próximo passo
      
       PROCEDURE DIVISION.
       INICIO.
           DISPLAY "Calculadora COBOL - Estrutura criada!".
           STOP RUN.
```

## Passos para Executar

1. Verifique se GnuCOBOL está instalado
2. Crie a pasta `src`
3. Crie o arquivo `src/CALCULADORA.cbl`
4. Compile com `cobc -x -o calculadora src/CALCULADORA.cbl`
5. Execute com `./calculadora`
6. Confirme que exibe a mensagem

## Critérios de Sucesso

- [ ] GnuCOBOL instalado e funcionando
- [ ] Pasta `src` criada
- [ ] Arquivo `CALCULADORA.cbl` existe
- [ ] Programa compila sem erros
- [ ] Programa executa e mostra mensagem

## Importante

- Leia o arquivo `AGENTS.md` para convenções
- Leia o skill em `.github/skills/cobol-calculadora/SKILL.md`
- Respeite as colunas do COBOL!

## Após Completar

Informe que a estrutura foi criada e sugira usar o próximo prompt:
`implementar-soma.prompt.md`

Vamos criar código COBOL! 🖥️
