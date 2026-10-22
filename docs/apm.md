# APM no Cowboy: o que foi feito e o que aprendemos

> Primeira versão. Documento de estudo sobre o **APM (Agent Package Manager)**, o que mudou no repositório `cowboy` ao adotá-lo, o que é bom, o que é ruim, boas práticas e alternativas.
>
> Versões resumidas: [apm.compacto.md](apm.compacto.md) (uma página) e [apm.view.md](apm.view.md) (diagramas Mermaid).

**Status de confiança.** Este texto separa o que foi **verificado** (executado ou lido na documentação oficial) do que é **hipótese**. O `apm install` ainda **não foi executado** neste projeto; tudo sobre o comportamento real do CLI está marcado como pendente de validação na seção [Pendências](#9-pendências-e-riscos-conhecidos).

---

## 1. O que é o APM

O APM é um gerenciador de dependências para o **contexto de agentes de IA**, na mesma ideia do npm para código. Em vez de copiar skills, prompts, agents e hooks de projeto em projeto, você os declara em um manifesto e instala com um comando.

| Conceito | Papel |
|---|---|
| `apm.yml` | Manifesto. Lista o que o projeto precisa e os metadados do pacote. |
| `apm.lock.yaml` | Lockfile. Fixa versões e hashes de conteúdo para reprodutibilidade. |
| `.apm/` | Diretório **de origem** de um pacote (onde você escreve). |
| `apm install` | Resolve, escaneia e **implanta** nos diretórios de cada agente (`.claude/`, `.github/`...). |
| Pacote | Um repositório git com `apm.yml` e `.apm/`. Pode ser privado. |

### Primitivos suportados

Layout de autoria dentro de `.apm/`:

| Pasta | Conteúdo | No Claude Code | No GitHub Copilot |
|---|---|---|---|
| `instructions/*.instructions.md` | Regras sempre ativas | `.claude/rules/` | nativo |
| `prompts/*.prompt.md` | Prompts reutilizáveis | viram `.claude/commands/` | nativo |
| `agents/*.agent.md` | Agentes nomeados | nativo | nativo |
| `skills/<nome>/SKILL.md` | Skills multi-arquivo | nativo | nativo |
| `hooks/*.json` | Hooks de ciclo de vida | mesclados em `.claude/settings.json` | nativo |
| MCP servers | Declarados em `dependencies.mcp` | nativo | nativo |

Regra de ouro da documentação oficial: pastas como `.claude/` e `.github/` são **saída de build**. Edite `.apm/` (no pacote), não a cópia instalada.

### Comandos principais

| Comando | Função |
|---|---|
| `apm init` | Cria o `apm.yml`. |
| `apm install` | Resolve dependências, aplica checagens de segurança/política, grava o lockfile e implanta. `--dry-run` mostra o plano; `--frozen` instala só do lockfile (para CI). |
| `apm update` | Re-resolve referências e pede confirmação antes de reescrever o lockfile. |
| `apm compile` | Gera arquivos agregados como `AGENTS.md` e `GEMINI.md`. |
| `apm run` | Executa um script declarado em `scripts:`. |
| `apm pack` | Empacota para distribuição (bundle de plugin do Claude por padrão). |

### Segurança embutida

Segundo a documentação, cada instalação escaneia caracteres Unicode ocultos, fixa hashes de conteúdo e bloqueia servidores MCP transitivos que não tenham sido declarados ou marcados como confiáveis. Existe ainda `apm-policy.yml` para regras de governança aplicadas na instalação.

### Autenticação em repositórios privados

Para GitHub, o APM procura, nesta ordem: `GITHUB_APM_PAT_<ORG>`, `GITHUB_APM_PAT`, `GITHUB_TOKEN`, `GH_TOKEN` e, por fim, `gh auth token`. Para outros hosts usa o credential helper do git. Chaves SSH precisam estar carregadas (`ssh-add`), pois o clone é não interativo.

---

## 2. Por que adotamos

Antes, o `cowboy` carregava **tudo** dentro do repositório: aplicação COBOL, harness (hooks, gate de fase, skills de SDLC) e documentação. Isso tem três custos:

1. **Acoplamento.** O que é ferramenta de trabalho ficava misturado com o produto.
2. **Cópia manual.** Cada novo projeto precisava reinstalar o harness (a skill `install-dev-harness` existia só para isso) e as cópias divergiam.
3. **Sem versão.** Não havia como dizer "este projeto usa o harness v0.2".

O APM resolve isso tratando o harness como **dependência versionada**.

---

## 3. O que foi feito

### 3.1 Pacote privado `emilianoeloi/apm`

Criado a partir de arquivos que já existiam no `cowboy`:

```
apm/
├── apm.yml                      # name: harness, type: hybrid, targets: claude+copilot
├── README.md
└── .apm/
    ├── skills/                  # harness, dev-harness-architect, harness-quadrant-process,
    │                            # architecture-fitness-functions, openspec-workflow,
    │                            # openspdd-workflow, vibe-coding-fundamentals
    ├── hooks/harness.json       # PreToolUse (Write/Edit, Bash) e SessionStart
    ├── scripts/                 # hooks .py, phase_cli.py, pre-commit
    └── templates/               # harness.config.json, HARNESS_QUADRANTE.md
```

### 3.2 O que saiu do `cowboy`

| Removido | Destino |
|---|---|
| `scripts/hooks/*.py`, `scripts/harness/phase_cli.py`, `scripts/git-hooks/pre-commit` | pacote |
| `harness.config.json`, `.claude/settings.json` | pacote (config e hooks) |
| 8 skills em `.github/skills/` (7 de harness/SDLC + `install-dev-harness`) | pacote (a última ficou obsoleta: o APM é o instalador) |
| `docs/HARNESS_QUADRANTE.md` | template do pacote |

### 3.3 O que ficou e o que foi adicionado

- **Ficou** (é do produto): `src/`, `tests/`, agents `cobol-*`, prompts, skills de COBOL, `readme-manutencao`, `conversa-release`.
- **Adicionado:** `apm.yml` com `dependencies.apm: [emilianoeloi/apm#main]`; alvos `make apm-install` e `make apm-frozen`; `CLAUDE.md` e `AGENTS.md` atualizados.

### 3.4 Incidentes durante a migração (aprendizados reais)

| Incidente | Causa | Lição |
|---|---|---|
| Ferramentas Bash/Write bloqueadas após apagar os scripts de hook | A sessão do Claude Code carrega os hooks na inicialização; ao apagar os scripts, os hooks em cache passaram a falhar e **bloquear** tudo | Remover hooks e seus scripts exige cuidado com a sessão em andamento. Ordem segura: tirar a referência em `settings.json`, reiniciar a sessão, só então apagar os scripts. |
| CI do PR quebrou | O workflow rodava `make apm-frozen`, que exige `apm.lock.yaml` (inexistente) e o secret `APM_PAT` (não criado) | Não coloque o gerenciador de pacotes no caminho crítico do CI antes de ter lockfile e credencial. Os gates de COBOL não dependem do harness. |
| `gh` falhando com `Bad credentials` | `GITHUB_TOKEN` inválido no ambiente | O mesmo token seria usado pelo APM **antes** do `gh auth token`. Um token inválido no ambiente pode atrapalhar o `apm install`. |
| Commit com `Co-Authored-By` indesejado | Instrução automática de atribuição | Preferência do usuário registrada em memória; commit reescrito antes do merge. |

Correção do CI: os passos do APM foram removidos do workflow (commit `f01d489` na branch do PR #17). Os alvos `apm-install`/`apm-frozen` ficaram no Makefile para uso local.

---

## 4. Como o fluxo funciona

1. Quem mantém o harness edita o **pacote** `emilianoeloi/apm` em `.apm/` e publica (commit/tag).
2. No projeto consumidor, `apm.yml` aponta para o pacote e uma referência (`#main`, `#v0.1.0`).
3. `apm install` clona o pacote, valida, grava `apm.lock.yaml` e implanta em `.claude/` e `.github/`.
4. O agente (Claude Code ou Copilot) lê o que foi implantado.
5. Para atualizar: `apm update`, revisar o plano, commitar o novo lockfile.

Veja os diagramas em [apm.view.md](apm.view.md).

---

## 5. O que é bom

- **Fonte única do harness.** Corrige uma vez, todos os projetos recebem.
- **Versionamento e reprodutibilidade.** Referência por tag + lockfile com hash.
- **Multi-agente.** O mesmo pacote serve Claude Code e Copilot (e outros, conforme a matriz de suporte).
- **Separação produto/ferramenta.** O repositório do produto fica mais limpo.
- **Segurança por padrão.** Varredura de Unicode oculto, hashes e bloqueio de MCP transitivo.
- **Privado e sem registry.** Qualquer repositório git serve; não depende de um marketplace.
- **Governança.** `apm-policy.yml` permite regras organizacionais.

## 6. O que é ruim ou arriscado

- **Ferramenta jovem.** Há inconsistências na própria documentação (por exemplo, a matriz de suporte a hooks diverge do glossário). Espere mudanças.
- **Mais um passo de setup.** `apm install` vira pré-requisito para clonar e trabalhar; sem ele o projeto perde hooks e skills.
- **Dependência de credencial.** Pacote privado exige PAT/SSH no desenvolvimento **e** no CI.
- **Saída de build versionada ou não?** Se `.claude/` e `.github/` forem commitados, surge ruído de diff; se não forem, quem clona sem o APM fica sem harness. É uma decisão de projeto.
- **Hooks com scripts.** Hooks são JSON, mas o nosso depende de scripts `.py`. O modo como o APM entrega scripts auxiliares não foi confirmado (ver pendências).
- **Execução de código de terceiros.** Skills e hooks rodam com permissões do agente. Pacote comprometido = risco. Fixe versões e revise antes de atualizar.
- **Suporte desigual entre agentes.** Alguns agentes não suportam hooks; o comportamento do pacote muda por alvo.
- **Quebra silenciosa em refatorações.** Os agents `cobol-*` do cowboy ainda citam `scripts/harness/phase_cli.py`, que deixou de existir no repositório. Remoções em um lado quebram o outro sem aviso.

---

## 7. Boas práticas

### Para o pacote
1. **Versione com tags semânticas** (`v0.1.0`) e consuma por tag, não por `#main`, assim que estabilizar.
2. **Um pacote por responsabilidade.** Considere separar `harness-core` (hooks e fase) de `sdlc` (openspec, spdd). Projetos pegam só o que precisam.
3. **Genérico no pacote, específico no projeto.** O pacote não deve conhecer COBOL; o projeto não deve reimplementar o harness.
4. **Hooks defensivos.** Falhar para "permitir" quando a config estiver ausente (o nosso já faz isso) evita travar o agente.
5. **README com contrato.** Documente o que o pacote instala e o que espera do projeto (arquivos, variáveis).
6. **Sem segredos no pacote.** Credenciais ficam em variáveis de ambiente.

### Para o consumidor
1. **Commite `apm.lock.yaml`.** Sem ele, `--frozen` falha e as instalações não são reproduzíveis.
2. **Use `apm install --frozen` no CI** somente depois que o lockfile e o secret existirem.
3. **Atualize de propósito.** `apm update --dry-run`, leia o plano, atualize num PR separado.
4. **Trate `.claude/` e `.github/` como saída de build** e documente se são versionados ou ignorados.
5. **Credencial dedicada.** PAT de leitura restrito ao repositório do pacote (`GITHUB_APM_PAT`), nunca um token amplo.
6. **Mantenha o CI independente quando possível.** Gates de qualidade do produto não deveriam depender de ferramentas de produtividade do agente.
7. **Ao remover hooks, reinicie a sessão** antes de apagar os scripts (ver incidente 3.4).

---

## 8. Alternativas no mercado

O ecossistema é novo e fragmentado. A comparação abaixo é qualitativa e baseada em fontes comunitárias; confirme cada projeto no repositório oficial antes de adotar.

| Opção | O que é | Pontos fortes | Limites |
|---|---|---|---|
| **APM (Microsoft)** | Gerenciador com manifesto + lockfile + política | Reprodutível, multi-agente, qualquer host git, segurança | Jovem; exige CLI e credencial |
| **Plugins e marketplaces do Claude Code** | Distribuição nativa (plugin com skills, agents, hooks, comandos, MCP) | Integrado ao Claude Code; diretório oficial da Anthropic | Específico do ecossistema Claude; Copilot exige manifestos adicionais |
| **Vercel `skills` CLI** (`npx skills add`) | Instalador de skills para dezenas de agentes | Muito simples; ampla compatibilidade; `skills-lock.json` | Focado em skills; restauração via `experimental_install` ainda experimental |
| **OpenSkills** | Carregador universal de skills | Funciona com agentes que leem `AGENTS.md` | Focado em skills |
| **Ruler / rulesync** | Sincronizam um conjunto de regras para vários agentes | Resolvem o problema de "mesma regra, N formatos" | Não gerenciam versões de dependências |
| **`AGENTS.md` puro** | Formato aberto de instruções | Zero ferramenta; suportado por vários agentes | Não distribui skills/hooks; sem versionamento |
| **Git submodule / cópia manual** | Compartilhar pastas entre repositórios | Sem dependência nova | Sem resolução, hash ou segurança; trabalhoso |

### Quando escolher o quê

- **Só regras de texto para vários agentes:** `AGENTS.md` + Ruler/rulesync.
- **Só skills, rápido:** `skills` CLI ou OpenSkills.
- **Time 100% Claude Code, quer distribuição oficial:** plugins/marketplace.
- **Vários agentes, versionamento, privado, governança:** APM (o nosso caso).
- **Equipe pequena, harness estável:** talvez o custo do APM não compense; um submodule já basta.

---

## 9. Pendências e riscos conhecidos

Itens abertos após o merge do PR #17:

| # | Pendência | Impacto |
|---|---|---|
| 1 | **`apm install` nunca foi executado.** O CLI não está instalado na máquina de desenvolvimento. | Todo o comportamento real é hipótese até rodar. |
| 2 | **Entrega dos scripts dos hooks.** O `harness.json` do pacote ainda referencia `$CLAUDE_PROJECT_DIR/scripts/hooks/...`, que não existe mais no cowboy. | Hooks podem não funcionar após o install. |
| 3 | **Sem `apm.lock.yaml`.** | `--frozen` indisponível; instalação não reproduzível. |
| 4 | **Secret `APM_PAT` não criado** e `GITHUB_TOKEN` local inválido. | CI e instalação local podem falhar na autenticação. |
| 5 | **Agents `cobol-*` citam `scripts/harness/phase_cli.py`.** | Instruções apontam para arquivo inexistente. |
| 6 | **`#main` como referência.** | Mudança no pacote altera o projeto sem aviso. Migrar para tags. |
| 7 | **Divisão do pacote** (core vs sdlc) não decidida. | Acoplamento maior que o necessário. |

### Próximos passos sugeridos

1. Instalar o CLI, corrigir o token e rodar `apm install --dry-run`, depois `apm install`.
2. Inspecionar o que foi implantado em `.claude/` e `.github/`; resolver a pendência 2.
3. Commitar `apm.lock.yaml`; criar o secret e só então reintroduzir `apm install --frozen` no CI.
4. Ajustar os agents `cobol-*`.
5. Publicar a tag `v0.1.0` do pacote e trocar a referência.

---

## 10. Glossário

| Termo | Significado |
|---|---|
| Primitivo | Tipo de artefato de contexto: instrução, prompt, agent, skill, hook, MCP. |
| Harness | Conjunto de regras, hooks, skills e gates que governam o trabalho do agente. |
| Gate de fase | Mecanismo `proposal`/`apply` que bloqueia escrita em código durante o planejamento. |
| Saída de build | Arquivos gerados pelo APM em `.claude/` e `.github/`; não se edita à mão. |
| Lockfile | `apm.lock.yaml`; versões e hashes exatos. |
| Target | Agente de destino (`claude`, `copilot`...). |

---

## Fontes

- [Documentação do APM](https://microsoft.github.io/apm/)
- [APM llms-full.txt (referência completa)](https://microsoft.github.io/apm/llms-full.txt)
- [README do APM](https://cdn.jsdelivr.net/gh/microsoft/apm@main/README.md)
- [apm-cli no PyPI](https://pypi.org/project/apm-cli/)
- [Agent Skills, Plugins and Marketplace: The Complete Guide](https://chris-ayers.com/posts/agent-skills-plugins-marketplace/)
- [7 AI Agent Skills Marketplaces in 2026 (Compared)](https://www.agensi.io/learn/best-ai-agent-skills-marketplaces-2026)
- [Claude Skills Managers & CLIs](https://agentskillshub.top/best/skill-management-tools/)
- [n-skills (marketplace curado)](https://github.com/numman-ali/n-skills)
- [awesome-coding-agent-skills](https://github.com/Abdalkaderdev/awesome-coding-agent-skills)
