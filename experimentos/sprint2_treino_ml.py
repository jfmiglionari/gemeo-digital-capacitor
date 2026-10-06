"""Sprint 2: treina e avalia o estimador de C/C0.

Compara o modelo completo (V, |Im|, |Ia|, defasagem) com a linha de base que
usa só |Im|. Rodar:  python experimentos/sprint2_treino_ml.py
"""

import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from gemeo_capacitor.gemeo.estimador_ml import (CLASSES, LIMIAR_ALERTA, LIMIAR_FALHA,
                                                classificar, criar_modelo)
from gemeo_capacitor.medicao.sensores import NOMES
from sprint2_dataset import gerar

RESULTADOS = Path(__file__).resolve().parent.parent / "resultados"


def avaliar(X, y, colunas):
    """Treina 80/20 usando só as colunas dadas; devolve métricas e previsões."""
    Xtr, Xte, ytr, yte = train_test_split(X[:, colunas], y, test_size=0.2, random_state=42)
    modelo = criar_modelo().fit(Xtr, ytr)
    est = modelo.predict(Xte)
    real_cl, est_cl = classificar(yte), classificar(est)
    saud = real_cl == 2
    return {
        "erro_medio_abs_pp": float(100 * np.mean(np.abs(est - yte))),
        "acuracia": float(np.mean(real_cl == est_cl)),
        "alarme_falso": float(np.mean(est_cl[saud] != 2)),
        "matriz_confusao (linhas=real, colunas=estimado; ordem " + "/".join(CLASSES) + ")":
            confusion_matrix(real_cl, est_cl, labels=[0, 1, 2]).tolist(),
    }, yte, est


if __name__ == "__main__":
    X, y = gerar()
    completo, yte, est = avaliar(X, y, [0, 1, 2, 3])
    base, _, _ = avaliar(X, y, [NOMES.index("|Im|")])
    metricas = {"modelo_completo": completo, "linha_de_base_so_Im": base}
    RESULTADOS.mkdir(exist_ok=True)
    (RESULTADOS / "sprint2_metricas.json").write_text(
        json.dumps(metricas, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(metricas, indent=2, ensure_ascii=False))

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(100 * yte, 100 * est, s=6, alpha=0.5)
    ax.plot([80, 102], [80, 102], "k-", lw=0.8, label="ideal")
    for lim, cor, nome in ((LIMIAR_ALERTA, "orange", "alerta (95%)"),
                           (LIMIAR_FALHA, "red", "falha (85%)")):
        ax.axvline(100 * lim, color=cor, ls="--", label=nome)
        ax.axhline(100 * lim, color=cor, ls="--")
    ax.set_xlabel("C/C0 real (%)")
    ax.set_ylabel("C/C0 estimado (%)")
    ax.set_title("Estimador ML: real × estimado (conjunto de teste)")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(RESULTADOS / "sprint2_real_vs_estimado.png", dpi=150)
