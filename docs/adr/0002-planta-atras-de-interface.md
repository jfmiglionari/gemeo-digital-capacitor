# ADR 0002 — A planta fica atrás de uma interface, e o gêmeo nunca lê o C verdadeiro

**Status:** aceito (2026-09-24)

## Contexto
Na fase 1 a "máquina real" é um simulador que conhece o valor verdadeiro de C. Se o gêmeo tiver acesso a esse valor, mesmo sem querer, os resultados ficam artificialmente bons. Além disso, o projeto quer trocar a planta simulada por uma bancada física no futuro.

## Decisão
- A planta implementa a interface `Planta`, que só expõe **amostras de sinais medidos** (tensão, corrente principal, corrente auxiliar).
- O gêmeo (modelo + estimador) recebe dados apenas da camada de medição.
- O valor verdadeiro de C fica restrito à planta simulada e aos scripts de avaliação, que o usam só para calcular o erro do gêmeo.

## Consequências
- Resultados honestos: o gêmeo trabalha nas mesmas condições que teria numa máquina real.
- A troca por bancada exige apenas uma nova implementação de `Planta`.
- A camada de medição precisa modelar sensores de forma realista (ruído, resolução, taxa de amostragem).
