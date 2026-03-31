## 1. Linearidade
Um sistema é considerado linear se satisfizer o princípio da superposição (aditividade e homogeneidade).Critério:Se $x_1(t) \xrightarrow{\mathcal{T}} y_1(t)$ e $x_2(t) \xrightarrow{\mathcal{T}} y_2(t)$, então:$$\mathcal{T}\{a x_1(t) + b x_2(t)\} = a y_1(t) + b y_2(t)$$Linear: $y(t) = 3x(t)$Não-Linear: $y(t) = x^2(t)$ ou $y(t) = x(t) + 5$ (sistemas com constante aditiva são afins, não lineares).

## 2. Invariância no Tempo
Um sistema é invariante no tempo se um deslocamento temporal na entrada produzir exatamente o mesmo deslocamento na saída.Critério:Se $y(t) = \mathcal{T}\{x(t)\}$, o sistema é invariante se:$$\mathcal{T}\{x(t - t_0)\} = y(t - t_0)$$Invariante: $y(t) = \sin(x(t))$Variante: $y(t) = t \cdot x(t)$ (o ganho muda conforme o tempo passa).

## 3. Causalidade
Um sistema é causal se a saída em qualquer instante depender apenas de valores presentes e/ou passados da entrada.Critério:$y(t)$ depende de $x(\tau)$ apenas para $\tau \leq t$.Causal: $y(t) = x(t-1)$Não-Causal (Antecipativo): $y(t) = x(t+1)$

## 4. Estabilidade (BIBO)
Um sistema é estável no sentido BIBO (Bounded-Input, Bounded-Output) se toda entrada limitada produzir uma saída limitada.Critério:Se $|x(t)| \leq M_x < \infty$, então deve existir $M_y < \infty$ tal que:$$|y(t)| \leq M_y$$Para sistemas LTI (Lineares e Invariantes no Tempo), a estabilidade é garantida se a resposta ao impulso $h(t)$ for absolutamente integrável:$$\int_{-\infty}^{\infty} |h(t)| dt < \infty$$

## 5. Memória
Sem Memória (Instantâneo): A saída $y(t)$ depende apenas de $x(t)$ no mesmo instante $t$. Ex: $y(t) = R \cdot i(t)$.Com Memória (Dinâmico): A saída depende de valores passados ou futuros. Ex: $y(t) = \int_{0}^{t} x(\tau) d\tau$.

## 6. Invertibilidade

Um sistema é invertível se entradas distintas produzirem saídas distintas, permitindo a recuperação do sinal original através de um sistema inverso.Critério:Existe $\mathcal{T}^{-1}$ tal que $\mathcal{T}^{-1}\{\mathcal{T}\{x(t)\}\} = x(t)$.