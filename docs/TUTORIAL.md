# Tutorial: Calculadora COBOL

## Aprendendo Agent Mode com COBOL

Este tutorial te ensina Agent Mode.
Usando COBOL como linguagem.
Uma combinação inesperada.
Mas muito educativa.

---

## Por Que COBOL?

COBOL é a linguagem dos mainframes.
Criada em 1959.
Ainda processa trilhões de dólares diariamente.

Aprender Agent Mode com COBOL mostra algo importante.
O Copilot funciona com qualquer linguagem.
Até as mais antigas.
Até as mais diferentes do seu dia a dia.

---

## A Estrutura do Projeto

O projeto tem uma organização específica.
Cada arquivo tem uma função.
Vamos entender.

### Na Raiz

README.md é a porta de entrada.
AGENTS.md são as regras globais.
TUTORIAL.md é este arquivo.
LEITURA_VOZ_ALTA.md é otimizado para você estudar.

### Na Pasta .github

Três subpastas importantes.

agents/ contém os três agentes.
skills/ contém o conhecimento COBOL.
prompts/ contém as missões.

### Na Pasta src (será criada)

Aqui ficará o código COBOL.
O arquivo CALCULADORA.cbl.
Criado pelo Agent Mode.

---

## Os Três Agentes

### COBOL Planner

O Planner pensa antes de agir.
Ele analisa a tarefa.
Cria um plano detalhado.
Mapeia as 4 divisões do COBOL.
Lista as variáveis necessárias.

Use o Planner para tarefas complexas.
Quando precisa pensar antes de fazer.

### COBOL Coder

O Coder é o implementador.
Ele escreve código COBOL.
Ele compila com GnuCOBOL.
Ele executa e testa.
Ele corrige erros.

Use o Coder para criar e modificar código.

### COBOL Reviewer

O Reviewer analisa qualidade.
Ele verifica estrutura.
Ele checa formatação de colunas.
Ele sugere melhorias.

Use o Reviewer após implementar.

---

## O Skill de COBOL

O skill está em .github/skills/cobol-calculadora/.
Contém conhecimento especializado.

Estrutura de programa COBOL.
Picture clauses explicadas.
Operações matemáticas.
Comandos de compilação.

O agente usa esse conhecimento.
Para escrever código correto.

---

## Os Três Prompts

### Prompt 1: Criar Programa

O primeiro prompt cria a estrutura.
Verifica se GnuCOBOL está instalado.
Cria a pasta src.
Cria o arquivo inicial.

É a fundação do projeto.

### Prompt 2: Implementar Soma

O segundo prompt adiciona a lógica.
Declara as variáveis.
Implementa os parágrafos.
Faz a calculadora funcionar.

É o coração do projeto.

### Prompt 3: Testar

O terceiro prompt valida tudo.
Testa vários cenários.
Documenta os resultados.
Confirma que funciona.

É a garantia de qualidade.

---

## COBOL em 5 Minutos

### As 4 Divisões

Todo programa COBOL tem 4 divisões.
Na ordem:

1. IDENTIFICATION DIVISION
   - Identifica o programa
   - Nome, autor, data

2. ENVIRONMENT DIVISION
   - Configurações de ambiente
   - Computador origem e destino

3. DATA DIVISION
   - Declara todas as variáveis
   - WORKING-STORAGE SECTION

4. PROCEDURE DIVISION
   - A lógica do programa
   - Parágrafos com código

### As Colunas

COBOL é sensível a colunas.
Isso vem da era dos cartões perfurados.

Colunas 1-6: números de linha.
Coluna 7: indicadores.
Colunas 8-11: Área A.
Colunas 12-72: Área B.

Área A é para divisões, seções, parágrafos.
Área B é para o código em si.

### Picture Clauses

PIC define o tipo da variável.

PIC 9(5) é um número de 5 dígitos.
PIC X(20) é texto de 20 caracteres.
PIC Z(5)9 suprime zeros à esquerda.

### Operações

COBOL é verboso.
As operações são palavras.

ADD A TO B GIVING C.
SUBTRACT A FROM B GIVING C.
MULTIPLY A BY B GIVING C.
DIVIDE A BY B GIVING C.

---

## Executando o Tutorial

### Passo 1: Preparar

Instale GnuCOBOL se necessário.
Abra o projeto no VS Code.
Ative o Agent Mode.

### Passo 2: Primeiro Prompt

Cole o conteúdo de criar-programa.prompt.md.
Observe o agente trabalhar.
Ele vai criar a estrutura.

### Passo 3: Segundo Prompt

Cole o conteúdo de implementar-soma.prompt.md.
Observe o agente adicionar a lógica.
A calculadora vai funcionar.

### Passo 4: Terceiro Prompt

Cole o conteúdo de testar-programa.prompt.md.
Observe o agente testar.
Veja o relatório final.

---

## O Que Você Aprende

### Sobre Agent Mode

- Como criar agentes especializados
- Como criar skills reutilizáveis
- Como criar prompts estruturados
- Como o agente usa ferramentas
- Como o agente itera até funcionar

### Sobre COBOL

- A estrutura de um programa
- As 4 divisões obrigatórias
- A importância das colunas
- Como declarar variáveis
- Como fazer operações matemáticas

### Sobre Aprendizado

- Que IA funciona com qualquer linguagem
- Que estrutura facilita autonomia
- Que instruções claras geram bons resultados
- Que iterar é parte do processo

---

## Expandindo

Depois de completar, você pode:

Adicionar subtração.
Adicionar multiplicação.
Adicionar divisão.
Criar um menu de opções.

Cada expansão é prática.
Com Agent Mode.
Com COBOL.

---

## Conclusão

COBOL é diferente de tudo que você usa.
Mas o Agent Mode funciona igual.

Agentes, skills, prompts.
A mesma estrutura.
Qualquer linguagem.

Isso é o poder do Agent Mode.
Abstração sobre a complexidade.
Autonomia com controle.

Bem-vindo ao mundo do COBOL.
E ao mundo do Agent Mode.

Vamos codar! 🖥️
