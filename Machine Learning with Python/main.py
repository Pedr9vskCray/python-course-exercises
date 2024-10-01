import pandas as pd
import numpy as np
# split dos dados entre informações para treino e teste
from sklearn.model_selection import train_test_split
# encoder dos dados em números para o modelo interpretar
from sklearn.preprocessing import LabelEncoder
# tabela de acertos e erros do modelo e seu número de precisão
from sklearn.metrics import confusion_matrix, accuracy_score
# algoritmo de classificação
from sklearn.ensemble import RandomForestClassifier

# lendo o arquivo com as informações que iremos trabalhar
credit = pd.read_csv('Credit.csv')

# preparando para encodar as informações não numéricas
labelencoder = LabelEncoder()

# filtrando somente as colunas aonde os dados são do tipo 'object' que são textos
for i in credit.select_dtypes(include='object'):
    if i != 'class': # excluindo a coluna com o nome class que não será inclusa
        credit[i] = labelencoder.fit_transform(credit[i])

# agora que temos somente números no nosso dataframe, precisamos transformar ele em um array do numpy
# o .values transforma automaticamente o intervalo de colunas em um array do tipo numpy como ja visto
# fazemos de 0:20 pois temos 20 colunas mas só queremos as primeiras 19, já separando as classes 
previsores = credit.iloc[:,0:20].values
# agora fazemos o mesmo processo acima mas somente com as classes
classes = credit.iloc[:,20] # todas as linhas mas somente a coluna 20

# agora precisamos separar nossos dados em dados de treinamento e dados de teste
x_training, x_test, y_training, y_test = train_test_split(
    previsores,
    classes,
    test_size=0.3,
    random_state=0) # garantindo que a divisão aleatória possa ser repetida pelo mesmo random_state number

# assim separamos as informações em x_training e x_test que serão as informações armazenadas nos 
# previsores, como definimos o test_size=0.3 a separação será de 30% para teste e 70% para treinar

# e também da mesma forma separamos os resultados em y_training e y_test que serão as informações que
# estão guardadas nas classes e que possuem a mesma separação de 30% para teste e 70% para treinar

print(x_training.shape)
print(x_test.shape)
print(y_training.shape)
print(y_test.shape)

# agora vamos configurar o algoritmo do modelo de machine learning
floresta = RandomForestClassifier(n_estimators=500, random_state=0)
floresta.fit(x_training, y_training)
# forest.fit(training_data, prediction_data)

# agora que nosso algoritmo de floresta está pronto para fazer as previsões, podemos iniciar os testes
previsoes = floresta.predict(x_test)

# agora que temos as previsoes do nosso algoritmo, precisamos comparar elas com os resultados existentes
# para isso criamos uma matriz de confusão (uma tabela indicando os acertos e erros do nosso modelo)

confusion = confusion_matrix(y_test, previsoes)

print(confusion)

# a matriz de confusão se lê da seguinte forma:

# [positivo verdadeiro (acerto), positivo falso (erro)]
# [negativo falso (erro), negativo verdadeiro (acerto)]

# agora para finalizarmos iremos imprimir a taxa de acerto do nosso modelo

accuracy = accuracy_score(y_test, previsoes)

print(f"{accuracy * 100}% accuracy")




