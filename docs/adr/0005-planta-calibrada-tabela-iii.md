# ADR 0005: Planta calibrada com as impedâncias da Tabela III do Ghial

**Status:** proposto (2026-09-28), para a revisão da Sprint 1

## Contexto
A V1 pede que o modelo reproduza o motor 1 do Ghial (2014). Refazer a extração de parâmetros do artigo (eqs. 1–33) a partir dos ensaios publicados dá IL = 0,11 A, contra 0,312 A medidos. A Tabela III do artigo tem valores intermediários que não seguem das próprias equações (detalhes em [Fontes de dados](../02-fontes-de-dados.md)). Já as impedâncias finais Z11, Z12, Z21 e Z22 da tabela, nas eqs. (51)–(55), reproduzem a medição com erro de 3–6%.

## Decisão
- A planta usa Z11, Z12 e Z21 da Tabela III como estão.
- De Z22 subtrai-se o capacitor nominal (Zc0 = 6,7 − j1162,6 Ω). O resto, Z22_sem_capacitor, é fixo.
- O capacitor volta como entrada: Z22 = Z22_sem_capacitor + Rc − jXc0·C0/C.
- Escorregamento fixo, o do ponto da tabela.

## Consequências
- C continua entrando só em Z22, como no modelo do artigo.
- A planta não depende da cadeia de extração, que não conseguimos reproduzir.
- Não dá para mudar parâmetros internos (Rr, Xmm, escorregamento) separadamente. Para a Sprint 1 v2 (equilíbrio de torque) e para o motor WEG, será preciso reconstruir o circuito completo. Isso fica para quando a etapa chegar.
- Tolerância da V1: 6% em IL e Pin, ±0,01 em pf.
