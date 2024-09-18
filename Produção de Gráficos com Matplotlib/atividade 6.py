import matplotlib.pyplot as plt
import numpy as np

# atividade 6

altura = np.array([1.60, 1.62, 1.65, 1.65, 1.70, 1.70, 1.75, 1.80, 1.85, 1.90, 1.90, 1.95, 2.00])
peso = np.array([42, 61, 64, 67, 70, 73, 80, 85, 90, 95, 85, 115, 152])

# definindo o estilo do gráfico
plt.style.use("bmh")

# calculando o imc das pessoas

imc = []

for i in range(0, 13):
    temp = peso[i] / (altura[i] ** 2)
    temp = round(temp, 2)
    imc.append(temp)

# definindo as cores de acordo com o imc

colors = []

for i in imc:
    
    match i:

        case i if (i < 16.9):
            colors.append('red')
        
        case i if (i >= 17 and i <= 18.4):
            colors.append('orange')

        case i if (i >= 18.5 and i <= 24.9):
            colors.append('green')
        
        case i if (i >= 25 and i <= 29.9):
            colors.append('yellow')

        case i if (i >= 30 and i <= 34.9):
            colors.append('orange')

        case i if (i > 35):
            colors.append('red')

        case _:
            colors.append('blue')

colors = np.array(colors)

# fazendo o plot dos pontos

plt.scatter(
    peso,
    altura,
    c=colors,
    marker='o',
    #s=size,
    edgecolors='black',
    linewidths=1,
    zorder=3,
    label='Relação Peso/Altura')

print(imc, colors)

plt.show()