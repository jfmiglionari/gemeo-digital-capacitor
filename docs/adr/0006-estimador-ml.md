# ADR 0006 — Estimador de C por machine learning (Sprint 2)

**Status:** aceito (2026-09-28)

## Contexto
O projeto precisa de um componente de inteligência artificial treinado, simples e honesto. A Sprint 2 previa um estimador clássico (RLS/EKF).

## Decisão
- A Sprint 2 passa a ser **"Estimador com ML"**: um modelo do scikit-learn (floresta aleatória ou rede neural pequena) que recebe as grandezas medidas (|Im|, |Ia|, defasagem entre elas, tensão) e devolve C/C0.
- Os dados de treino vêm da **planta simulada validada** (Sprint 1), com C de 100% a 85% e variações de tensão, carga, temperatura e ruído de sensor.
- A saída classifica o capacitor em saudável / alerta / falha (ADR 0004).
- RLS/EKF fica como comparação opcional, depois.

## Consequências
- O valor da IA está em **separar o efeito de C do efeito de tensão, carga e temperatura**; sem essas variações, o problema seria uma fórmula e o ML não se justificaria.
- O rótulo (C verdadeiro) só é usado no treino e na avaliação; na inferência, o modelo recebe apenas medições (ADR 0002).
- Nova dependência: scikit-learn.
- Limite honesto: treinado em simulação; a validação em máquina real fica para a bancada.
