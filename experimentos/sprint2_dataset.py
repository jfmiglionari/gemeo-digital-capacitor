"""Sprint 2: dataset sintético para treinar o estimador de C/C0.

5.000 casos: C/C0 em [0,80; 1,02], V em [207; 253] V (±10%) e temperatura do
cobre em [20; 70] °C. Entradas = só as medições dos sensores; rótulo = C/C0.
Escorregamento fixo (limitação conhecida).
"""

import numpy as np

from gemeo_capacitor.medicao.sensores import medir
from gemeo_capacitor.planta.motor_psc import MotorPSC

N_CASOS = 5000
SEMENTE = 42
T_REF = 20.0  # °C, temperatura em que a Tabela III vale (referência)
ALFA_COBRE = 0.0039  # +0,39% de resistência por °C


def gerar(n=N_CASOS, semente=SEMENTE):
    """Devolve (X, y): X = medições [V, |Im|, |Ia|, defasagem]; y = C/C0."""
    rng = np.random.default_rng(semente)
    motor = MotorPSC()
    c = rng.uniform(0.80, 1.02, n)
    v = rng.uniform(207, 253, n)
    temp = rng.uniform(20, 70, n)
    X = np.empty((n, 4))
    for i in range(n):
        r = motor.resolver(C_F=c[i] * motor.C0_F, V=v[i],
                           fator_resistencia=1 + ALFA_COBRE * (temp[i] - T_REF))
        X[i] = medir(r, v[i], rng)
    return X, c


if __name__ == "__main__":
    X, y = gerar()
    print(X.shape, y.min(), y.max())
