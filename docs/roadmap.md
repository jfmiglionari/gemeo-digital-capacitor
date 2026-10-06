# Roadmap

O projeto segue sprints com portão (ver [Metodologia](06-metodologia.md)).

| Sprint | Pergunta | Entrega | Validação | Status |
|---|---|---|---|---|
| 0 | Temos os dados de entrada verificados? | Revisão de literatura, motor e capacitor de referência, norma, critério de alerta/falha, esta documentação | — | ✔ 2026-09-24 |
| 1 | A perda de C aparece nas correntes? | Modelo do motor validado + sensibilidade de C = 100% a 85% | V1, V2 | ✔ 2026-10-05 |
| 2 | Uma IA estima C pelas correntes, com ruído e perturbações? | Estimador com machine learning treinado na planta simulada + classificação saudável/alerta/falha ([ADR 0006](adr/0006-estimador-ml.md)) | V3, V4, V5 | versão mínima ✔ 2026-10-05 |
| 3 | Dá para mostrar isso de forma clara? | Painel web interativo | — | — |
| 4 | Vale para outro motor? | Motor WEG | V6 | — |
| 5 | Vale na máquina real? | Bancada (futuro) | V7 | — |

## Resultados da Sprint 0
- Lacuna confirmada: o modelo do motor PSC com capacitor existe (Ghial 2014) e a estimação online de capacitância existe em conversores (Ghadrdan 2023; Ribeiro 2025), mas ninguém aplicou ao motor.
- Critério do gêmeo: alerta em −5%, falha em −15% ([ADR 0004](adr/0004-criterio-alerta-falha.md)), com base em Zhao 2021 e IEC 60252-1.
- A tolerância de ±5% dos capacitores de motor obriga o gêmeo a aprender C0 no comissionamento.

## Resultados da Sprint 1 (portão fechado em 2026-10-05)
- Uma queda de 5% em C muda |Im| (corrente do enrolamento principal) em −4,15%; |Ia| −2,11%, IL −2,81%, defasagem Ia-Im +2,83°. Em −15%: |Im| −12,5%, defasagem +9,9°.
- Simplificação: tensão e escorregamento fixos. Dados em `resultados/etapa1_sensibilidade.csv` e `.png`.
- Leitura da revisão: a variação é monotônica e quase linear, e a defasagem entre Ia e Im não depende da amplitude da tensão no modelo linear, o que a torna a melhor candidata a atributo. Mas a tensão da rede (±10%) muda as correntes mais do que a perda de C de 5%; por isso a Sprint 2 precisa de um estimador que combine vários atributos.

## Resultados da Sprint 2, versão mínima (2026-10-05)
- Estimador: floresta aleatória (scikit-learn, 200 árvores) com entradas V, |Im|, |Ia| e defasagem Ia-Im, treinada em 4.000 motores simulados e testada em 1.000 nunca vistos. C/C0 entre 80% e 102%, tensão ±10%, cobre de 20 a 70 °C, ruído de sensor de 1% (amplitude) e 0,5° (ângulo).
- **Erro médio de 0,70 ponto percentual** na capacitância estimada; **acurácia de 92,7%** em saudável / alerta / falha; **alarme falso de 4,7%**; nenhum capacitor em falha classificado como saudável.
- Linha de base com só |Im|: erro médio de 4,87 pontos, acurácia de 49,9%, alarme falso de 57%. Combinar as medições é o que separa o efeito do capacitor do efeito da tensão e da temperatura.
- Pendente para fechar a sprint: variação de carga (escorregamento), redução do alarme falso (ex.: média de várias leituras no tempo) e comparação com RLS/EKF.

## Marcos para comunicação
Cada sprint concluída gera uma atualização pública (LinkedIn), com o resultado e um gráfico:
- Sprint 0: o problema, a lacuna e o critério.
- Sprint 1: "uma queda de 5% em C muda X em Y%".
- Sprint 2: a IA estimando o capacitor pelas correntes.
- Sprint 3: vídeo do painel.
- Sprint 4: o teste na segunda máquina.
