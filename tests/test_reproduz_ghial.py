"""V1: o modelo reproduz o motor 1 do Ghial (2014)?

Compara com o que o artigo MEDIU em operação (Fluke 43B): V = 230 V,
IL = 0,312 A, Pin = 70 W, pf = 1,00.
"""

import json

import pytest

from gemeo_capacitor.planta.motor_psc import ARQUIVO_MOTOR, MotorPSC

MEDIDO = json.loads(ARQUIVO_MOTOR.read_text(encoding="utf-8"))["medido_em_operacao"]

# Tolerância de V1 (docs/05-plano-de-validacao.md): 6% em IL e Pin.
# O próprio artigo, com as suas impedâncias da Tabela III, fica 3–6% acima
# do medido (ver docs/02-fontes-de-dados.md, "Reprodução do artigo").
TOL_REL = 0.06
TOL_PF = 0.01  # o Fluke mostra o fator de potência com 2 casas


def erro_pct(calc, med):
    return 100 * (calc - med) / med


@pytest.fixture(scope="module")
def resultado():
    return MotorPSC().resolver()


def test_corrente_de_linha(resultado):
    e = erro_pct(resultado.IL, MEDIDO["IL_A"])
    print(f"IL = {resultado.IL:.4f} A (medido {MEDIDO['IL_A']}) → erro {e:+.1f}%")
    assert abs(e) <= 100 * TOL_REL


def test_potencia(resultado):
    e = erro_pct(resultado.Pin, MEDIDO["Pin_W"])
    print(f"Pin = {resultado.Pin:.2f} W (medido {MEDIDO['Pin_W']}) → erro {e:+.1f}%")
    assert abs(e) <= 100 * TOL_REL


def test_fator_de_potencia(resultado):
    print(f"pf = {resultado.pf:.4f} (medido {MEDIDO['pf']})")
    assert abs(resultado.pf - MEDIDO["pf"]) <= TOL_PF


def test_capacitor_so_muda_Z22():
    """C só entra em Z22: sem acoplamento (Z12 = Z21 = 0), Im não mudaria."""
    motor = MotorPSC()
    motor.Z12 = motor.Z21 = 0
    im_100 = motor.resolver().Im
    im_95 = motor.resolver(C_F=0.95 * motor.C0_F).Im
    assert im_100 == pytest.approx(im_95)
