"""Sprint 2: o estimador de C/C0 erra menos de 1 ponto percentual?"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "experimentos"))

from sprint2_treino_ml import avaliar  # noqa: E402
from sprint2_dataset import gerar  # noqa: E402


def test_erro_medio_menor_que_1_pp():
    X, y = gerar()
    m, _, _ = avaliar(X, y, [0, 1, 2, 3])
    assert m["erro_medio_abs_pp"] < 1.0
