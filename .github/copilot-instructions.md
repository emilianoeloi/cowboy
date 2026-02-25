# Copilot Instructions

## Projeto: Calculadora COBOL

Este arquivo contém instruções específicas para o GitHub Copilot.
Siga estas diretrizes em todas as interações.

---

## Linguagem e Comunicação

- Responda sempre em português brasileiro
- Explique conceitos COBOL com clareza
- Use analogias modernas quando útil
- Seja paciente com a verbosidade do COBOL

---

## Estrutura de Código COBOL

### Template Básico

```cobol
      ******************************************************************
      * Nome do Programa: NOME-PROG
      * Descrição: Descrição breve
      * Autor: Nome
      * Data: DD/MM/AAAA
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. NOME-PROG.
       AUTHOR. NOME.
       DATE-WRITTEN. DD/MM/AAAA.
      
       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       
       DATA DIVISION.
       WORKING-STORAGE SECTION.
      * Declaração de variáveis aqui
       
       PROCEDURE DIVISION.
      * Lógica do programa aqui
           STOP RUN.
```

### Regras de Formatação

```
Colunas:
1-6    : Números de sequência (opcional)
7      : Indicador (* = comentário, - = continuação)
8-11   : Área A (DIVISION, SECTION, nomes de parágrafo)
12-72  : Área B (código, sentenças)
73-80  : Identificação (ignorado pelo compilador)
```

### Comentários

```cobol
      * Este é um comentário de linha inteira
      * Use asterisco na coluna 7
      
      * Seção: CALCULOS
      * Descrição: Realiza os cálculos matemáticos
```

---

## Declaração de Variáveis

### Working Storage Section

```cobol
       WORKING-STORAGE SECTION.
      
      * Variáveis para entrada
       01 WS-NUMERO-1          PIC 9(5) VALUE ZEROS.
       01 WS-NUMERO-2          PIC 9(5) VALUE ZEROS.
      
      * Variável para resultado
       01 WS-RESULTADO         PIC 9(6) VALUE ZEROS.
      
      * Variável para display formatado
       01 WS-RESULTADO-DISPLAY PIC Z(5)9.
```

### Picture Clauses Comuns

```cobol
PIC 9(5)      → 5 dígitos numéricos (00000-99999)
PIC S9(5)     → 5 dígitos com sinal
PIC 9(5)V99   → 5 inteiros + 2 decimais
PIC X(20)     → 20 caracteres alfanuméricos
PIC Z(5)9     → Suprime zeros à esquerda
PIC -(5)9     → Suprime zeros, mostra sinal negativo
```

---

## Operações Matemáticas

### Soma

```cobol
           ADD WS-NUMERO-1 TO WS-NUMERO-2 
               GIVING WS-RESULTADO.
      
      * Ou forma alternativa:
           COMPUTE WS-RESULTADO = WS-NUMERO-1 + WS-NUMERO-2.
```

### Outras Operações

```cobol
      * Subtração
           SUBTRACT WS-B FROM WS-A GIVING WS-RESULTADO.
      
      * Multiplicação
           MULTIPLY WS-A BY WS-B GIVING WS-RESULTADO.
      
      * Divisão
           DIVIDE WS-A BY WS-B GIVING WS-RESULTADO.
```

---

## Entrada e Saída

### Display (Saída)

```cobol
           DISPLAY "=================================".
           DISPLAY "   CALCULADORA COBOL".
           DISPLAY "=================================".
           DISPLAY "Resultado: " WS-RESULTADO-DISPLAY.
```

### Accept (Entrada)

```cobol
           DISPLAY "Digite o primeiro numero: ".
           ACCEPT WS-NUMERO-1.
           
           DISPLAY "Digite o segundo numero: ".
           ACCEPT WS-NUMERO-2.
```

---

## Fluxo do Agent Mode

Quando executar em Agent Mode:

1. **Leia primeiro** - Entenda o AGENTS.md e este arquivo
2. **Verifique ambiente** - Confirme que GnuCOBOL está instalado
3. **Crie o código** - Seguindo a estrutura COBOL
4. **Compile** - Use `cobc -x -o programa arquivo.cbl`
5. **Execute** - Use `./programa`
6. **Corrija** - Se houver erros, analise e corrija

---

## Erros Comuns em COBOL

### Erro: Falta ponto final
```
ERRO: Missing period
SOLUÇÃO: Adicione ponto no final da sentença
```

### Erro: Coluna errada
```
ERRO: Invalid indicator
SOLUÇÃO: Verifique se código está na área correta
```

### Erro: Picture inválida
```
ERRO: Invalid PICTURE string
SOLUÇÃO: Verifique a cláusula PIC
```

---

## Formato de Resposta

Quando completar uma tarefa, responda:

```
## ✅ Tarefa Concluída

### O que foi feito:
- Item 1
- Item 2

### Arquivos criados/modificados:
- src/CALCULADORA.cbl

### Compilação:
✅ cobc -x -o calculadora src/CALCULADORA.cbl

### Execução:
✅ ./calculadora
[saída do programa]

### Próximos passos sugeridos:
- Sugestão 1
```

---

## Lembre-se

COBOL é verboso por design.
Isso é uma característica, não um bug.
A legibilidade era o objetivo em 1959.
E ainda é valorizada hoje.

Vamos criar código COBOL limpo! 🖥️
