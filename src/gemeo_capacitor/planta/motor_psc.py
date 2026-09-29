"""Motor PSC em regime permanente (Ghial, Saini & Saini, 2014).

Modelo da planta: dado o capacitor (C, Rc) e a tensão, calcula as correntes
dos enrolamentos e o desempenho do motor. Escorregamento fixo (ver
docs/03-modelo-matematico.md, seção 6).

Calibração (ver docs/adr/0005-planta-calibrada-tabela-iii.md): Z11, Z12 e Z21
e a parte de Z22 sem o capacitor vêm da Tabela III do artigo. O capacitor é
somado de volta a Z22 como Zc = Rc − jXc, e é só aí que C entra.
"""

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np

RAIZ = Path(__file__).resolve().parents[3]
ARQUIVO_MOTOR = RAIZ / "dados" / "referencia" / "motor_ghial_2014.json"


def _complexo(par):
    """Converte [real, imag] do JSON em número complexo."""
    return complex(par[0], par[1])


@dataclass
class Resultado:
    """Saídas do modelo (fasores em valor eficaz, com a tensão como referência de fase)."""

    Im: complex  # corrente do enrolamento principal
    Ia: complex  # corrente do enrolamento auxiliar
    IL: float  # módulo da corrente de linha |Im + Ia|
    Pin: float  # potência de entrada
    pf: float  # fator de potência

    @property
    def defasagem_graus(self) -> float:
        """Ângulo entre Ia e Im (quanto Ia está adiantada em relação a Im)."""
        return float(np.degrees(np.angle(self.Ia / self.Im)))


class MotorPSC:
    """Motor PSC do Ghial (2014), motor 1, com o capacitor como entrada."""

    def __init__(self, arquivo=ARQUIVO_MOTOR):
        dados = json.loads(Path(arquivo).read_text(encoding="utf-8"))
        tab = dados["tabela_III_metodo_proposto"]
        cap = dados["capacitor"]

        # Impedâncias acopladas, Ghial eqs. (47)–(50), valores da Tabela III
        self.Z11 = _complexo(tab["Z11_ohm"])
        self.Z12 = _complexo(tab["Z12_ohm"])
        self.Z21 = _complexo(tab["Z21_ohm"])
        Z22_artigo = _complexo(tab["Z22_ohm"])

        # Capacitor nominal: Ghial eq. (18), Zc = Rc − jXc
        self.C0_F = cap["C_uF"] * 1e-6
        self.Rc0_ohm = cap["Rc_ohm"]
        self.Xc0_ohm = cap["Xc_ohm"]
        Zc0 = self.Rc0_ohm - 1j * self.Xc0_ohm

        # Ghial eq. (50): Z22 = Z*sa + Zc + a²(Zfm + Zbm).
        # Tiramos o capacitor nominal; o que sobra não depende de C.
        self.Z22_sem_capacitor = Z22_artigo - Zc0

        self.V_nominal = dados["medido_em_operacao"]["V_V"]

    def Zc(self, C_F: float, Rc_ohm=None) -> complex:
        """Ghial eq. (18). Xc = 1/(2πfC), logo Xc escala com C0/C."""
        Rc = self.Rc0_ohm if Rc_ohm is None else Rc_ohm
        Xc = self.Xc0_ohm * self.C0_F / C_F
        return Rc - 1j * Xc

    def resolver(self, C_F=None, V=None, Rc_ohm=None) -> Resultado:
        """Calcula correntes e desempenho para um capacitor C (padrão: nominal)."""
        C = self.C0_F if C_F is None else C_F
        V = self.V_nominal if V is None else V
        Vm = Va = V  # enrolamentos em paralelo na mesma rede

        Z22 = self.Z22_sem_capacitor + self.Zc(C, Rc_ohm)  # Ghial eq. (50)
        det = self.Z11 * Z22 - self.Z12 * self.Z21

        # Regra de Cramer nas eqs. (45)–(46); com Vm = Va viram as eqs. (51)–(52)
        Im = (Vm * Z22 - Va * self.Z12) / det
        Ia = (Va * self.Z11 - Vm * self.Z21) / det

        I_linha = Im + Ia
        # Escolha documentada em docs/02-fontes-de-dados.md: IL = |Im + Ia|
        # (o que o analisador mede), e não Re[Im + Ia] da eq. (53).
        IL = abs(I_linha)
        pf = float(np.cos(np.angle(I_linha)))  # Ghial eq. (55)
        Pin = float((V * np.conj(I_linha)).real)  # Ghial eq. (54): V·IL·cosθ

        return Resultado(Im=Im, Ia=Ia, IL=IL, Pin=Pin, pf=pf)
