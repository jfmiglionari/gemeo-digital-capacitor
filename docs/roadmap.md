# Roadmap

O projeto segue sprints com portão (ver [Metodologia](06-metodologia.md)).

| Sprint | Pergunta | Entrega | Validação | Status |
|---|---|---|---|---|
| 0 | Temos os dados de entrada verificados? | Revisão de literatura, motor e capacitor de referência, norma, critério de alerta/falha, esta documentação | — | ✔ 2026-09-24 |
| 1 | A perda de C aparece nas correntes? | Modelo do motor validado + sensibilidade de C = 100% a 85% | V1, V2 | aberta |
| 2 | Uma IA estima C pelas correntes, com ruído e perturbações? | Estimador com machine learning treinado na planta simulada + classificação saudável/alerta/falha ([ADR 0006](adr/0006-estimador-ml.md)) | V3, V4, V5 | — |
| 3 | Dá para mostrar isso de forma clara? | Painel web interativo | — | — |
| 4 | Vale para outro motor? | Motor WEG | V6 | — |
| 5 | Vale na máquina real? | Bancada (futuro) | V7 | — |

## Resultados da Sprint 0
- Lacuna confirmada: o modelo do motor PSC com capacitor existe (Ghial 2014) e a estimação online de capacitância existe em conversores (Ghadrdan 2023; Ribeiro 2025), mas ninguém aplicou ao motor.
- Critério do gêmeo: alerta em −5%, falha em −15% ([ADR 0004](adr/0004-criterio-alerta-falha.md)), com base em Zhao 2021 e IEC 60252-1.
- A tolerância de ±5% dos capacitores de motor obriga o gêmeo a aprender C0 no comissionamento.

## Marcos para comunicação
Cada sprint concluída gera uma atualização pública (LinkedIn), com o resultado e um gráfico:
- Sprint 0: o problema, a lacuna e o critério.
- Sprint 1: "uma queda de 5% em C muda X em Y%".
- Sprint 2: a IA estimando o capacitor pelas correntes.
- Sprint 3: vídeo do painel.
- Sprint 4: o teste na segunda máquina.
