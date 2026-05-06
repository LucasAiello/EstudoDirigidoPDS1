# Atividade 2 – Cálculo manual de convolução

Considere:
x[n] = {1, 2, 1} h[n] = {1, 1}

## 1 - Calcule manualmente a convolução y[n] = x[n] ∗ h[n]

Primeiramente, deve-se calcular a quantidade de iterações do somatório *n*

*n* = 3 + 2 - 1 = 4

n = 0
y[0] = (x[0] * h[0 - 0]) + (x[1] * h[0 - 1]) + (x[2] * h[0 - 2])
y[0] = (1 * h[0]) + (2 * h[-1]) + (1 * h[-2])
y[0] = (1 * 1) + (2 * 0) + (1 * 0)
y[0] = 1

n = 1
y[1] = (x[0] * h[1 - 0]) + (x[1] * h[1 - 1]) + (x[2] * h[1 - 2])
y[1] = (1 * h[1]) + (2 * h[0]) + (1 * h[-1])
y[1] = (1 * 1) + (2 * 1) + (1 * 0)
y[1] = 3

n = 2
y[2] = (x[0] * h[2 - 0]) + (x[1] * h[2 - 1]) + (x[2] * h[2 - 2])
y[2] = (1 * h[2]) + (2 * h[1]) + (1 * h[0])
y[2] = (1 * 0) + (2 * 1) + (1 * 1)
y[2] = 3

n = 3
y[2] = (x[0] * h[3 - 0]) + (x[1] * h[3 - 1]) + (x[2] * h[3 - 2])
y[2] = (1 * h[3]) + (2 * h[2]) + (1 * h[1])
y[2] = (1 * 0) + (2 * 0) + (1 * 1)
y[2] = 1

## 2 - Apresente o resultado em forma de sequência.

y[n] = {1,3,3,1}

## 3 - Explique o significado do resultado obtido.

O resultado da convolução indica que o sistema soma cada amostra do sinal de entrada com a amostra anterior, produzindo um efeito de suavização. 