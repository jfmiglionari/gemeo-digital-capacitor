# Plano de validação

| # | Pergunta | Como verificar | Critério de sucesso |
|---|---|---|---|
| V1 | O modelo do motor está certo? | Reproduzir o motor 1 do Ghial (IL, Pin, pf medidos) | Erro comparável ao reportado pelo artigo (a definir após reproduzir) |
| V2 | A perda de C aparece nas correntes? | Sprint 1: varredura de C de 100% a 85% | Alguma grandeza muda mais que a precisão do sensor para C/C0 = 95% (limiar de alerta, ADR 0004) |
| V3 | O estimador recupera C sem ruído? | Etapa 2: planta simulada ideal | Erro de C < 0,5% |
| V4 | E com sensores reais? | Sprint 2: ruído e resolução dos sensores | Erro de C bem menor que 5% (margem até o alerta) |
| V5 | E com carga, tensão e temperatura variando? | Sprint 2: cenários com perturbações | Sem alarmes falsos; alerta em C/C0 = 95%, bem antes da falha em 85% |
| V6 | Vale para outro motor? | Repetir V1–V5 com o motor WEG | Mesmas conclusões |
| V7 | (Futuro) Vale na máquina real? | Bancada com capacitores de valores conhecidos | Erro de C dentro do obtido em V4 |

Cada verificação vira um script em `experimentos/` e, quando possível, um teste em `tests/`.
