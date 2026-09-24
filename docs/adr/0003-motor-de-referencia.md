# ADR 0003 — Motor de referência: Ghial et al. (2014), motor 1

**Status:** aceito (2026-09-24)

## Contexto
O modelo precisa de todos os parâmetros do circuito equivalente de um motor PSC real **e** de medições em operação para validar. Datasheets comerciais normalmente não trazem o circuito equivalente.

## Decisão
Usar o motor 1 do estudo de caso de Ghial, Saini & Saini (2014): ventilador PSC de 70 W, 230 V, 50 Hz, 4 polos, C = 2,63 µF. Um motor comercial WEG entra depois como segunda máquina (etapa 4).

## Consequências
- Modelo validável contra dados publicados desde o primeiro dia.
- Dependência de um único artigo: inconsistências nele (ver [Fontes de dados](../02-fontes-de-dados.md)) precisam ser tratadas e documentadas.
- A generalização só é demonstrada com a segunda máquina.
