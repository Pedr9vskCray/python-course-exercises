import os
import csv

# atividade 1

att1 = []

with open("exercicio1.txt", "rt") as text:
    data = text.read()
    for info in data:
        if info != "\n":
            att1.append(info)

print(att1)

print("\n")

# atividade 2

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    @staticmethod
    def extrair_produtos():
        produtos = []
        with open("exercicio2.txt", "rt") as text:
            data = text.readlines()
            for info in data:
                nome,valor = info.split(" ", 1)
                temp = Produto(nome, valor)
                produtos.append(temp)
        return produtos
        
produtos = Produto.extrair_produtos()

for produto in produtos:
    print(f"Nome -> {produto.nome} | Valor -> {produto.valor}")

print("\n")

# atividade 3

with open("atividade3.txt", "wt") as text:
    for i in range(101):
        text.write(f"{str(i)}\n")

# atividade 4

with open("atividade4.txt", "wt") as text:
    for i in range(1,101):
        if i % 3 == 0:
            text.write(f"{str(i)}\n")

# atividade 5

def fazer_registro(**info):
    with open("registros.csv", "w", newline="") as text:
        mywriter = csv.writer(text, delimiter=";")
        mywriter.writerow(['nome', 'grau de parentesco'])
        for key,value in info.items():
            mywriter.writerow([key, value])

def ler_registro() -> dict:
    with open("registros.csv", "r") as text:
        data = {}
        myreader = csv.reader(text, delimiter=";")
        for info in myreader:
            if info[0] == 'nome' and info[1] == 'grau de parentesco':
                pass
            else:
                data[info[0]] = info[1]
        return data

#fazer_registro(pedro="filho", thiago="tio", joão="pai", maria="mãe", juliana="tia")
for key,value in ler_registro().items():
    print(f"{key} -> {value}")