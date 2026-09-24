# Modelo de falhas do capacitor

## Tipos de capacitor e modos de falha

| | Capacitor permanente (PSC) | Capacitor de partida |
|---|---|---|
| Tecnologia | Filme de polipropileno metalizado | Eletrolítico AC |
| Modo de falha dominante | Desgaste: perda gradual de capacitância | Falha brusca por calor e excesso de partidas |
| Previsível? | Sim | Pouco |
| No escopo? | **Sim** | Não |

## Mecanismo físico (filme metalizado)

Quando um ponto fraco do dielétrico sofre ruptura, a camada metálica em volta evapora e isola o defeito: é a **autocura (self-healing)**. O capacitor continua funcionando, mas perde um pouco de área de eletrodo, e a capacitância cai um pouco a cada evento. Com o acúmulo de eventos, C cai até o fim de vida (Wang & Blaabjerg, 2014). Tensão alta e harmônicos aceleram a perda (Li et al., 2024).

## Critério de fim de vida

| Tipo | Critério | Fonte |
|---|---|---|
| Filme metalizado (MPPF) | **C/C0 < 95%** | Zhao et al. 2021, Tabela I |
| Eletrolítico de alumínio | C/C0 < 80% ou ESR/ESR0 > 2 | Zhao et al. 2021, Tabela I |

## Modelo de vida útil

Modelo empírico mais usado (Wang & Blaabjerg, 2014, eq. 1):

$$L = L_0 \left(\frac{V}{V_0}\right)^{-n} \exp\left[\frac{E_a}{k_B}\left(\frac{1}{T} - \frac{1}{T_0}\right)\right]$$

- L, L0: vida útil nas condições de uso e nas condições de referência
- V, V0: tensão de uso e de referência; n: expoente de tensão
- T, T0: temperatura de uso e de referência (K); Ea: energia de ativação; kB: constante de Boltzmann

## Cenários de degradação para a simulação

| Cenário | C(t) | Uso |
|---|---|---|
| Degraus | C = 100%, 99%, 98%, 97%, 95%, 90% | Etapa 1: sensibilidade |
| Linear | C cai a taxa constante até 95% | Etapa 2: rastreamento |
| "Lenta → rápida" | Perda que acelera no fim da vida, como observado por Li et al. (2024) | Etapa 2: antecedência do alerta |
| Com perturbações | Qualquer um dos anteriores + variação de carga, de tensão da rede e de temperatura | Etapa 2: robustez |

**A pesquisar:** norma IEC 60252-1 (capacitores para motores AC) e datasheets de fabricantes, para vida útil nominal e tolerância de capacitância de capacitores de motor reais.
