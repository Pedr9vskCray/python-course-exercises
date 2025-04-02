import matplotlib.pyplot as plt
import numpy as np

# atividade 3

plt.style.use('default')

plt.figure(figsize=(12,7))

plt.grid(
    c='blue',
    ls='solid',
    lw=1.5,
    alpha=0.1,
    zorder=1
)

year = np.array([i for i in range(2016, 2023)])
dolar = np.array([3.15, 3.26, 3.88, 4.30, 5.33, 5.45, 5.39])

plt.xlabel("Ano")
plt.ylabel("Valor")
plt.title("Valor do Real em Relação ao Dólar")

plt.xticks([i for i in range(2016, 2023)])
plt.yticks([(i/100) for i in range(0, 600, 25)])

plt.ylim(0, 6)

plt.bar(year, dolar, color='red', width=0.4, zorder=3, alpha=0.7)

plt.show()