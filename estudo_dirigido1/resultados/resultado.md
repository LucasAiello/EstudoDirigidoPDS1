## A relação entre os fundamentos matemáticos e a implementação em Python revela nuances críticas para o processamento de sinais:

### A. O Impacto da Linearidade e do OffsetNa teoria
Vimos que $y[n] = x[n] + 5$ não é um sistema linear, mas sim afim. Na prática do sensor industrial (simulacao2.py), o sinal possui um offset de $25$. Se o sistema de processamento não for linear (por exemplo, se houver uma saturação ou se o ganho mudar com a amplitude), a superposição de sinais seria violada, tornando impossível prever a saída para diferentes níveis de ruído.

### B. Causalidade e o Dilema do Tempo RealNo texto teórico
Definimos que um sistema causal não "prevê o futuro". No código, ao utilizar mode='same' na convolução, o Python centraliza a janela. Isso significa que, para calcular o valor filtrado no instante $n$, ele usa amostras de $n+1$ e $n+2$.Conclusão Prática: Em um sistema embarcado (ESP32), isso seria impossível. O sistema deve ser forçado à causalidade, utilizando apenas amostras passadas ($n, n-1, n-2...$), o que introduz um atraso de fase inevitável na saída.

### C. Estabilidade BIBO e Convolução
O filtro de média móvel implementado é um sistema BIBO Estável. Como a resposta ao impulso $h[n]$ é uma sequência finita de valores $1/5$, a soma absoluta de seus coeficientes é exatamente $1$ (finita). Isso garante que, mesmo que o sensor sofra um pico súbito de ruído, a saída do filtro nunca "explodirá" para o infinito, protegendo os atuadores subsequentes no processo industrial.

### D. A Natureza do Erro na Amostragem
Ao comparar o sinal contínuo com o discreto no código inicial, observamos que a escolha da frequência de amostragem ($20\text{ Hz}$) define a fidelidade da representação. Se a frequência do sinal do sensor fosse superior a $10\text{ Hz}$ (metade da taxa de amostragem), ocorreria o fenômeno de aliasing, e a informação original seria irremediavelmente perdida, independentemente da qualidade do filtro de média móvel aplicado depois.