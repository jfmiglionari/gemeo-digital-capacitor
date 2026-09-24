# Visão geral

## Objetivo

Construir um gêmeo digital que detecta, **só pelas correntes do motor**, que o capacitor de um motor de ventilador PSC está perdendo capacitância, **antes de ele falhar**.

### Pergunta de foco

Toda tarefa do projeto precisa responder: *"como isto nos aproxima de detectar a perda de capacitância pelas correntes?"*. Se não responder, está fora do escopo.

## O problema

Um motor PSC (permanent split capacitor) tem dois enrolamentos: o principal, ligado direto à rede, e o auxiliar, ligado à rede através de um capacitor. O capacitor defasa a corrente do auxiliar em relação à do principal e cria o campo girante que faz o motor funcionar. Se a capacitância cai, a defasagem muda, o torque cai, a corrente sobe e o motor esquenta, até queimar ou não partir.

O capacitor de filme perde capacitância aos poucos (autocura do dielétrico), e o fim de vida é tipicamente definido como **C/C0 < 95%**. A pergunta do projeto é se essa perda de poucos por cento pode ser estimada de fora, sem desmontar nada, só medindo tensão e correntes.

## Escopo

**Dentro:**
- Motor de indução monofásico **PSC** (capacitor permanente de filme).
- Degradação **gradual** da capacitância (e da resistência série do capacitor).
- Sinais: tensão da rede, corrente do enrolamento principal, corrente do enrolamento auxiliar (e, se necessário, velocidade).
- Fase 1: **simulação**, com a planta física substituída por um modelo validado contra dados publicados.
- Entrega: painel web interativo.

**Fora (por enquanto):**
- Capacitor de partida (eletrolítico), que falha de forma brusca.
- Falhas de rolamento, estator e rotor.
- Motores trifásicos e PMSM.
- Transformadores.
- Bancada física (possível fase futura; a arquitetura já prevê a troca).

## Estratégia em etapas

1. **Viabilidade:** simular o motor e medir quanto as correntes mudam quando C cai 1%, 3%, 5% e 10%.
2. **Estimador:** algoritmo que recebe as correntes e devolve C estimado, robusto a ruído, carga e tensão.
3. **Painel:** interface em que o usuário "envelhece" o capacitor e vê o gêmeo detectar.
4. **Segunda máquina:** repetir com outro motor (WEG) para ver se o resultado se generaliza.
5. **(Futuro) Bancada:** motor real com capacitores de valores diferentes.
