# Plano de validação

| # | Pergunta | Como verificar | Critério de sucesso |
|---|---|---|---|
| V1 | O modelo do motor está certo? | Reproduzir o motor 1 do Ghial (IL, Pin, pf medidos) | Erro comparável ao reportado pelo artigo (a definir após reproduzir) |
| V2 | A perda de C aparece nas correntes? | Etapa 1: varredura de C | Alguma grandeza muda mais que a precisão do sensor para C/C0 = 95% |
| V3 | O estimador recupera C sem ruído? | Etapa 2: planta simulada ideal | Erro de C < 0,5% |
| V4 | E com sensores reais? | Etapa 2: ruído e resolução dos sensores | Erro de C menor que a margem até o fim de vida (5%) |
| V5 | E com carga, tensão e temperatura variando? | Etapa 2: cenários com perturbações | Sem alarmes falsos; alerta antes de C/C0 = 95% |
| V6 | Vale para outro motor? | Repetir V1–V5 com o motor WEG | Mesmas conclusões |
| V7 | (Futuro) Vale na máquina real? | Bancada com capacitores de valores conhecidos | Erro de C dentro do obtido em V4 |

Cada verificação vira um script em `experimentos/` e, quando possível, um teste em `tests/`.
