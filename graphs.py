from matplotlib import pyplot as plt
import numpy as np
from functions import *



degrees = [318.25, 317.37, 316.83, 316.62 ,315.15 ,314.3 ,313.72]
wavelenghts = [443.755, 471.314, 492.193, 501.567, 587.562, 667.815, 686.7]
eq = lambda x:6.0331*(x**2) - 3869.4*x + 620821
np.vectorize(eq)
x_axis_inter = np.linspace(313, 318.5, 100)
interpolation = eq(x_axis_inter)



fig, ax = plt.subplots(figsize=(5, 3))

ax.set_title('Curva de Calibración del Helio')
ax.set_ylabel('Longitud de Onda λ (nm)')
ax.set_xlabel('Grados (°)')
ax.scatter(degrees, wavelenghts)
ax.plot(x_axis_inter, interpolation, '--', color='orange', label=r'$6.0331x^{2} - 3869.4x + 620821$')
ax.text(317, 650, r'$r^{2} = 0.9924$', fontsize = 10)
ax.legend(loc='upper right')
ax.grid()
fig.tight_layout()


delta = np.array([53.38, 49.32, 46.55, 45.53, 45.17, 46.73, 47.65, 49.92, 50.8, 51.12])
theta_i = np.array([40.25, 42.25, 43.75, 45.25, 47.75, 60.75, 61.25, 67, 68, 69.25])
eq2 = lambda x: 0.0345*(x**2) - 3.7344*x + 145.53
np.vectorize(eq2)
theta_axis_inter = np.linspace(40, 70, 10)
delta_inter = eq2(theta_axis_inter)
amax = np.argmin(delta_inter)
delta_min = delta_inter[amax]
delta_min_str = str((round(delta_min, 3)))
xlim,ylim = plt.xlim(), plt.ylim()

print(len(theta_i), len(delta))
fig1, ax1 = plt.subplots(figsize=(5, 3))
plt.plot([theta_axis_inter[amax], theta_axis_inter[amax], 38], [43, delta_inter[amax], delta_inter[amax]], linestyle="--", color='magenta', label=r'$\delta_{min}$ ' + f'= {delta_min_str}')
ax1.set_title(r'Desviación $\delta$  v.s Ángulo de Incidencia $\theta_i$')
ax1.set_ylabel(r'Desviación $\delta$ (°)')
ax1.set_xlabel(r'Ángulo de Incidencia $\theta_i$ (°)')
ax1.scatter(theta_i, delta)
ax1.plot(theta_axis_inter, delta_inter, '--', color='orange', label=r'$0.0345x^{2} - 3.7344x + 145.53$')
ax1.text(49, 48, r'$r^{2} = 0.7709$', fontsize = 10)
ax1.legend(loc='best')
ax1.grid()
fig1.tight_layout()


theta_e = [73.13, 67.07, 62.8, 60.28, 57.42, 45.98, 46.4, 42.92, 42.8, 41.87]
eq3 = lambda x: (-0.9501*x) + 105.89
np.vectorize(eq3)
theta_axis_inter = np.linspace(40, 70, 10)
the_inter = eq3(theta_axis_inter)

fig2, ax2 = plt.subplots(figsize=(5, 3))

ax2.set_title(r'Ángulo de Salida $\theta_e$  v.s Ángulo de Incidencia $\theta_i$')
ax2.set_ylabel(r'Ángulo de Salida $\theta_e$ (°)')
ax2.set_xlabel(r'Ángulo de Incidencia $\theta_i$ (°)')
ax2.scatter(theta_i, theta_e)
ax2.plot(theta_axis_inter, the_inter, '--', color='orange', label=r'$-0.9501x + 105.89')
ax2.text(56, 58, r'$r^{2} = 0.9467$', fontsize = 10)
ax2.legend(loc='upper right')
ax2.grid()
fig2.tight_layout()


plt.show()