"""Camada de medição: o que um sensor barato entrega ao gêmeo.

Fronteira (ADR 0002): o gêmeo só enxerga estas quatro medições, nunca o C
verdadeiro nem as impedâncias da planta.
"""

import numpy as np

RUIDO_AMPLITUDE = 0.01  # 1% (relativo) em V, |Im| e |Ia|
RUIDO_ANGULO_GRAUS = 0.5  # 0,5° na defasagem Ia−Im
NOMES = ["V", "|Im|", "|Ia|", "defasagem"]


def medir(resultado, V, rng):
    """Devolve [V, |Im|, |Ia|, defasagem (graus)] com ruído gaussiano.

    rng: np.random.Generator (a semente fica com quem chama).
    """
    amp = 1 + RUIDO_AMPLITUDE * rng.standard_normal(3)
    return np.array([
        V * amp[0],
        abs(resultado.Im) * amp[1],
        abs(resultado.Ia) * amp[2],
        resultado.defasagem_graus + RUIDO_ANGULO_GRAUS * rng.standard_normal(),
    ])
