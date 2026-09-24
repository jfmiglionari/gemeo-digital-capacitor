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
| Norma de capacitores para motores AC (classes de vida útil) | IEC 60252-1 | a pesquisar |
| Datasheet de capacitor de motor (ex.: 2,5–3 µF, 400–450 V AC) com vida útil e tolerância | fabricantes | a pesquisar |

## 4. Sensores

Para a camada de medição simulada: precisão, resolução e taxa de amostragem de sensores baratos.
- Referência inicial: o sensor de corrente SCT-013-030 e o ADC ADS1115 usados por Shukla et al. (2025).
- **A fazer:** registrar a precisão de datasheet desses componentes.
