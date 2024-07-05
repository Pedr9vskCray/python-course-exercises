# atividade 1

def retornomes():
    yield "janeiro"
    yield "fevereiro"
    yield "março"
    yield "abril"
    yield "maio"
    yield "junho"
    yield "julho"
    yield "agosto"
    yield "setembro"
    yield "outubro"
    yield "novembro"
    yield "dezembro"

for mes in retornomes():
    print(mes)

print("")

# atividade 2

def multiplica2(lista):
    for num in lista:
        yield 2*num

for i in multiplica2(range(1,11)):
    print(i)

print("")

# atividade 3

class Tabuada:
    def __init__(self, numero):
        self.numero = numero

    def __iter__(self):
        self.currentnum = 1
        return self

    def __next__(self):
        if self.currentnum < 11:
            retorno = self.numero * self.currentnum
            self.currentnum += 1
            return retorno
        else:
            raise StopIteration

tabuada5 = Tabuada(5)

for num in tabuada5:
    print(num)

print("")

# atividade 4

class Fatorial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        self.atual = self.x
        return self

    @staticmethod
    def calculafatorial(num):
        temp = 1
        for i in range(1, num+1):
            temp *= i
        return temp

    def __next__(self):
        if self.atual < self.y+1:
            retorno = Fatorial.calculafatorial(self.atual)
            self.atual += 1
            return retorno
        else:
            raise StopIteration

testefatorial = Fatorial(1, 10)
for num in testefatorial:
    print(num)

print("")

# atividade 5

for num,mes in enumerate(retornomes()):
    print(str(num+1) + " - " + mes)

print("")

idx = [i for i in range(1, 13)]
meses = [i for i in retornomes()]

stringmeses = " ".join((str(x) + "-" + y for x,y in zip(idx, meses)))

print(stringmeses)

print("")

# atividade 6

def criatexto(lista):
    return ".\n".join(lista)

frases = ["pedro é muito legal", "hoje é dia 3 de julho", "amanhã vai fazer muito frio"]

print(f"{criatexto(frases)}.")


