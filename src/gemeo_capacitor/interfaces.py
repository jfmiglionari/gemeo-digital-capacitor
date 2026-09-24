"""Contratos entre as camadas do gêmeo digital (ver docs/01-arquitetura.md).

A planta simulada e a futura bancada implementam a mesma interface `Planta`.
O gêmeo nunca acessa o valor verdadeiro de C (ver docs/adr/0002).
"""

from dataclasses import dataclass
from typing import Protocol

import numpy as np


@dataclass
class Amostras:
    """Sinais como um sensor entregaria."""

    tempo_s: np.ndarray
    v_rede: np.ndarray
    i_principal: np.ndarray
    i_auxiliar: np.ndarray


@dataclass
class Fasores:
    """Amplitude e fase (números complexos, valor eficaz) na frequência da rede."""

    Vm: complex
    Im: complex
    Ia: complex


@dataclass
class EstadoEstimado:
    """O que o gêmeo acredita sobre o capacitor."""

    C_F: float
    Rc_ohm: float
    incerteza_C_F: float
    residuo: float


class Planta(Protocol):
    def amostrar(self, duracao_s: float) -> Amostras: ...


class Estimador(Protocol):
    def atualizar(self, fasores: Fasores) -> EstadoEstimado: ...
