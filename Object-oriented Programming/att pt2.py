# atividade 5

class Veiculo:
    def __init__(self, peso, potencia, rodas, marca):
        self.peso = peso
        self.potencia = potencia
        self.rodas = rodas
        self.marca = marca

    def distpercorrida(self):
        distancia = (self.potencia / self.peso) * 1000
        return distancia

    def __lt__(self, foo): # foo é uma referência ao outro objeto utilizado na comparação
        return self.potencia < foo.potencia

    def __gt__(self, foo):
        return self.potencia > foo.potencia
        


class Onibus(Veiculo):
    def __init__(self, peso, potencia, rodas, marca):
        Veiculo.__init__(self, peso, potencia, rodas, marca)


class Moto(Veiculo):
    def __init__(self, peso, potencia, rodas, marca):
        Veiculo.__init__(self, peso, potencia, rodas, marca)


class Carro(Veiculo):
    def __init__(self, peso, potencia, rodas, marca):
        Veiculo.__init__(self, peso, potencia, rodas, marca)

onibus = Onibus(3350, 400, 6, "Volkswagen")
moto = Moto(250, 50, 2, "Yamaha")
carro = Carro(1350, 100, 4, "Honda")

print(onibus > carro)
print(onibus < moto)
print(moto > carro)

print("")

# atividade 6

class Negativo:
    def __init__(self, numero):
        if numero > 0:
            print("O número não pode deixar de ser negativo.")
        else:
            self.numero = numero

    def __lt__(self, foo):
        return self.numero < foo.numero

    def __gt__(self, ham):
        return self.numero > ham.numero

    def __sub__(self, bar):
        temp = self.numero - bar.numero
        if temp > 0:
            print("O número não pode deixar de ser negativo.")
        else:
            self.numero = temp
    
    def __modnumero(self, newnumero):
        if newnumero > 0:
            print("O número não pode deixar de ser negativo.")
        else:
            self.numero = newnumero
    
    def __retornanumero(self):
        return self.numero

    info = property(__retornanumero, __modnumero) #property(fget, fset, fdel)

num1 = Negativo(-4)
num2 = Negativo(-14)
num1 - num2
print(num1 < num2)
print(num1.info)
num1.info = 14
num2.info = -2
print(num2.info)


print("")

# atividade 7

def testeprimitivo(objeto):
    return isinstance(objeto, (int, float, str, bool))

print(testeprimitivo([1, 3, 5, 7]))
print(testeprimitivo("pedro"))
