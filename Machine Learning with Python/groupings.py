from sklearn import datasets
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# primeiro carregamos os conjuntos de dados de teste que vamos obter dos datasets
iris = datasets.load_iris()

# para vermos os dados que iremos utilizar para fazer os agrupamentos
iris.data

# para vermos a classe de cada instância da iris, vamos usar somente no final para testar nosso modelo
iris.target

# para vermos os nomes das classes que iremos classificar cada flor, os números que vimos acima são as
# representações numéricas desses nomes de classe que podemos ver e qual classe cada flor pertence
iris.target_names

# o nome dos atributos, são os nomes de cada atributo que cada uma das flores possui, os atributos são
# aqueles que vimos quando printamos iris.data e cada um significa uma coisa diferente na classificação
iris.feature_names

# nosso objetivo é criar 3 grupos distintos com base nos nomes das classes e tentar classificar cada
# flor que temos em um desses 3 grupos com base em uma análise de cluster (KMeans) e após isso testar
# com a classificação real de cada flor nesses grupos distintos para avaliar a precisão do agrupamento

# primeiro vamos checar quantos grupos únicos nós temos e quantas instâncias de cada um desse grupos
# nós temos dentro do dataset que vamos trabalhar
unique, quantity = np.unique(iris.target, return_counts=True)
print(unique) # 3 grupos únicos como ja sabíamos
print(quantity) # 50 flores para cada grupo é o resultado esperado no final do nosso agrupamento

# para utilizar o KMeans precisamos indicar a quantidade de clustes que iremos criar, como sabemos que
# temos exatamente 3 grupos (classes) de flores diferentes vamos criar 3 clusters diferentes

clusters = KMeans(n_clusters=3)

# agora vamos agrupar os dados nos 3 clusters que nós criamos

clusters.fit(iris.data)

# agora veremos o resultado do nosso agrupamento de clusters
# vamos também printar os resultados reais para fazermos uma comparação visual

agrupamentos = clusters.labels_
print(agrupamentos)
print(iris.target)

# dessa forma podemos ver que nosso agrupamento foi bom mas não foi 100% fiel ao que esperamos, para
# visualizarmos melhor como que está ocorrendo esse processo vamos analisar os dados únicos e também
# vamos gerar uma matriz de confusão e um placar de precisão com base na performance atual

# dados únicos e sua distribuição
uni, qnt = np.unique(agrupamentos, return_counts=True)
print(uni)
print(qnt)

# matriz de confusão
resultados = confusion_matrix(iris.target, agrupamentos) # (y_true, y_pred)
print(resultados)

# taxa de acerto
accuracy = accuracy_score(iris.target, agrupamentos)
print(f'precisão -> {accuracy * 100}%')

# agora vamos plotar um gráfico desses agrupamentos

plt.scatter(iris.data[agrupamentos == 0,0], iris.data[agrupamentos == 0,1], c='green', label='Setosa')
plt.scatter(iris.data[agrupamentos == 1,0], iris.data[agrupamentos == 1,1], c='red', label='Versicolor')
plt.scatter(iris.data[agrupamentos == 2,0], iris.data[agrupamentos == 2,1], c='blue', label='Virginica')

plt.legend()

plt.show()