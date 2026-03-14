---
mode: agent
description: Adicionar operacao de logaritmo na calculadora COBOL
---

# Prompt: Implementar Logaritmo

## Objetivo
Adicionar a operacao de logaritmo base 10 como opcao 5 da calculadora COBOL.

## Contexto
O programa src/CALCULADORA.cbl ja possui 4 operacoes.
O logaritmo usa FUNCTION LOG10 do GnuCOBOL.
Por ser operacao unaria (1 numero), o fluxo de leitura deve ser ajustado.

## Criterios de Aceite
- [ ] Compilacao sem erros
- [ ] log10(100) = 2.000000
- [ ] log10(1000) = 3.000000
- [ ] Erro ao tentar log de zero
