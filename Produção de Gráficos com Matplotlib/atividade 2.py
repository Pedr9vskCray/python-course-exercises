import matplotlib.pyplot as plt
import numpy as np

# atividade 2

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

year = np.array([i for i in range(2016, 2023)])
dolar = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])

plt.title("Valor do Real em Relação ao Dólar", fontdict=font_props, y=1.05)
plt.xlabel("Ano", fontdict=font_props)
plt.ylabel("Valor", fontdict=font_props)

plt.xticks([i for i in range(2016, 2023)])
plt.yticks([(i/100) for i in range(int(min(dolar)*100), int(max(dolar)*100)+55, 10)])

plt.ylim(min(dolar), 6)

plt.plot(
    year,
    dolar,
    label='"Valor do Real em Relação ao Dólar',
    color='red',
    alpha=0.5,
    marker='.',
    markerfacecolor='black',
    markeredgecolor='black',
    markersize=7)

plt.show()