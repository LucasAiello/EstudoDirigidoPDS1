# Atividade 5 – Suavização de sinais

Considere um sinal de sensor representado por:

x[n] = {2, 5, 4, 6, 8, 7, 5, 4}

e um filtro de média simples:

h[n] = 1/3{1, 1, 1}

## 1 - Realize a convolução entre x[n] e h[n].

$y[0]$: $\frac{1}{3}(2 + 0 + 0) = \mathbf{0,67}$

$y[1]$: $\frac{1}{3}(5 + 2 + 0) = \mathbf{2,33}$

$y[2]$: $\frac{1}{3}(4 + 5 + 2) = \frac{11}{3} = \mathbf{3,67}$

$y[3]$: $\frac{1}{3}(6 + 4 + 5) = \frac{15}{3} = \mathbf{5,00}$

$y[4]$: $\frac{1}{3}(8 + 6 + 4) = \frac{18}{3} = \mathbf{6,00}$

$y[5]$: $\frac{1}{3}(7 + 8 + 6) = \frac{21}{3} = \mathbf{7,00}$

$y[6]$: $\frac{1}{3}(5 + 7 + 8) = \frac{20}{3} = \mathbf{6,67}$

$y[7]$: $\frac{1}{3}(4 + 5 + 7) = \frac{16}{3} = \mathbf{5,33}$

$y[8]$: $\frac{1}{3}(0 + 4 + 5) = \mathbf{3,00}$

$y[9]$: $\frac{1}{3}(0 + 0 + 4) = \mathbf{1,33}$

## 2 - Apresente o gráfico do sinal original e do sinal filtrado.

O gráfico do sinal original está no arquivo *atv5_grafico1.png* e gráfico do sinal filtrado está em *atv5_grafico2.png*

## 3 - Explique por que esse filtro atua como suavizador.

O filtro de média funciona como um filtro passa-baixas. Ele reduz ruídos e variações bruscas ao tirar a média dos vizinhos, preservando apenas a tendência principal do sinal.