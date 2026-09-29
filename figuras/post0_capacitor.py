"""Imagem do post 0 do LinkedIn: o motor PSC e a vida do capacitor.

Gera figuras/post0_capacitor.png (1200 x 1200 px). Rodar da raiz do repositório:
    python figuras/post0_capacitor.py
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, Rectangle

RAIZ = Path(__file__).resolve().parent.parent

# Tensão da rede: motor de referência (Ghial et al., 2014) em dados/referencia/
with open(RAIZ / "dados" / "referencia" / "motor_ghial_2014.json") as f:
    motor = json.load(f)


V_REDE = motor["medido_em_operacao"]["V_V"]  # 230 V, ponto de operação do V1

# Critérios do gêmeo: ADR 0004 (alerta C/C0 <= 0,95; falha C/C0 <= 0,85, IEC 60252-1)
C_NOVO = 100
C_ALERTA = 95
C_FALHA = 85

# Paleta Okabe-Ito (segura para daltonismo): só 3 cores além do preto/cinza
VERDE = "#009E73"
AMBAR = "#E69F00"
VERMELHO = "#D55E00"
CINZA = "#6B6B6B"
PRETO = "#1A1A1A"

# 12 x 12 polegadas a 100 dpi = 1200 x 1200 px; 1 pt = 1,39 px, então 16 pt ~ 22 px
fig = plt.figure(figsize=(12, 12), dpi=100, facecolor="white")
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, 12)
ax.set_ylim(0, 12)
ax.axis("off")

LW = 3.5  # espessura dos fios
fio = dict(color=PRETO, lw=LW, solid_capstyle="round")

# ---------- Título e rodapé ----------
ax.text(6, 11.15, "O capacitor avisa antes de falhar", ha="center", va="center",
        fontsize=36, fontweight="bold", color=PRETO)
ax.text(6, 0.45, "github.com/jfmiglionari/gemeo-digital-capacitor", ha="center",
        va="center", fontsize=16, color=CINZA)


# ---------- ESQUERDA: esquemático do motor PSC ----------
def bobina(x, y_topo, y_base, voltas=4):
    """Enrolamento: semicírculos empilhados na vertical."""
    passo = (y_topo - y_base) / voltas
    r = passo / 2
    for i in range(voltas):
        yc = y_topo - r - i * passo
        ax.add_patch(Arc((x, yc), 2 * r, 2 * r, theta1=-90, theta2=90,
                         color=PRETO, lw=LW))


X_FONTE, X_R1, X_R2 = 1.0, 2.3, 4.8  # posições da fonte e dos dois ramos
Y_SUP, Y_INF = 9.2, 4.2              # barramentos superior e inferior

# fonte AC
R_FONTE = 0.55
Y_FONTE = (Y_SUP + Y_INF) / 2
ax.add_patch(Circle((X_FONTE, Y_FONTE), R_FONTE, fill=False, color=PRETO, lw=LW))
t = np.linspace(-np.pi, np.pi, 100)
ax.plot(X_FONTE + 0.3 * t / np.pi, Y_FONTE + 0.15 * np.sin(t), color=PRETO, lw=3)
ax.plot([X_FONTE, X_FONTE], [Y_FONTE + R_FONTE, Y_SUP], **fio)
ax.plot([X_FONTE, X_FONTE], [Y_INF, Y_FONTE - R_FONTE], **fio)
ax.text(X_FONTE, Y_INF - 0.55, f"rede\n{V_REDE:.0f} V", ha="center", va="top",
        fontsize=20, color=PRETO, linespacing=1.2)

# barramentos (ramos em paralelo)
ax.plot([X_FONTE, X_R2], [Y_SUP, Y_SUP], **fio)
ax.plot([X_FONTE, X_R2], [Y_INF, Y_INF], **fio)
for x in (X_R1, X_R2):
    ax.plot(x, Y_SUP, "o", color=PRETO, ms=10)
    ax.plot(x, Y_INF, "o", color=PRETO, ms=10)

Y_BOB_TOPO, Y_BOB_BASE = 6.9, 4.9

# ramo 1: enrolamento principal
ax.plot([X_R1, X_R1], [Y_SUP, Y_BOB_TOPO], **fio)
bobina(X_R1, Y_BOB_TOPO, Y_BOB_BASE)
ax.plot([X_R1, X_R1], [Y_BOB_BASE, Y_INF], **fio)
ax.text(X_R1 + 0.45, (Y_BOB_TOPO + Y_BOB_BASE) / 2, "enrolamento\nprincipal",
        ha="left", va="center", fontsize=18, color=PRETO, linespacing=1.2)

# ramo 2: capacitor (destacado) em série com o enrolamento auxiliar
Y_CAP = 8.05
GAP, LARG = 0.14, 0.5
ax.plot([X_R2, X_R2], [Y_SUP, Y_CAP + GAP], **fio)
ax.plot([X_R2 - LARG, X_R2 + LARG], [Y_CAP + GAP] * 2, color=VERDE, lw=7,
        solid_capstyle="butt")
ax.plot([X_R2 - LARG, X_R2 + LARG], [Y_CAP - GAP] * 2, color=VERDE, lw=7,
        solid_capstyle="butt")
ax.text(X_R2 - LARG - 0.2, Y_CAP, "capacitor", ha="right", va="center",
        fontsize=20, fontweight="bold", color=VERDE)
ax.plot([X_R2, X_R2], [Y_CAP - GAP, Y_BOB_TOPO], **fio)
bobina(X_R2, Y_BOB_TOPO, Y_BOB_BASE)
ax.plot([X_R2, X_R2], [Y_BOB_BASE, Y_INF], **fio)
ax.text(X_R2 + 0.45, (Y_BOB_TOPO + Y_BOB_BASE) / 2, "enrolamento\nauxiliar",
        ha="left", va="center", fontsize=18, color=PRETO, linespacing=1.2)

# legenda do papel do capacitor
ax.text((X_FONTE + X_R2) / 2 + 0.4, 2.55, "o capacitor atrasa a corrente\ndo auxiliar → o eixo gira",
        ha="center", va="center", fontsize=19, color=PRETO, linespacing=1.3)

# ---------- DIREITA: a vida do capacitor ----------
X_BARRA, L_BARRA = 7.55, 0.9
C_MIN = 75  # base da barra (%), só para mostrar a zona de falha


def y_de(c):
    """Converte capacitância (%) em altura na figura (escala linear)."""
    return 2.2 + (c - C_MIN) / (C_NOVO - C_MIN) * 7.0


faixas = [(C_ALERTA, C_NOVO, VERDE), (C_FALHA, C_ALERTA, AMBAR), (C_MIN, C_FALHA, VERMELHO)]
for c_base, c_topo, cor in faixas:
    ax.add_patch(Rectangle((X_BARRA, y_de(c_base)), L_BARRA, y_de(c_topo) - y_de(c_base),
                           facecolor=cor, alpha=0.35, edgecolor="none"))
ax.add_patch(Rectangle((X_BARRA, y_de(C_MIN)), L_BARRA, y_de(C_NOVO) - y_de(C_MIN),
                       fill=False, edgecolor=PRETO, lw=2))

ax.text(X_BARRA + L_BARRA / 2, y_de(C_NOVO) + 0.45, "capacitância", ha="center",
        va="bottom", fontsize=18, color=CINZA)

marcas = [
    (C_NOVO, "capacitor novo", PRETO),
    (C_ALERTA, f"alerta do gêmeo\ndigital (−{C_NOVO - C_ALERTA}%)", PRETO),
    (C_FALHA, f"falha pela norma\nIEC 60252-1 (−{C_NOVO - C_FALHA}%)", PRETO),
]
for c, rotulo, cor in marcas:
    y = y_de(c)
    ax.plot([X_BARRA - 0.15, X_BARRA + L_BARRA + 0.15], [y, y], color=cor, lw=3)
    ax.text(X_BARRA - 0.3, y, f"{c}%", ha="right", va="center", fontsize=20,
            fontweight="bold", color=cor)
    ax.text(X_BARRA + L_BARRA + 0.35, y, rotulo, ha="left", va="center",
            fontsize=18, color=cor, linespacing=1.2)

# seta do envelhecimento
ax.annotate("", xy=(X_BARRA - 0.95, y_de(C_MIN) + 0.3), xytext=(X_BARRA - 0.95, y_de(C_FALHA) - 0.5),
            arrowprops=dict(arrowstyle="-|>", color=CINZA, lw=2.5, mutation_scale=25))
ax.text(X_BARRA - 1.15, (y_de(C_MIN) + y_de(C_FALHA)) / 2 - 0.1, "envelhece",
        ha="right", va="center", fontsize=16, color=CINZA, rotation=90)

fig.savefig(Path(__file__).with_suffix(".png"), dpi=100, facecolor="white")
print("salvo:", Path(__file__).with_suffix(".png"))
