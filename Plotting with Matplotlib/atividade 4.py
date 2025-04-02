import matplotlib.pyplot as plt
import numpy as np

# atividade 4

plt.figure(figsize=(12.5,8.5))

font_props = {
    'family' : 'Times New Roman',
    'weight' : 'medium',
    'color' : 'grey',
    'size' : 16
}

# gráfico 1

plt.subplot(1, 2, 1)

plt.grid(
    c='blue',
    ls='solid',
    lw=1.5,
    alpha=0.1,
    zorder=1
)

year = np.array([i for i in range(2016, 2023)])
dolar = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])

plt.xlabel("Ano", fontdict=font_props)
plt.ylabel("Valor", fontdict=font_props)
plt.title("Valor do Real em Relação ao Dólar", fontdict=font_props)

plt.xticks([i for i in range(2016, 2023)])
plt.yticks([(i/100) for i in range(0, 600, 25)])

plt.ylim(0, 6)

plt.bar(year, dolar, color='red', width=0.4, zorder=3, alpha=0.7)

# gráfico 2

plt.subplot(1, 2, 2)

plt.grid(
    c='blue',
    ls='solid',
    lw=1.5,
    alpha=0.1,
    zorder=1
)

p_year = np.array([i for i in range(2016, 2023)])
pib_br = np.array([8710.50, 9928.50, 9151.58, 8897.29, 6795.32, 7500.21, 7542.34])

plt.xlabel("Ano", fontdict=font_props)
plt.ylabel("PIB per Capita Brasil", fontdict=font_props)
plt.title("PIB per Capita Brasileiro (USD)", fontdict=font_props)

plt.xticks([i for i in range(2016, 2023)])
plt.yticks([i for i in range(6700, 10001, 100)])

#plt.ylim(min(pib_br), 10000)

plt.plot(
    p_year,
    pib_br,
    label='"PIB per Capita Brasileiro (USD)',
    color='red',
    alpha=0.5,
    marker='.',
    markerfacecolor='black',
    markeredgecolor='black',
    markersize=7)

# ajustando os gráficos
plt.subplots_adjust(wspace=0.4)
plt.suptitle("Informações sobre o Brasil", x=0.5, y=0.97)

plt.show()