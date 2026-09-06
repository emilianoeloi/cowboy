# O modelo de harness — referência completa

> Baseado no conceito de "Harness Engineering for Coding Agent Users"
> (Martin Fowler). Generalizado a partir do harness de dev do UIMaker ADK.

## Definição

**Harness** = tudo que envolve o agente de codificação além do próprio
modelo LLM: instruções, ferramentas, sensores e configurações que aumentam a
qualidade e a segurança das ações do agente.

## O quadrante

```
┌─────────────────────────────────────────────────────────────────┐
│  GUIAS (feedforward) — o que o agente sabe antes de agir        │
│                                                                  │
│  Inferencial                    Computacional                    │
│  ─────────────────              ─────────────────               │
│  Arquivo raiz do agente         Config de editor                │
│  (CLAUDE.md / AGENTS.md /       (.vscode/settings.json,         │
│  copilot-instructions.md)       .editorconfig)                  │
│  Prompts situacionais           Config de linter/formatter      │
│  (*.prompt.md, slash commands)  Config de type-checker          │
│  Skills especializados          Manifest de dependências        │
│  Specs / contratos de domínio   (versões fixas)                 │
└──────────────────────────────────┬──────────────────────────────┘
                                   ▼
                       Agente de codificação
                                   │
┌──────────────────────────────────▼──────────────────────────────┐
│  SENSORES (feedback) — o que verifica o que foi produzido       │
│                                                                  │
│  Rápidos (pre-commit/hook)      CI (por tiers)                  │
│  ─────────────────              ───────────────────────────     │
│  lint + format                  Tier 1: lint + types            │
│  types (quando rápido)          Tier 2: testes + cobertura      │
│  detect-secret                  Tier 3: security scan           │
│  forbidden-pattern greps        Tier 4: fitness functions       │
│                                                                  │
│  Runtime (guardrails)           Estruturais (fitness functions) │
│  ─────────────────              ───────────────────────────     │
│  Gateway único de escrita       Regra de dependência entre      │
│  em filesystem                  camadas                         │
│  Allowlist de shell             Regra de gateway único           │
│  Hook PreToolUse (agente)       Padrões proibidos (grep no CI)  │
│                                                                  │
│  Inferenciais                                                   │
│  ─────────────────                                              │
│  Skill/agente de code-review                                    │
│  Segundo agente avaliador (nunca o mesmo que implementou)        │
└─────────────────────────────────────────────────────────────────┘
```

**Regra de prioridade:** quando um padrão pode ser detectado
deterministicamente, prefira o sensor computacional. Reserve sensores
inferenciais para julgamentos semânticos que o código não consegue capturar.

## Hierarquia de instruções

Quando mais de um agente de codificação trabalha no mesmo repositório (Claude
Code, Copilot, Codex, Cursor), cada um lê seu próprio arquivo de configuração
por convenção de mercado. O risco é duplicar a mesma regra em vários lugares
e eles divergirem silenciosamente.

Padrão recomendado: um **arquivo raiz fino por ferramenta**, que só aponta
para uma única fonte de verdade.

```
CLAUDE.md (raiz)              ──┐
.github/copilot-instructions.md ├──►  AGENTS.md (fonte única de verdade)
.cursor/rules/                ──┘         │
                                           ▼
                                    specs/ (contratos de domínio,
                                    não editados durante implementação)
```

Exemplo mínimo de arquivo raiz fino:

```markdown
# CLAUDE.md

Harness local deste repositório.

## Fonte de verdade

1. `AGENTS.md` (raiz do repo)
2. Specs em `specs/`

Se houver conflito, siga a ordem acima.

## Regras operacionais

- <regra 1, específica e verificável>
- <regra 2>

## Quality gates mínimos

<comandos de lint/types/test do stack>
```

Se houver conflito entre dois arquivos, declare explicitamente a ordem de
precedência — não deixe implícito.

## Tabela de adaptação por stack

Preencha os slots genéricos com a ferramenta concreta do projeto.

| Slot genérico | Python | Node/TypeScript | Swift/iOS | Kotlin/Android | Go |
|---|---|---|---|---|---|
| Lint | `ruff check` | `eslint` | `swiftlint` / `swift format lint` | `ktlint` | `go vet` + `staticcheck` |
| Format | `ruff format` | `prettier` | `swift format` | `ktlint format` | `gofmt` |
| Type check | `mypy` | `tsc --noEmit` | compilador Swift (estático) | compilador Kotlin (estático) | compilador Go (estático) |
| Test runner | `pytest` | `vitest` / `jest` | `XCTest` (`xcodebuild test`) | `JUnit` / `Kotest` (`./gradlew test`) | `go test` |
| Cobertura | `pytest --cov` | `vitest --coverage` | `xccov` / `llvm-cov` | JaCoCo | `go test -cover` |
| Fitness function / regra de arquitetura | teste `ast`-based em `tests/structural/` | `dependency-cruiser` | script de regex sobre `.swift` (Python ou Swift), ou custom rule SwiftLint | Konsist, ou custom rule Detekt | script de `go/ast` ou `go-arch-lint` |
| Security scan | `pip-audit` + grep de secrets | `npm audit` + grep de secrets | `xcodebuild analyze` + grep de secrets, ou Semgrep | `./gradlew dependencyCheckAnalyze`, ou Semgrep | `govulncheck` |
| Sensor rápido (pre-commit) | `pre-commit` (framework Python, funciona em qualquer stack) | `husky` + `lint-staged` | `pre-commit` framework, ou script em `.git/hooks/pre-commit` | `pre-commit` framework, ou plugin Gradle de git hooks | `pre-commit` framework, ou `golangci-lint` no hook |
| Gateway de escrita/shell (runtime) | módulo Python único que resolve e valida todo path/comando (ex. `PathGuard`) | módulo Node único, mesma ideia | um único ponto de acesso a `FileManager`/`Process` — não literal, mas a mesma disciplina arquitetural | um único ponto de acesso a `File`/`ProcessBuilder` | um único ponto de acesso a `os`/`exec` |
| Hook do agente de codificação (PreToolUse) | script stdlib (`json`, `sys`, `re`, `pathlib`) — roda fora do projeto, então não depende do stack alvo | idem — hooks do Claude Code são sempre um comando de shell, então o script de guardrail pode ser Python/Node/shell independentemente da linguagem do projeto sendo editado | idem | idem | idem |

**Observação importante:** o *hook* do agente de codificação (o script que
intercepta `Write`/`Edit`/`Bash` antes de executar) roda como um processo
externo chamado pelo Claude Code — ele não precisa estar na mesma linguagem
do projeto. Um script Python/stdlib funciona como guardrail para um projeto
Swift ou Kotlin sem nenhuma dependência extra, desde que `python3` esteja
disponível na máquina de desenvolvimento (é o caso padrão em macOS/Linux).
Isso é o que torna os hooks em `install-dev-harness/templates/hooks/`
diretamente reutilizáveis em qualquer stack.

## Referências

- Martin Fowler — "Harness Engineering for Coding Agent Users":
  https://martinfowler.com/articles/harness-engineering.html
- Ford, Parsons, Kua — *Building Evolutionary Architectures* (conceito de
  fitness function usado em `architecture-fitness-functions`).
