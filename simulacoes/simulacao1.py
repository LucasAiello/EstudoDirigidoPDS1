import numpy as np
import matplotlib.pyplot as plt


plt.rcParams.update({'font.size': 11, 'figure.figsize': (12, 8), 'axes.grid': True})

frequency = 20  
t_cont = np.linspace(0, 0.5, 1000)
x_cont = np.cos(2 * np.pi * 10 * t_cont) 

n_amostras = np.arange(0, 11) 
x_disc = np.cos(2 * np.pi * 10 * (n_amostras/frequency))

n_range = np.arange(-10, 21)
impulso = (n_range == 0).astype(float)
degrau = (n_range >= 0).astype(float)

fig, axs = plt.subplots(1, 4, figsize=(15, 10))

axs[0].plot(t_cont, x_cont, label='Contínuo $x(t)$')
axs[0].stem(n_amostras/frequency, x_disc, 'r', label='Discreto $x[n]$')
axs[0].set_title("1.1 Processo de Amostragem (Contínuo vs Discreto)")
axs[0].set_xlabel("Tempo (s)"); axs[0].legend()

axs[1].stem(n_range, impulso, 'b')
axs[1].set_title("1.2 Impulso Unitário $\delta[n]$")

axs[2].stem(n_range, degrau, 'orange')
axs[2].set_title("1.3 Degrau Unitário $u[n]$")

axs[3].stem(n_range, np.cumsum(impulso), 'g')
axs[3].set_title("1.4 Degrau gerado pela Soma de Impulsos")

plt.tight_layout()
plt.show()