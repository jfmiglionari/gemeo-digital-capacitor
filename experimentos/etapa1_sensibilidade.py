"""Sprint 1, V2: a perda de C aparece nas correntes?

Varre C de 100% a 85% do nominal, com tensão e escorregamento FIXOS, e mostra
quanto cada grandeza medida varia em relação a C = 100%.

SIMPLIFICAÇÃO: escorregamento fixo (docs/03-modelo-matematico.md, seção 6).
No motor real, quando C cai, o torque muda e a velocidade se ajusta à carga do
ventilador. Aqui isso é ignorado; fica para a Sprint 1 v2.

Rodar:  python experimentos/etapa1_sensibilidade.py
"""

import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
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


RESULTADOS = Path(__file__).resolve().parent.parent / "resultados"


def salvar_csv(var, caminho):
    """Tabela de variações (% ; defasagem em graus) por fração de C."""
    nomes = list(var[1.00])
    with open(caminho, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["C/C0 (%)"] + nomes)
        for k, linha in var.items():
            w.writerow([round(100 * k)] + [round(v, 4) for v in linha.values()])


def plotar(var, caminho):
    """Variação das grandezas vs C/C0, com as linhas de alerta e falha (ADR 0004)."""
    ks = [100 * k for k in var]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.5))
    for g in var[1.00]:
        if g == ANGULO or g == "pf":
            continue
        a1.plot(ks, [var[k][g] for k in var], "o-", label=g)
    a2.plot(ks, [var[k][ANGULO] for k in var], "o-", color="tab:purple")
    for a, tit, yl in ((a1, "Correntes", "variação vs C = 100% (%)"),
                       (a2, "Defasagem Ia-Im", "variação vs C = 100% (graus)")):
        a.axvline(95, color="orange", ls="--", label="alerta (95%)")
        a.axvline(85, color="red", ls="--", label="falha (85%)")
        a.invert_xaxis()
        a.set_xlabel("C / C0 (%)")
        a.set_ylabel(yl)
        a.set_title(tit)
        a.grid(alpha=0.3)
        a.legend(fontsize=8)
    fig.suptitle("Sprint 1: sensibilidade das grandezas medidas à perda de C (V e escorregamento fixos)")
    fig.tight_layout()
    fig.savefig(caminho, dpi=150)


if __name__ == "__main__":
    np.set_printoptions(precision=4)
    tab = varredura()
    var = variacao_pct(tab)
    imprimir(tab, var)
    RESULTADOS.mkdir(exist_ok=True)
    salvar_csv(var, RESULTADOS / "etapa1_sensibilidade.csv")
    plotar(var, RESULTADOS / "etapa1_sensibilidade.png")
