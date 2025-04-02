import matplotlib.pyplot as plt
import numpy as np

# atividade 1

x = np.arange(0, 11, 1)
y = (5 * x) + 1

plt.figure(figsize=(9,7))

plt.grid(
    c='blue',
    ls='solid',
    lw=1.5,
    alpha=0.1
)

font_props = {
    'family' : 'Times New Roman',
    'weight' : 'medium',
    'color' : 'grey',
    'size' : 16
}

plt.plot(
    x,
    y,
    label='y = 5x + 1',
    color='blue',
    marker='s',
    markerfacecolor='red',
    markeredgecolor='red',
    markersize=6)

plt.xlabel("Eixo X", fontdict=font_props)
plt.ylabel("Eixo Y", fontdict=font_props)
plt.title("Gráfico da Função: y = 5x + 1", fontdict=font_props, y=1.05)

plt.xticks([i for i in range(0,11)])

print(x, y)

plt.show()