---
name: Testar Programa COBOL
description: Testa o programa COBOL com diferentes cenários
mode: agent
---

# 🖥️ Missão: Testar a Calculadora COBOL

## Contexto

A calculadora está implementada.
Agora você vai testar vários cenários.
Garantir que funciona corretamente.

## Sua Tarefa

Execute testes manuais com diferentes valores.
Documente os resultados.
Verifique se o programa funciona em todos os casos.

## Cenários de Teste

### Teste 1: Números Simples
```
Entrada: 5 e 3
Esperado: 8
```

### Teste 2: Zero
```
Entrada: 0 e 10
Esperado: 10

Entrada: 10 e 0
Esperado: 10
```

### Teste 3: Números Iguais
```
Entrada: 50 e 50
Esperado: 100
```

### Teste 4: Números Grandes
```
Entrada: 99999 e 1
Esperado: 100000
```

### Teste 5: Resultado Grande
```
Entrada: 50000 e 50000
Esperado: 100000
```

## Passos para Executar

1. Compile o programa (se ainda não compilou)
   ```bash
   cobc -x -o calculadora src/CALCULADORA.cbl
   ```

2. Para cada teste, execute o programa:
   ```bash
   ./calculadora
   ```

3. Digite os valores quando solicitado

4. Verifique se o resultado está correto

5. Documente o resultado de cada teste

## Formato de Documentação

Para cada teste, registre:

```markdown
### Teste X: [Nome do Teste]

**Entrada:**
- Primeiro número: X
- Segundo número: Y

**Saída do Programa:**
```
[cole a saída aqui]
```

**Resultado:** ✅ Passou / ❌ Falhou

**Observações:** [se houver]
```

## Critérios de Sucesso

- [ ] Teste 1 passou (5 + 3 = 8)
- [ ] Teste 2 passou (soma com zero)
- [ ] Teste 3 passou (números iguais)
- [ ] Teste 4 passou (número grande + 1)
- [ ] Teste 5 passou (resultado de 6 dígitos)

## Se Algum Teste Falhar

1. Identifique qual teste falhou
2. Analise a saída do programa
3. Verifique o código COBOL
4. Corrija o problema
5. Recompile e teste novamente

## Possíveis Problemas

### Overflow
Se o resultado exceder 999999 (6 dígitos):
- O COBOL pode truncar o valor
- Considere aumentar o PIC do resultado

### Zeros à Esquerda
Se os zeros não estão sendo suprimidos:
- Verifique se está usando Z no PIC de display
- Verifique se está fazendo MOVE para a variável de display

### Formatação
Se a saída não está alinhada:
- Verifique os DISPLAY
- Use SPACES para alinhar se necessário

## Relatório Final

Após todos os testes, crie um resumo:

```markdown
# 📊 Relatório de Testes - Calculadora COBOL

## Resumo
- Total de testes: 5
- Passou: X
- Falhou: Y

## Resultados

| Teste | Entrada | Esperado | Obtido | Status |
|-------|---------|----------|--------|--------|
| 1     | 5 + 3   | 8        | 8      | ✅     |
| 2a    | 0 + 10  | 10       | 10     | ✅     |
| 2b    | 10 + 0  | 10       | 10     | ✅     |
| 3     | 50 + 50 | 100      | 100    | ✅     |
| 4     | 99999+1 | 100000   | 100000 | ✅     |
| 5     | 50000+50000 | 100000 | 100000 | ✅ |

## Conclusão
[Aprovado/Reprovado com observações]

Calculadora COBOL testada e funcionando! 🖥️
```

## Após Completar

Apresente o relatório completo de testes.
Sugira revisar com `@cobol-reviewer` se desejar.
Celebre o sucesso do projeto!

Vamos testar como um mainframe! 🖥️
