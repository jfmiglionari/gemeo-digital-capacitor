# Metodologia: sprints com portão

O projeto avança em **sprints**. Cada sprint tem objetivo, entradas, entregas e um **critério de pronto**. A sprint seguinte só começa quando **todos** os itens do critério de pronto da atual estiverem cumpridos (portão). Isso evita construir sobre dados não verificados.

## Papéis

| Papel | Quem | Responsabilidade |
|---|---|---|
| Dono do produto | João | Define prioridades, pesquisa as entradas (artigos, datasheets, normas), aprova decisões, executa o desenvolvimento |
| Arquiteto e revisor | Claude (conversa) | Verifica cada entrada antes de liberar a sprint, registra decisões (ADRs), escreve a especificação da sprint e revisa o resultado |
| Desenvolvedor | Claude Code (VS Code) | Implementa a especificação da sprint neste repositório, em passos pequenos, explicando cada um |

Se uma entrada não for encontrada, a rota é redefinida em conjunto e registrada; o portão não é pulado.

## Sprints

| Sprint | Pergunta | Critério de pronto | Validações | Status |
|---|---|---|---|---|
| 0 — Fundamentos | Temos todos os dados de entrada com fonte verificada? | Lacuna confirmada; motor de referência; datasheet de capacitor; norma; critério de alerta e falha decidido | — | ✔ 2026-09-24 |
| 1 — Modelo e sensibilidade | A perda de C aparece nas correntes? | Modelo reproduz o artigo de referência; sensibilidade de C = 100% a 85%; resultado em uma frase | V1, V2 | aberta |
| 2 — Estimador | Dá para estimar C online, com ruído e perturbações? | Estimador + camada de saúde; alerta em −5% sem alarmes falsos | V3, V4, V5 | — |
| 3 — Painel | Dá para mostrar isso de forma clara? | Painel web interativo | — | — |
| 4 — Segunda máquina | Vale para outro motor? | Mesmas conclusões com um motor WEG | V6 | — |
| 5 — Bancada (futuro) | Vale na máquina real? | Erro de C dentro do obtido em V4 | V7 | — |

Validações definidas em [Plano de validação](05-plano-de-validacao.md).
