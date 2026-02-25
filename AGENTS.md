# AGENTS.md - Instruções Globais para Agentes

## Sobre Este Projeto

Este é o projeto Calculadora COBOL.
Uma calculadora simples de soma.
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
src/
└── CALCULADORA.cbl    ← Programa principal

test/
└── TEST-CALC.cbl      ← Programa de teste (opcional)
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
# Compilar o programa
cobc -x -o calculadora src/CALCULADORA.cbl

# Executar o programa
./calculadora

# Compilar com debug
cobc -x -debug -o calculadora src/CALCULADORA.cbl

# Verificar sintaxe sem compilar
cobc -fsyntax-only src/CALCULADORA.cbl
```

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

## Contexto para o Agente

Este projeto é didático.
O objetivo é aprender Agent Mode.
Usando COBOL como exemplo.

Mantenha o código simples.
Explique cada parte.
O aprendizado é mais importante que a eficiência.
