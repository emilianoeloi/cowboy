# SKILL.md — Skill: Conversa Release

## Objetivo

Documentar o fluxo completo de versionamento, tag e release para projetos didáticos (exemplo: Calculadora COBOL), incluindo boas práticas, comandos e checklist para releases públicos.

---

## Quando Usar
- Ao finalizar uma feature relevante e já aprovada via PR
- Antes de publicar uma nova versão para usuários/testadores
- Para garantir rastreabilidade e documentação do que mudou

---

## Fluxo Padrão de Release

1. **Confirme o commit final na branch principal**
   - Exemplo: `git log --oneline -5`
2. **Verifique branch e tags existentes**
   - `git branch --show-current`
   - `git tag --sort=-version:refname | head -10`
3. **Crie uma tag anotada**
   - `git tag -a vX.Y.Z -m "mensagem do release"`
   - Exemplo de mensagem:
     - "feat: adicionar operacao de logaritmo base 10\n\n- Nova opcao 5 no menu: Logaritmo (base 10)\n- FUNCTION LOG10 do GnuCOBOL\n- Validacao de log de zero\n- Banco de 6 citacoes do Asimov no readme-writer.agent.md\n- Demo nos 3 READMEs atualizada"
4. **Publique a tag no repositório remoto**
   - `git push origin vX.Y.Z`
5. **Crie o release no GitHub**
   - Usando GitHub CLI:
     ```bash
     gh release create vX.Y.Z \
       --title "vX.Y.Z - Título do Release" \
       --notes "## O que há de novo\n\n- Lista de features\n- Testes validados\n- Mudanças de documentação\n- Fluxo de agentes executado"
     ```
   - Ou via interface web: https://github.com/<user>/<repo>/releases/new

---

## Checklist de Release
- [x] Commit final revisado e aprovado
- [x] Branch principal atualizada
- [x] Tag criada e publicada
- [x] Release criado com changelog detalhado
- [x] Link do release compartilhado

---

## Boas Práticas
- Use versionamento semântico (ex: v1.2.0)
- Mensagem de tag clara e objetiva
- Release notes com tópicos: features, testes, documentação, fluxo de agentes
- Inclua links para PRs e issues relevantes
- Sincronize READMEs e documentação antes do release

---

## Exemplo Real (Calculadora COBOL)

- Tag: `v1.2.0`
- Release: https://github.com/emilianoeloi/cowboy/releases/tag/v1.2.0
- Features:
  - Logaritmo base 10 (opção 5)
  - Novo prompt `implementar-log.prompt.md`
  - Banco de citações Asimov rotativo
  - Demo e READMEs atualizados
- Testes: log10(100), log10(1000), log10(1), log(0) erro, regressão das 4 operações
- Fluxo: Vibecoder → Reviewer → README Writer

---

## Observações
- Adapte o fluxo para outros projetos didáticos
- Use como referência para onboarding de novos colaboradores
- Atualize este SKILL.md conforme novas práticas forem adotadas
