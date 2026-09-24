# ADR 0001 — Python como linguagem única

**Status:** aceito (2026-09-24)

## Contexto
O projeto tem três etapas técnicas: simulação do motor, estimador online e painel web. A alternativa natural na engenharia elétrica seria MATLAB/Simulink.

## Decisão
Usar **Python** em todas as etapas (NumPy, SciPy, Matplotlib; biblioteca de painel web a definir na etapa 3).

## Consequências
- Gratuito e aberto: qualquer pessoa pode reproduzir os resultados a partir do repositório público.
- Uma linguagem só da simulação ao painel.
- Perde-se o ambiente gráfico do Simulink; os modelos ficam em código, o que por outro lado facilita versionar e testar.
