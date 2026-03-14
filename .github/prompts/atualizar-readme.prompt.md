---
mode: agent
description: Atualiza os três READMEs (PT-BR, EN e ZH) após uma implementação concluída e testada. Use após terminar e validar uma nova feature.
---

# Prompt: Atualizar README

A implementação foi concluída e testada. Agora é hora de atualizar a documentação.

## Contexto

Leia os arquivos abaixo para entender o estado atual do projeto:

- `README.md` — README em português (fonte da verdade)
- `README-en.md` — README em inglês
- `README-zh.md` — README em chinês
- `src/CALCULADORA.cbl` — código fonte atual
- `.github/agents/` — agentes disponíveis
- `.github/skills/` — skills disponíveis
- `.github/prompts/` — prompts disponíveis
- `AGENTS.md` — instruções do projeto

## Tarefa

1. **Analise** o que mudou no projeto desde a última atualização dos READMEs
2. **Atualize** o `README.md` (PT-BR) com as mudanças
3. **Sincronize** o `README-en.md` com as mesmas mudanças em inglês
4. **Sincronize** o `README-zh.md` com as mesmas mudanças em chinês

## O Que Verificar e Atualizar

### Seção: Estrutura do Projeto
Reflita os arquivos e pastas atuais do repositório.

### Seção: O Que Você Vai Aprender / Features
Inclua todos os agentes, skills e prompts existentes.

### Seção: Como Usar
Verifique que as instruções de compilação e execução estão corretas.

### Seção: Exemplos
Se houver saída esperada do programa, atualize com o output atual.

## Restrições

- Mantenha o tom da **tagline**: *"Vibe Coding é programar sem entender o código"*
- Preserve todos os badges e links de navegação entre idiomas
- Não remova seções existentes — apenas atualize o conteúdo
- Use o skill `readme-manutencao` para guiar as traduções
- PT-BR sempre é a fonte da verdade; EN e ZH são derivados

## Formato de Resposta

Ao concluir, informe:
- Quais seções foram atualizadas em cada arquivo
- Se houver algo que não conseguiu traduzir com certeza, sinalize para revisão manual
