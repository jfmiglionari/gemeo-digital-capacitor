"""Sprint 1, V2: a perda de C aparece nas correntes?

Varre C de 100% a 85% do nominal, com tensão e escorregamento FIXOS, e mostra
quanto cada grandeza medida varia em relação a C = 100%.

SIMPLIFICAÇÃO: escorregamento fixo (docs/03-modelo-matematico.md, seção 6).
No motor real, quando C cai, o torque muda e a velocidade se ajusta à carga do
ventilador. Aqui isso é ignorado; fica para a Sprint 1 v2.

Rodar:  python experimentos/etapa1_sensibilidade.py
"""

import numpy as np

from gemeo_capacitor.planta.motor_psc import MotorPSC

# Pontos da varredura (fração de C0). 95% = alerta e 85% = falha (ADR 0004).
FRACOES_C = [1.00, 0.99, 0.98, 0.97, 0.95, 0.90, 0.85]


def grandezas(r):
    """O que um sensor de corrente (e de tensão, para a fase) consegue medir."""
    return {
        "|Im| (A)": abs(r.Im),
        "|Ia| (A)": abs(r.Ia),
        "defasagem Ia-Im (graus)": r.defasagem_graus,
        "IL (A)": r.IL,
        "pf": r.pf,
    }


def varredura(motor=None):
    """Devolve {fração de C: {grandeza: valor}}."""
    motor = motor or MotorPSC()
    return {k: grandezas(motor.resolver(C_F=k * motor.C0_F)) for k in FRACOES_C}


ANGULO = "defasagem Ia-Im (graus)"


def variacao_pct(tabela):
    """Variação em relação a C = 100%: em % para correntes e pf.

    Para a defasagem, a variação é em GRAUS: como o ângulo de referência é
    pequeno (cerca de −10°), uma porcentagem sobre ele exageraria o efeito.
    """
    ref = tabela[1.00]
    return {
        k: {
            g: (v - ref[g]) if g == ANGULO else 100 * (v - ref[g]) / ref[g]
            for g, v in linha.items()
        }
        for k, linha in tabela.items()
    }


def imprimir(tabela, var):
    nomes = list(tabela[1.00])
    print("Valores absolutos (V = 230 V, escorregamento fixo)")
    print(f"{'C/C0':>6} " + " ".join(f"{n:>24}" for n in nomes))
    for k, linha in tabela.items():
        print(f"{k:>6.0%} " + " ".join(f"{v:>24.4f}" for v in linha.values()))

    print("\nVariação em relação a C = 100% (% ; defasagem em graus)")
    print(f"{'C/C0':>6} " + " ".join(f"{n:>24}" for n in nomes))
    for k, linha in var.items():
        marca = {0.95: "  ← alerta", 0.85: "  ← falha"}.get(k, "")
        print(f"{k:>6.0%} " + " ".join(f"{v:>+24.2f}" for v in linha.values()) + marca)


if __name__ == "__main__":
    np.set_printoptions(precision=4)
    tab = varredura()
    imprimir(tab, variacao_pct(tab))
