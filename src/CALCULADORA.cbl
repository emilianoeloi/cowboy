      ******************************************************************
      * Programa: CALCULADORA
      * Descrição: Calculadora de soma em COBOL
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

      * Operação escolhida (1=Soma, 2=Subtração)
       01 WS-OPERACAO          PIC 9(1) VALUE ZEROS.

      * Resultado com sinal para suportar negativos
       01 WS-RESULTADO         PIC S9(6) VALUE ZEROS.

      * Resultado formatado para display (exibe sinal negativo)
       01 WS-RESULTADO-DISPLAY PIC -(5)9.

      * Linha decorativa
       01 WS-LINHA             PIC X(40) VALUE ALL "=".

       PROCEDURE DIVISION.

      ******************************************************************
      * INICIO - Parágrafo principal que controla o fluxo
      ******************************************************************
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

      ******************************************************************
      * EXIBIR-CABECALHO - Mostra o título do programa
      ******************************************************************
       EXIBIR-CABECALHO.
           DISPLAY WS-LINHA.
           DISPLAY "       CALCULADORA COBOL".
           DISPLAY "       Soma e Subtracao".
           DISPLAY WS-LINHA.

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
      * EXIBIR-RESULTADO - Mostra o resultado formatado
      ******************************************************************
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
