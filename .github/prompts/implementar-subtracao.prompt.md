---
name: Implementar Subtração COBOL
description: Adiciona a operação de subtração na Calculadora COBOL com menu de seleção de operação
mode: agent
---

# 🖥️ Missão: Implementar Função de Subtração

## Contexto

A calculadora já implementa a soma.
Agora você vai adicionar a subtração.
O usuário escolherá a operação por um menu.

## Sua Tarefa

Modifique o arquivo `src/CALCULADORA.cbl` para:

### 1. Adicionar Variáveis na WORKING-STORAGE

```cobol
      * Operação escolhida (1=Soma, 2=Subtração)
       01 WS-OPERACAO          PIC 9(1) VALUE ZEROS.

      * Resultado com sinal para suportar negativos
       01 WS-RESULTADO         PIC S9(6) VALUE ZEROS.

      * Resultado formatado para display (exibe sinal negativo)
       01 WS-RESULTADO-DISPLAY PIC -(5)9.
```

> **Atenção:** altere o `PIC` de `WS-RESULTADO` de `9(6)` para `S9(6)`
> e de `WS-RESULTADO-DISPLAY` de `Z(5)9` para `-(5)9`.

### 2. Adicionar Parágrafo EXIBIR-MENU

```cobol
      ******************************************************************
      * EXIBIR-MENU - Solicita a operação desejada
      ******************************************************************
       EXIBIR-MENU.
           DISPLAY " ".
           DISPLAY "Escolha a operacao:".
           DISPLAY "  1 - Soma".
           DISPLAY "  2 - Subtracao".
           DISPLAY " ".
           DISPLAY "Digite sua opcao (1 ou 2): ".
           ACCEPT WS-OPERACAO.
```

### 3. Adicionar Parágrafo CALCULAR-SUBTRACAO

```cobol
      ******************************************************************
      * CALCULAR-SUBTRACAO - Realiza a operação de subtração
      ******************************************************************
       CALCULAR-SUBTRACAO.
           SUBTRACT WS-NUMERO-2 FROM WS-NUMERO-1
               GIVING WS-RESULTADO.
           MOVE WS-RESULTADO TO WS-RESULTADO-DISPLAY.
```

### 4. Atualizar o Parágrafo INICIO

```cobol
       INICIO.
           PERFORM EXIBIR-CABECALHO.
           PERFORM EXIBIR-MENU.
           PERFORM LER-NUMEROS.
           IF WS-OPERACAO = 1
               PERFORM CALCULAR-SOMA
           ELSE IF WS-OPERACAO = 2
               PERFORM CALCULAR-SUBTRACAO
           ELSE
               DISPLAY "Opcao invalida! Encerrando."
               STOP RUN
           END-IF.
           PERFORM EXIBIR-RESULTADO.
           STOP RUN.
```

### 5. Atualizar EXIBIR-RESULTADO para refletir a operação

```cobol
       EXIBIR-RESULTADO.
           DISPLAY " ".
           DISPLAY WS-LINHA.
           IF WS-OPERACAO = 1
               DISPLAY "RESULTADO DA SOMA"
           ELSE
               DISPLAY "RESULTADO DA SUBTRACAO"
           END-IF.
           DISPLAY WS-LINHA.
           IF WS-OPERACAO = 1
               DISPLAY WS-NUMERO-1 " + " WS-NUMERO-2 " = "
                   WS-RESULTADO-DISPLAY
           ELSE
               DISPLAY WS-NUMERO-1 " - " WS-NUMERO-2 " = "
                   WS-RESULTADO-DISPLAY
           END-IF.
           DISPLAY WS-LINHA.
           DISPLAY " ".
           DISPLAY "Programa encerrado com sucesso!".
```

## Saída Esperada

### Caso 1 — Soma (opção 1)

```
========================================
       CALCULADORA COBOL
       Soma e Subtracao
========================================

Escolha a operacao:
  1 - Soma
  2 - Subtracao

Digite sua opcao (1 ou 2): 
1

Digite o primeiro numero (0-99999): 
100
Digite o segundo numero (0-99999): 
50

========================================
RESULTADO DA SOMA
========================================
00100 + 00050 =    150
========================================

Programa encerrado com sucesso!
```

### Caso 2 — Subtração com resultado negativo (opção 2)

```
========================================
       CALCULADORA COBOL
       Soma e Subtracao
========================================

Escolha a operacao:
  1 - Soma
  2 - Subtracao

Digite sua opcao (1 ou 2): 
2

Digite o primeiro numero (0-99999): 
30
Digite o segundo numero (0-99999): 
100

========================================
RESULTADO DA SUBTRACAO
========================================
00030 - 00100 =    -70
========================================

Programa encerrado com sucesso!
```

## Passos para Executar

1. Leia o skill SKILL.md
2. Modifique o arquivo CALCULADORA.cbl
3. Adicione/atualize as variáveis na WORKING-STORAGE
4. Implemente os novos parágrafos na PROCEDURE DIVISION
5. Compile com `cobc -x -o calculadora src/CALCULADORA.cbl`
6. Execute com calculadora
7. Teste a soma com 100 e 50
8. Teste a subtração com 30 e 100 (resultado negativo)

## Critérios de Sucesso

- [ ] Variável `WS-OPERACAO` declarada com `PIC 9(1)`
- [ ] `WS-RESULTADO` atualizado para `PIC S9(6)` (com sinal)
- [ ] `WS-RESULTADO-DISPLAY` atualizado para `PIC -(5)9`
- [ ] Parágrafo `EXIBIR-MENU` implementado
- [ ] Parágrafo `CALCULAR-SUBTRACAO` implementado com `SUBTRACT`
- [ ] `INICIO` atualizado com lógica condicional `IF/ELSE IF/ELSE`
- [ ] Validação de opção inválida presente
- [ ] `EXIBIR-RESULTADO` exibe símbolo e título corretos
- [ ] Programa compila sem erros
- [ ] Soma e subtração produzem resultados corretos
- [ ] Resultado negativo exibe sinal `-`

## Regras COBOL a Lembrar

- `PIC S9(n)` para números com sinal
- `PIC -(n)9` para exibir sinal negativo no display
- `SUBTRACT B FROM A GIVING C` — subtrai B de A, guarda em C
- Toda sentença termina com ponto
- `IF/ELSE IF/ELSE/END-IF` para múltiplas condições
- Use `PERFORM` para chamar parágrafos

## Após Completar

Mostre o código completo e as saídas dos dois casos de teste.
Sugira revisar com o agente `cobol-reviewer.agent.md`.

Vamos subtrair em COBOL! 🖥️
