# Gêmeo digital do capacitor de motor monofásico

> **Objetivo:** construir um gêmeo digital que detecta, **só pelas correntes do motor**, que o capacitor de um motor de ventilador PSC está perdendo capacitância, **antes de ele falhar**.

Motores monofásicos com capacitor permanente (PSC) estão em ventiladores, ar-condicionado e lavadoras. O capacitor é um dos componentes que mais falham nesses motores, e hoje a falha só é percebida quando o motor já não funciona direito. Este projeto investiga se é possível estimar a saúde do capacitor com o motor rodando, usando apenas sinais elétricos que qualquer sensor de corrente barato mede.

**Status:** fase 1, simulação. Ver [roadmap](docs/roadmap.md).

## Por que isso não é óbvio

- O capacitor de filme chega ao fim de vida quando perde **5% da capacitância** (Zhao et al., 2021). Um sinal tão pequeno precisa ser separado do efeito da carga, da tensão da rede e da temperatura.
- O modelo do motor PSC com o capacitor existe (Ghial et al., 2014), mas é usado **offline**.
- Estimar capacitância **online** já foi feito, mas em **conversores eletrônicos** (Ghadrdan et al., 2023; Ribeiro et al., 2025), não em motores.
- O trabalho mais próximo em motor monofásico (Shukla et al., 2025) detecta apenas o capacitor **removido**, não a degradação gradual.

Este projeto junta as duas coisas: modelo do motor + estimação online da capacitância.

## Documentação

| Documento | Conteúdo |
|---|---|
| [Visão geral](docs/00-visao-geral.md) | Objetivo, escopo, o que está fora do escopo |
| [Arquitetura](docs/01-arquitetura.md) | Camadas, componentes, fluxo de dados, interfaces |
| [Fontes de dados](docs/02-fontes-de-dados.md) | De onde vem cada número usado na simulação |
| [Modelo matemático](docs/03-modelo-matematico.md) | Equações do motor e do capacitor |
| [Modelo de falhas](docs/04-modelo-de-falhas.md) | Como o capacitor degrada e quando é considerado falho |
| [Plano de validação](docs/05-plano-de-validacao.md) | Como sabemos que o gêmeo funciona |
| [Decisões (ADRs)](docs/adr/) | Registro das decisões de arquitetura e por quê |
| [Roadmap](docs/roadmap.md) | Etapas do projeto |
| [Referências](docs/referencias.md) | Artigos usados |

## Stack

Python 3 · NumPy · SciPy · Matplotlib · painel web (etapa 3).

---

## English summary

**Goal:** build a digital twin that detects, **from motor currents alone**, that the run capacitor of a permanent-split-capacitor (PSC) fan motor is losing capacitance, **before it fails**.

Film run capacitors reach end-of-life at about 5% capacitance loss. The PSC equivalent-circuit model with the capacitor exists (Ghial et al., 2014) but is used offline; online capacitance estimation exists, but for power-converter DC links. This project combines both: a PSC motor model plus online capacitance estimation. Phase 1 is simulation-only; a lab bench may follow. Documentation is in Portuguese.

## Licença / License

MIT — ver [LICENSE](LICENSE).
