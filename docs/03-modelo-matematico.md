# Modelo matemático

Base: Ghial, Saini & Saini (2014). Modelo em regime permanente pela teoria dos campos girantes duplos (double-revolving-field): o campo pulsante de cada enrolamento é decomposto em um campo que gira para frente (forward) e outro para trás (backward).

## 1. Capacitor não ideal

O capacitor fica em série com o enrolamento auxiliar e é modelado como uma resistência série Rc (perdas, ESR) mais a reatância capacitiva:

$$Z_c = R_c - jX_c, \qquad X_c = \frac{1}{2\pi f C}$$

**É aqui que a degradação entra no modelo:** perder capacitância aumenta Xc; o aumento da resistência série aumenta Rc.

## 2. Impedâncias de avanço e retrocesso

Para o enrolamento principal (eqs. 10–11), com Xmm a reatância de magnetização:

$$Z_{fm} = \frac{1}{2}\,\frac{jX_{mm}\left(\frac{R_r}{S_f} + jX_r\right)}{\frac{R_r}{S_f} + j(X_r + X_{mm})}, \qquad Z_{bm} = \frac{1}{2}\,\frac{jX_{mm}\left(\frac{R_r}{S_b} + jX_r\right)}{\frac{R_r}{S_b} + j(X_r + X_{mm})}$$

com $S_b = 2 - S_f$. O auxiliar tem expressões análogas (eqs. 21–22).

## 3. Equações acopladas dos dois enrolamentos

Com a razão de transformação complexa *a* (CCVR, eq. 33), os dois enrolamentos formam um sistema 2×2 (eqs. 45–50):

$$\bar I_m Z_{11} + \bar I_a Z_{12} = V_m, \qquad \bar I_m Z_{21} + \bar I_a Z_{22} = V_a$$

$$Z_{11} = Z_{sm} + Z_{fm} + Z_{bm}, \quad Z_{12} = -ja(Z_{fm} - Z_{bm}), \quad Z_{21} = ja(Z_{fm} - Z_{bm})$$

$$Z_{22} = Z^*_{sa} + \mathbf{Z_c} + a^2(Z_{fm} + Z_{bm})$$

**O capacitor só aparece em Z22.** Uma mudança em C altera Z22, que altera as duas correntes (o sistema é acoplado), a defasagem entre elas, a corrente de linha, a potência e o fator de potência.

## 4. Saídas

Correntes (eqs. 51–52), potência e fator de potência (eqs. 53–55):

$$\bar I_m = \frac{V_m(Z_{22} - Z_{12})}{Z_{11}Z_{22} - Z_{12}Z_{21}}, \qquad \bar I_a = \frac{V_a(Z_{11} - Z_{21})}{Z_{11}Z_{22} - Z_{12}Z_{21}}$$

## 5. Problema inverso (o gêmeo)

O artigo resolve o **problema direto**: dados os parâmetros (incluindo C), calcula as correntes. O gêmeo resolve o **problema inverso**: dadas as correntes medidas, encontra C.

Formulação inicial: encontrar C e Rc que minimizam a diferença entre as correntes previstas pelo modelo e as medidas:

$$\min_{C,\,R_c}\; \left|\bar I_m^{\text{med}} - \bar I_m(C, R_c)\right|^2 + \left|\bar I_a^{\text{med}} - \bar I_a(C, R_c)\right|^2$$

Na etapa 2 isso vira um estimador recursivo (RLS ou EKF) que acompanha C ao longo do tempo.

## 6. Simplificações conhecidas

| Simplificação | Consequência | Quando tratar |
|---|---|---|
| Regime permanente senoidal | Não modela partida nem transitórios | Se necessário, modelo dinâmico d-q |
| Escorregamento fixo na etapa 1 | Na realidade o motor muda de velocidade para manter o torque da carga | Etapa 1 v2: resolver o equilíbrio torque motor = torque carga |
| Parâmetros constantes com a temperatura | A resistência do cobre varia ~0,4%/°C e pode mascarar a variação de C | Etapa 2 (robustez) |
| Sem saturação magnética | Erro em tensões acima da nominal | Avaliar na validação |
