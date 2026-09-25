# Gêmeo digital do capacitor de motor monofásico (repositório público)

Projeto do João, estudante de engenharia elétrica. Repositório **público**: vitrine do projeto, candidatura a edital da faculdade (projeto com IA) e base para posts no LinkedIn. A pesquisa e as notas privadas ficam em outro repositório (`digital-twin`, privado).

Responda sempre em **português**, de forma curta e acionável.

## Objetivo

> Construir um gêmeo digital que detecta, **só pelas correntes do motor**, que o capacitor de um motor de ventilador PSC está perdendo capacitância, **antes de ele falhar**.

**Pergunta de foco:** antes de cada tarefa, responda em uma frase "como isto nos aproxima de detectar a perda de C pelas correntes?". Se não houver resposta clara, avise antes de executar.

## Modo de trabalho: aprendizado

- O João **não digita código**, mas **executa e precisa entender** cada passo. O Claude escreve; o João roda.
- Antes de cada passo: explicar em português simples o que será feito e por quê.
- Depois: mostrar o resultado, interpretar e fazer 1 pergunta de verificação. Só avançar quando ele confirmar.
- Passos pequenos. Código comentado em português, citando as equações do artigo (ex.: `# Ghial eq. (51)`).

## Metodologia

Sprints com portão (`docs/06-metodologia.md`). Implemente apenas a sprint aberta no `docs/roadmap.md`. A documentação (`docs/`, `dados/referencia/`, README) também é atualizada pela sessão de arquitetura (Claude no app); **sempre rode `git pull` antes de começar e não reescreva documentos sem necessidade**. Critério do gêmeo: alerta em −5%, falha em −15% (ADR 0004).

## Regras do repositório

- A arquitetura está em `docs/01-arquitetura.md`. Respeitar as camadas e a regra de fronteira: **o gêmeo nunca lê o C verdadeiro da planta** (ADR 0002).
- Todo número de entrada vai para `dados/referencia/` com a fonte. Nada de valor "mágico" no código.
- Decisões de arquitetura novas viram um ADR em `docs/adr/`.
- Ao concluir uma etapa: atualizar `docs/roadmap.md` e, se algo mudou, os documentos afetados.
- **Não versionar PDFs de artigos** (direitos autorais); citar em `docs/referencias.md`.
- Sincronização com o GitHub: commit e push em silêncio sempre que algo relevante mudar; avisar só em caso de erro.
