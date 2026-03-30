import numpy as np
import matplotlib.pyplot as plt

n_s = np.arange(0, 80)
sinal_puro = 25 + 3 * np.sin(0.1 * n_s) 
ruido = np.random.normal(0, 0.6, len(n_s)) 
x_sensor = sinal_puro + ruido

janela = 5
y_sensor = np.convolve(x_sensor, np.ones(janela)/janela, mode='same')

n_atraso = 15
x_atrasado = np.zeros_like(x_sensor)
x_atrasado[n_atraso:] = x_sensor[:-n_atraso]

energia = np.sum(np.abs(x_sensor)**2)
potencia_media = energia / len(x_sensor)


plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.plot(n_s, x_sensor, 'r--', alpha=0.5, label='Entrada: Sensor + Ruído')
plt.plot(n_s, y_sensor, 'b-', linewidth=2, label='Saída: Sinal Filtrado (Média Móvel)')
plt.title("2.1 Problema Norteador: Filtragem de Sensor Industrial")
plt.legend()

plt.subplot(1, 2, 2)
plt.stem(n_s, x_sensor, linefmt='C0-', markerfmt='C0o', label='$x[n]$ original')
plt.stem(n_s, x_atrasado, linefmt='C1-', markerfmt='C1o', label='$x[n-15]$ atrasado')
plt.title("2.2 Operação de Deslocamento Temporal (Atraso)")
plt.legend()

plt.tight_layout()
plt.show()