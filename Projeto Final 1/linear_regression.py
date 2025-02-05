import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# criando a classe

# x = variável independente
# y = variável dependente

class Linear:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __correlation(self):
        a = np.cov(self.x, self.y, bias=True)[0][1]
        b = np.sqrt(np.var(self.x) * np.var(self.y))
        return a / b

    def __inclination(self):
        stdx = np.std(self.x)
        stdy = np.std(self.y)
        return self.__correlation() * (stdy / stdx)

    def __interception(self):
        avgx = np.average(self.x)
        avgy = np.average(self.y)
        return avgy - (self.__inclination() * avgx)

    def regression(self, v):
        return self.__interception() + (self.__inclination() * v)

    def plotdata(self, name_x="X Axle", name_y="Y Axle", title="Linear Regression Graph"):

        plt.xlabel(name_x)
        plt.ylabel(name_y)
        plt.title(title)

        plt.scatter(self.x, self.y)

        x_min = min(self.x)
        x_max = max(self.x)

        x_line = [x_min, x_max]
        y_line = [self.regression(x_min), self.regression(x_max)]
        plt.plot(x_line, y_line, color="red")

        plt.show()

# dados de teste

idade = np.array([18, 23, 25, 33, 34, 43, 48, 51, 58, 63, 67])
custo = np.array([871, 1100, 1393, 1654, 1915, 2100, 2356, 2698, 2959, 3000, 3100])

# testando o modelo de regressão linear

model = Linear(idade, custo)

print(model.regression(54))

model.plotdata()