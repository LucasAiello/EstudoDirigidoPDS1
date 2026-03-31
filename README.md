# Estudo dirigido PDS

O presente repositório visa compartilhar um estudo sobre os conceitos básicos de sinais e sistemas para a disciplina de Processamento Digital de Sinais, baseando-se na metodologia PBL (Problem/Project Based Learning), e utilizando o livro "Sinais e Sistemas" de Alan V. Oppenheim e Alan S. Willsky como referência para o estudo.

## Esse repositório contém:

* Um resumo teórico 
* Simulações computacionais envolvendo sinais discretos
* Interpretação dos resultados obtidos nas simulações, relacionando
os conceitos estudados com aplicações em engenharia.

Para resolver o problema norteador, o fluxo de trabalho foi dividido em quatro etapas fundamentais:

### Modelagem Matemática do Sinal do Sensor:
Representação de um fenômeno físico (como temperatura ou pressão) através de uma função composta: $x[n] = s[n] + \eta[n] + C$, onde $s[n]$ é o sinal de interesse, $\eta[n]$ é o ruído Gaussiano e $C$ é o offset (viés) do sensor.

### Simulação de Processamento Digital (Filtragem):

Implementação de um sistema de média móvel para suavizar o ruído. A operação foi realizada via convolução discreta, utilizando uma janela de 5 amostras para extrair a tendência do sinal puro.

### Análise de Propriedades Estruturais:

Verificação manual e computacional das propriedades do sistema de filtragem (Linearidade, Causalidade e Estabilidade) para garantir que o processamento não distorça a informação essencial.

### Quantificação de Intensidade:

Cálculo de métricas de Energia e Potência Média para determinar a viabilidade do sistema em termos de hardware e consumo energético.