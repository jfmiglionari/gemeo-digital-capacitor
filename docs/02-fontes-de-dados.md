# Fontes de dados

Todo número usado na simulação precisa ter origem conhecida. Este documento registra de onde vem cada conjunto de dados e o que falta.

## 1. Motor de referência: Ghial et al. (2014), motor 1

Fonte: Ghial, Saini & Saini, *IEEE Transactions on Industrial Electronics*, 61(2), 2014, seção VI (estudo de caso).

Motor de ventilador PSC, 4 polos, 220–240 V, 70 W, 50 Hz, 1400 rpm.

| Grandeza | Valor | Origem no artigo |
|---|---|---|
| Rsm (resistência CC, principal) | 177,0785 Ω | ensaio CC |
| Rsa (resistência CC, auxiliar) | 177,0785 Ω | ensaio CC (ver observação) |
| Rs | 88,5392 Ω | ensaio CC |
| VNL, INL, PNL | 240 V; 0,238 A; 57 W | ensaio em vazio |
| VLR, ILR, PLR | 174,4 V; 0,3040 A; 51 W | ensaio de rotor bloqueado |
| RLR, XLR, ZLR | 551,8525 Ω; 156,7559 Ω; 573,6842 Ω | eqs. (1)–(3) |
| Sf, Sb | 0,0591; 1,9409 | escorregamentos de avanço e retrocesso |
| **C** | **2,63 µF** | medido com medidor LCR |
| **Rc** | **6,7 Ω** | medido com medidor LCR |
| Xc, Zc | 1162,6 Ω; 6,7 − j1162,6 Ω | calculados |
| Medido em operação | V = 230 V; IL = 0,312 A; Pin = 70 W; pf = 1,00 | analisador Fluke 43B |

**Por que este motor:** é o único caso no corpus com todos os parâmetros do circuito equivalente **e** medições em operação para validar o modelo.

**Observações a verificar:**
1. Rsm e Rsa aparecem com o mesmo valor, o que é incomum (os enrolamentos costumam ser diferentes).
2. A eq. (53) define a corrente de linha como a parte real de Im + Ia, e não o módulo.
3. Fator de potência medido igual a 1,00.

Esses pontos são tratados na etapa 1 e o que for decidido fica registrado aqui.

**Decisões da Sprint 1:**

| # | Observação | Escolha | Por quê |
|---|---|---|---|
| 1 | Rsm = Rsa | Mantido como está | 177,0785 = 2 × 88,5392 (Rs): parece que o artigo mediu os dois enrolamentos em paralelo e dividiu igualmente, e não mediu cada um. Não temos como corrigir. Como a planta usa as impedâncias da Tabela III (abaixo), o valor já está embutido nelas. |
| 2 | IL = Re[Im + Ia] (eq. 53) | IL = \|Im + Ia\| | O Fluke 43B mede o valor eficaz, que é o módulo. Com Re[·], a eq. (54) (Pin = V·IL·cosθ) contaria o cosθ duas vezes. Usamos Pin = Re(V·I*) e pf = cos(ângulo de I). Com pf ≈ 1 a diferença é de 0,4%. |
| 3 | pf = 1,00 medido | Aceito, com tolerância de ±0,01 | O analisador mostra 2 casas. O modelo dá 0,996, que se arredonda para 1,00. Quer dizer que, no ponto de operação, o capacitor quase compensa a parte indutiva do motor. |
| 4 | Xc = 1162,6 Ω, mas 1/(2π·50·2,63 µF) = 1210 Ω | Usar 1162,6 Ω (valor do artigo) como Xc0 | É o valor que o artigo usou nas contas. Para variar C, escalamos Xc = Xc0·C0/C. A escolha afeta a sensibilidade em cerca de 4% relativo (por ex., 3,0% contra 3,1%), não a conclusão. |

**Reprodução do artigo (V1):** a cadeia de extração de parâmetros (eqs. 1–33) **não se reproduz** a partir dos dados publicados. A Tabela III tem valores que não seguem das próprias equações:
- Vab1 foi calculado com 230 V, e não com VNL = 240 V;
- na eq. (19), Xc entra com sinal negativo (−Xc), e com ≈ 1153 Ω;
- o ramo de avanço usa Sf = 1/15 (1400 de 1500 rpm), e não 0,0591;
- Zinsm ≠ Z11 na parte imaginária;
- Eac, Emc e Z22 não saem das eqs. (28)–(31) e (50).

Seguindo as equações ao pé da letra, IL dá 0,11 A (medido: 0,312 A). Já as **impedâncias finais Z11, Z12, Z21 e Z22 da Tabela III**, aplicadas às eqs. (51)–(55), reproduzem a medição: IL +3,5%, Pin +5,7% e pf 0,996. Por isso a planta usa essas impedâncias ([ADR 0005](adr/0005-planta-calibrada-tabela-iii.md)). Os valores estão em `motor_ghial_2014.json`, em `tabela_III_metodo_proposto`.

## 2. Segunda máquina: motor comercial WEG (a pesquisar)

Objetivo: testar se o resultado da etapa 1 vale para outro motor.

- **O que um catálogo/datasheet costuma trazer:** potência, tensão, frequência, polos, corrente nominal, rotação, rendimento, fator de potência e, em motores com capacitor, o valor do capacitor.
- **O que costuma faltar:** as resistências e reatâncias do circuito equivalente, que o modelo precisa.
- **Como resolver:** ajustar os parâmetros do circuito equivalente para reproduzir o ponto nominal do datasheet (corrente, potência, fator de potência, rotação), usando os valores do motor do Ghial como ponto de partida. Nguyen et al. (2024) fazem um ajuste parecido com o método de Nelder–Mead. Essa decisão vira um ADR quando a etapa começar.
- **A fazer:** escolher um motor PSC do catálogo WEG com potência próxima (ventilador/exaustor) e salvar o datasheet em `dados/referencia/`.

## 3. Capacitor

| Informação | Fonte | Status |
|---|---|---|
| Valor nominal e resistência série do motor 1 | Ghial 2014 | ✔ |
| Critério de fim de vida do capacitor de filme: C/C0 < 95% | Zhao et al. 2021, Tabela I | ✔ |
| Mecanismo de degradação (autocura) e modelo de vida em função de tensão e temperatura | Wang & Blaabjerg 2014 | ✔ |
| Forma da curva de perda de capacitância no tempo | Li et al. 2024 (filme sob tensão CC + harmônicos) | ✔ parcial: é capacitor de alta tensão, não de motor |
| Classes de vida (A/B/C/D = 30.000/10.000/3.000/1.000 h), taxa de falha ≤ 3% e **definição de falha** (deriva de C 10% além da tolerância) | IEC 60252-1 ed. 2.1, seção 3 | ✔ |
| Capacitor de motor real: ±5%, classe A 30.000 h a 420 VAC, tan δ = 0,002 (20 °C, 50 Hz), −25 a +85 °C, disponível em 2,5 e 3 µF / 450 V | KEMET C87 (datasheet F3063_C87) | ✔ |
| Capacitor típico de ventilador (CBB61): ±5% ou ±10%, tan δ ≤ 0,003 (1 kHz); sem classe de vida | WEE Technology CBB61 | ✔ complementar |

Dados estruturados em `dados/referencia/capacitor_kemet_c87.json`. Critério de alerta e falha: [ADR 0004](adr/0004-criterio-alerta-falha.md).

## 4. Sensores

Para a camada de medição simulada: precisão, resolução e taxa de amostragem de sensores baratos.
- Referência inicial: o sensor de corrente SCT-013-030 e o ADC ADS1115 usados por Shukla et al. (2025).
- **A fazer:** registrar a precisão de datasheet desses componentes.
