"""Estimador de C/C0 com machine learning (ADR 0006).

Recebe só as medições da camada de sensores (ADR 0002); nunca vê o C verdadeiro
fora do treino.
"""

import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Critério do gêmeo, ADR 0004
LIMIAR_ALERTA = 0.95
LIMIAR_FALHA = 0.85
CLASSES = ["falha", "alerta", "saudável"]


def criar_modelo(semente=42):
    return RandomForestRegressor(n_estimators=200, random_state=semente, n_jobs=-1)


def classificar(c_rel):
    """Saudável (> 0,95), alerta (0,85–0,95), falha (< 0,85). Aceita escalar ou vetor.

    Devolve índices: 0 = falha, 1 = alerta, 2 = saudável (ver CLASSES).
    """
    c = np.asarray(c_rel)
    return np.where(c > LIMIAR_ALERTA, 2, np.where(c >= LIMIAR_FALHA, 1, 0))
