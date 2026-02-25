---
name: Implementar Soma COBOL
description: Implementa a função de soma na Calculadora COBOL
mode: agent
---

# 🖥️ Missão: Implementar Função de Soma

## Contexto

O programa COBOL já tem a estrutura básica.
Agora você vai implementar a calculadora completa.
Foco: operação de soma com dois números.

## Sua Tarefa

Modifique o arquivo `src/CALCULADORA.cbl` para:

### 1. Adicionar Variáveis na DATA DIVISION

```cobol
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
```

### 2. Implementar a PROCEDURE DIVISION

Crie os seguintes parágrafos:

1. **INICIO** - Controla o fluxo principal
2. **EXIBIR-CABECALHO** - Mostra título do programa
3. **LER-NUMEROS** - Solicita os dois números
4. **CALCULAR-SOMA** - Realiza a soma
5. **EXIBIR-RESULTADO** - Mostra o resultado formatado

### 3. Lógica Esperada

```
1. Exibir cabeçalho bonito
2. Pedir primeiro número
3. Pedir segundo número
4. Calcular: resultado = numero1 + numero2
5. Formatar resultado (suprimir zeros)
6. Exibir resultado
7. Encerrar com STOP RUN
```

## Saída Esperada

```
========================================
       CALCULADORA COBOL
       Soma de Dois Numeros
========================================
 
Digite o primeiro numero (0-99999): 
5
Digite o segundo numero (0-99999): 
3
 
========================================
RESULTADO DA SOMA
========================================
00005 + 00003 =      8
========================================
 
Programa encerrado com sucesso!
```

## Passos para Executar

1. Leia o skill `.github/skills/cobol-calculadora/SKILL.md`
2. Modifique o arquivo `src/CALCULADORA.cbl`
3. Adicione as variáveis na WORKING-STORAGE
4. Implemente os parágrafos na PROCEDURE DIVISION
5. Compile com `cobc -x -o calculadora src/CALCULADORA.cbl`
6. Execute com `./calculadora`
7. Teste com os valores 5 e 3

## Critérios de Sucesso

- [ ] Variáveis declaradas corretamente
- [ ] Todos os parágrafos implementados
- [ ] Entrada de dados funcionando (ACCEPT)
- [ ] Cálculo de soma correto (ADD)
- [ ] Resultado formatado corretamente
- [ ] Programa compila sem erros
- [ ] Programa executa e produz saída esperada

## Regras COBOL a Lembrar

- Colunas 8-11: Área A (parágrafos)
- Colunas 12-72: Área B (código)
- Toda sentença termina com ponto
- Use PERFORM para chamar parágrafos
- Use ADD ... GIVING para soma
- Use MOVE para copiar valores

## Após Completar

Mostre o código completo e a saída do programa.
Sugira usar o próximo prompt: `testar-programa.prompt.md`

Vamos somar em COBOL! 🖥️
