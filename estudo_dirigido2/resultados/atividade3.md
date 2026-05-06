# Atividade 3 – Sistema descrito por equação de diferenças

Considere o sistema:

y[n] = 0.8 y[n − 1] + x[n]

## 1 - Determine os primeiros valores de h[n] para 0 ≤ n ≤ 5.

Para $n = 0$:
$h[0] = 0,8 \cdot h[-1] + \delta[0] \implies 0,8(0) + 1 = \mathbf{1}$

Para $n = 1$:
$h[1] = 0,8 \cdot h[0] + \delta[1] \implies 0,8(1) + 0 = \mathbf{0,8}$

Para $n = 2$:
$h[2] = 0,8 \cdot h[1] + \delta[2] \implies 0,8(0,8) + 0 = \mathbf{0,64}$

Para $n = 3$:
$h[3] = 0,8 \cdot h[2] + \delta[3] \implies 0,8(0,64) + 0 = \mathbf{0,512}$

Para $n = 4$:
$h[4] = 0,8 \cdot h[3] + \delta[4] \implies 0,8(0,512) + 0 = \mathbf{0,4096}$

Para $n = 5$:
$h[5] = 0,8 \cdot h[4] + \delta[5] \implies 0,8(0,4096) + 0 = \mathbf{0,32768}$

## 2 - A partir da resposta ao impulso obtida, discuta se o sistema parece ser estável.

Sim é estável, pois a série converge pra um valor finito

## 3 - Verifique se o sistema é causal.

Sim, é causal. Pois, para um sistema ser causal ele deve depender de valores presentes ou passados, e como a formula mostra:
y[n] = 0.8 y[n − 1] + x[n]
