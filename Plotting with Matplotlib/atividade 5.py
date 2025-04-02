import matplotlib.pyplot as plt
import numpy as np

# atividade 5

plt.figure(figsize=(7.5, 6.5))

labels = np.array(['China', 'Estados Unidos', 'Europa', 'Outros'])
data = np.array([30, 40, 20, 10])
colors = ['red', 'blue', 'yellow', 'grey']
#offsets = [0.03, 0.03, 0.02, 0.02]

edge_props = {
    'linewidth' : 2,
    'edgecolor' : 'black',
    'linestyle' : 'solid'
}

text_props = {
    'color' : 'black',
    'style' : 'oblique',
    'size' : 8
}

plt.pie(
    data,
    labels=labels,
    colors=colors,
    shadow=True,
    startangle=90,
    radius=0.7,
    #explode=offsets,
    wedgeprops=edge_props,
    textprops=text_props,
    autopct=lambda value: '%.2f %s' %(value, '%')
)

plt.title("Destinos de exportações do Brasil")
plt.legend(labels, loc='lower left')

plt.show()