from matplotlib import pyplot as plt
import numpy as np
from functions import *


x, y = process_data('nofilter.txt')
red_x, red_y = process_data('redfilter.txt')
blue_x, blue_y = process_data('bluefilter.txt')
green_x, green_y = process_data('greenfilter.txt')
rb_x, rb_y = process_data('blueredfilter.txt')
bg_x, bg_y = process_data('greenbluefilter.txt')
rg_x, rg_y = process_data('greenredfilter.txt')

fig, ax = plt.subplots(figsize=(5, 3))

ax.set_title('Espectro Fuente de Luz Blanca')
ax.set_ylabel('Intensidad Relativa')
ax.set_xlabel('Longitud de Onda (λ)')
ax.plot(x, y)
ax.grid()
ax.set_xlim([120, 900])
ax.set_xticks(np.arange(120, len(x) - 50, 80))
fig.tight_layout()

fig1, ax1 = plt.subplots(figsize=(5,3))
ax1.set_title('Espectro Fuente de Luz Blanca Aplicando Filtros')
ax1.set_ylabel('Intensidad Relativa')
ax1.set_xlabel('Longitud de Onda (λ)')
ax1.plot(x, red_y, label='Filtro rojo', color='red')
ax1.plot(x, blue_y, label='Filtro azul', color='blue')
ax1.plot(x, green_y, label='Filtro verde', color='green')
ax1.set_xticks(np.arange(120, len(x) - 50, 80))
fig1.tight_layout()
ax1.legend(loc='upper left')
ax1.grid()


fig2, ax2 = plt.subplots(figsize=(5,3))
ax2.set_title('Espectro Fuente de Luz Blanca Aplicando 2 Filtros')
ax2.set_ylabel('Intensidad Relativa')
ax2.set_xlabel('Longitud de Onda (λ)')
ax2.plot(x, rb_y, label='Flt. rojo-azul', color='purple')
ax2.plot(x, bg_y, label='Flt azul-verde', color='darkturquoise')
ax2.plot(x, rg_y, label='Flt rojo-verde', color='orange')
ax2.set_xticks(np.arange(120, len(x) - 50, 80))
fig2.tight_layout()
ax2.legend(loc='upper left')
ax2.grid()


plt.show()


