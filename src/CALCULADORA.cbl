      ******************************************************************
      * Programa: CALCULADORA
      * Descrição: Calculadora de soma, subtracao, multiplicacao, divisao e log
      * Autor: Copilot Agent
      * Data: 2026
      ******************************************************************
       IDENTIFICATION DIVISION.
       PROGRAM-ID. CALCULADORA.
       AUTHOR. COPILOT-AGENT.
       DATE-WRITTEN. 2026.
       DATE-COMPILED.

       ENVIRONMENT DIVISION.
       CONFIGURATION SECTION.
       SOURCE-COMPUTER. PC.
       OBJECT-COMPUTER. PC.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
      * Números de entrada
       01 WS-NUMERO-1          PIC 9(5) VALUE ZEROS.
       01 WS-NUMERO-2          PIC 9(5) VALUE ZEROS.

      * Operação escolhida (1=Soma, 2=Subtracao, 3=Multiplicacao, 4=Divisao)
       01 WS-OPERACAO          PIC 9(1) VALUE ZEROS.

      * Resultado com sinal para suportar negativos
      * PIC S9(10) para comportar multiplicacao (99999 x 99999 = ~10 digitos)
       01 WS-RESULTADO         PIC S9(10) VALUE ZEROS.

      * Resultado formatado para display (exibe sinal negativo)
       01 WS-RESULTADO-DISPLAY PIC -(9)9.

      * Resultado da divisão com 2 casas decimais
       01 WS-RESULTADO-DIVISAO     PIC S9(10)V99 VALUE ZEROS.

      * Resultado da divisão formatado para display
       01 WS-RESULTADO-DIV-DISPLAY PIC -(9)9.99.

      * Resultado do logaritmo com 6 casas decimais
       01 WS-RESULTADO-LOG         PIC S9(5)V9(6) VALUE ZEROS.

      * Resultado do logaritmo formatado para display
       01 WS-RESULTADO-LOG-DISPLAY PIC -(4)9.9(6).

      * Linha decorativa
       01 WS-LINHA             PIC X(40) VALUE ALL "=".

       PROCEDURE DIVISION.

      ******************************************************************
      * INICIO - Parágrafo principal que controla o fluxo
      ******************************************************************
       INICIO.
           PERFORM EXIBIR-CABECALHO.
           PERFORM EXIBIR-MENU.
           IF WS-OPERACAO = 5
               PERFORM LER-NUMERO-LOG
           ELSE
               PERFORM LER-NUMEROS
           END-IF.
           IF WS-OPERACAO = 1
               PERFORM CALCULAR-SOMA
           ELSE IF WS-OPERACAO = 2
               PERFORM CALCULAR-SUBTRACAO
           ELSE IF WS-OPERACAO = 3
               PERFORM CALCULAR-MULTIPLICACAO
           ELSE IF WS-OPERACAO = 4
               PERFORM CALCULAR-DIVISAO
           ELSE IF WS-OPERACAO = 5
               PERFORM CALCULAR-LOG
           ELSE
               DISPLAY "Opcao invalida! Encerrando."
               STOP RUN
           END-IF.
           PERFORM EXIBIR-RESULTADO.
           STOP RUN.

      ******************************************************************
      * EXIBIR-CABECALHO - Mostra o título do programa
      ******************************************************************
       EXIBIR-CABECALHO.
           DISPLAY WS-LINHA.
           DISPLAY "       CALCULADORA COBOL".
           DISPLAY "   Soma, Subtracao, Multiplicacao, Divisao e Log".
           DISPLAY WS-LINHA.

      ******************************************************************
      * EXIBIR-MENU - Solicita a operação desejada
      ******************************************************************
       EXIBIR-MENU.
           DISPLAY " ".
           DISPLAY "Escolha a operacao:".
           DISPLAY "  1 - Soma".
           DISPLAY "  2 - Subtracao".
           DISPLAY "  3 - Multiplicacao".
           DISPLAY "  4 - Divisao".
           DISPLAY "  5 - Logaritmo (base 10)".
           DISPLAY " ".
           DISPLAY "Digite sua opcao (1, 2, 3, 4 ou 5): ".
           ACCEPT WS-OPERACAO.

      ******************************************************************
      * LER-NUMEROS - Solicita os números ao usuário
      ******************************************************************
       LER-NUMEROS.
           DISPLAY " ".
           DISPLAY "Digite o primeiro numero (0-99999): ".
           ACCEPT WS-NUMERO-1.
           DISPLAY "Digite o segundo numero (0-99999): ".
           ACCEPT WS-NUMERO-2.

      ******************************************************************
      * LER-NUMERO-LOG - Solicita apenas um numero para o logaritmo
      ******************************************************************
       LER-NUMERO-LOG.
           DISPLAY " ".
           DISPLAY "Digite o numero (deve ser maior que zero): ".
           ACCEPT WS-NUMERO-1.

      ******************************************************************
      * CALCULAR-SOMA - Realiza a operação de soma
      ******************************************************************
       CALCULAR-SOMA.
           ADD WS-NUMERO-1 TO WS-NUMERO-2
               GIVING WS-RESULTADO.
           MOVE WS-RESULTADO TO WS-RESULTADO-DISPLAY.

      ******************************************************************
      * CALCULAR-SUBTRACAO - Realiza a operação de subtração
      ******************************************************************
       CALCULAR-SUBTRACAO.
           SUBTRACT WS-NUMERO-2 FROM WS-NUMERO-1
               GIVING WS-RESULTADO.
           MOVE WS-RESULTADO TO WS-RESULTADO-DISPLAY.

      ******************************************************************
      * CALCULAR-MULTIPLICACAO - Realiza a operação de multiplicação
      ******************************************************************
       CALCULAR-MULTIPLICACAO.
           MULTIPLY WS-NUMERO-1 BY WS-NUMERO-2
               GIVING WS-RESULTADO.
           MOVE WS-RESULTADO TO WS-RESULTADO-DISPLAY.

      ******************************************************************
      * CALCULAR-DIVISAO - Realiza a operação de divisão
      *                    Verifica divisão por zero antes de calcular
      ******************************************************************
       CALCULAR-DIVISAO.
           IF WS-NUMERO-2 = ZERO
               DISPLAY " "
               DISPLAY "ERRO: Divisao por zero nao e permitida!"
               DISPLAY " "
               STOP RUN
           ELSE
               DIVIDE WS-NUMERO-1 BY WS-NUMERO-2
                   GIVING WS-RESULTADO-DIVISAO
               MOVE WS-RESULTADO-DIVISAO
                   TO WS-RESULTADO-DIV-DISPLAY
           END-IF.

      ******************************************************************
      * CALCULAR-LOG - Calcula o logaritmo base 10 do numero
      *                Verifica se o numero e maior que zero
      ******************************************************************
       CALCULAR-LOG.
           IF WS-NUMERO-1 <= ZERO
               DISPLAY " "
               DISPLAY "ERRO: Logaritmo de zero nao e permitido!"
               DISPLAY " "
               STOP RUN
           ELSE
               COMPUTE WS-RESULTADO-LOG =
                   FUNCTION LOG10(WS-NUMERO-1)
               MOVE WS-RESULTADO-LOG
                   TO WS-RESULTADO-LOG-DISPLAY
           END-IF.

      ******************************************************************
      * EXIBIR-RESULTADO - Mostra o resultado formatado
      ******************************************************************
       EXIBIR-RESULTADO.
           DISPLAY " ".
           DISPLAY WS-LINHA.
           IF WS-OPERACAO = 1
               DISPLAY "RESULTADO DA SOMA"
           ELSE IF WS-OPERACAO = 2
               DISPLAY "RESULTADO DA SUBTRACAO"
           ELSE IF WS-OPERACAO = 3
               DISPLAY "RESULTADO DA MULTIPLICACAO"
           ELSE IF WS-OPERACAO = 4
               DISPLAY "RESULTADO DA DIVISAO"
           ELSE
               DISPLAY "RESULTADO DO LOGARITMO"
           END-IF.
           DISPLAY WS-LINHA.
           IF WS-OPERACAO = 1
               DISPLAY WS-NUMERO-1 " + " WS-NUMERO-2 " = "
                   WS-RESULTADO-DISPLAY
           ELSE IF WS-OPERACAO = 2
               DISPLAY WS-NUMERO-1 " - " WS-NUMERO-2 " = "
                   WS-RESULTADO-DISPLAY
           ELSE IF WS-OPERACAO = 3
               DISPLAY WS-NUMERO-1 " x " WS-NUMERO-2 " = "
                   WS-RESULTADO-DISPLAY
           ELSE IF WS-OPERACAO = 4
               DISPLAY WS-NUMERO-1 " / " WS-NUMERO-2 " = "
                   WS-RESULTADO-DIV-DISPLAY
           ELSE
               DISPLAY "LOG10(" WS-NUMERO-1 ") = "
                   WS-RESULTADO-LOG-DISPLAY
           END-IF.
           DISPLAY WS-LINHA.
           DISPLAY " ".
           DISPLAY "Programa encerrado com sucesso!".
