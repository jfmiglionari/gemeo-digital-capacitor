# ADR 0004 — Critério de alerta (−5%) e de falha (−15%)

**Status:** aceito (2026-09-24)

## Contexto
Duas fontes definem o fim de vida do capacitor de filme de forma diferente:
- **Zhao et al. (2021)**, sobre capacitores de filme em conversores eletrônicos: fim de vida quando C/C0 < 95%.
- **IEC 60252-1**, a norma de capacitores para **motores AC**: falha inclui deriva de capacitância que passe **10% além dos limites de tolerância**. Com a tolerância típica de ±5% (datasheet KEMET C87), isso fica em torno de −15% do nominal.

Além disso, a tolerância de ±5% faz com que um capacitor novo possa estar até 5% abaixo ou acima do valor de catálogo.

## Decisão
- **Alerta** quando a capacitância estimada cair **5%** em relação ao valor inicial (C/C0 ≤ 0,95).
- **Falha** quando cair **15%** (C/C0 ≤ 0,85), alinhado à IEC 60252-1.
- **C0 é aprendido no comissionamento** de cada capacitor (valor estimado com o capacitor novo), e não tirado do catálogo.

## Consequências
- O gêmeo avisa com folga antes da falha normativa.
- A meta técnica passa a ser: estimar variações **relativas** de C com resolução bem menor que 5%.
- A Sprint 1 varre C de 100% até 85%.
