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

      * Resultado
       01 WS-RESULTADO         PIC 9(6) VALUE ZEROS.

      * Resultado formatado para display
       01 WS-RESULTADO-DISPLAY PIC Z(5)9.

      * Linha decorativa
       01 WS-LINHA             PIC X(40) VALUE ALL "=".

       PROCEDURE DIVISION.

      ******************************************************************
      * INICIO - Parágrafo principal que controla o fluxo
      ******************************************************************
       INICIO.
           PERFORM EXIBIR-CABECALHO.
           PERFORM LER-NUMEROS.
           PERFORM CALCULAR-SOMA.
           PERFORM EXIBIR-RESULTADO.
           STOP RUN.

      ******************************************************************
      * EXIBIR-CABECALHO - Mostra o título do programa
      ******************************************************************
       EXIBIR-CABECALHO.
           DISPLAY WS-LINHA.
           DISPLAY "       CALCULADORA COBOL".
           DISPLAY "       Soma de Dois Numeros".
           DISPLAY WS-LINHA.

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
      * EXIBIR-RESULTADO - Mostra o resultado formatado
      ******************************************************************
       EXIBIR-RESULTADO.
           DISPLAY " ".
           DISPLAY WS-LINHA.
           DISPLAY "RESULTADO DA SOMA".
           DISPLAY WS-LINHA.
           DISPLAY WS-NUMERO-1 " + " WS-NUMERO-2 " = "
               WS-RESULTADO-DISPLAY.
           DISPLAY WS-LINHA.
           DISPLAY " ".
           DISPLAY "Programa encerrado com sucesso!".
