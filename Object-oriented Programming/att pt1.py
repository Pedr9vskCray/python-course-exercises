from typeguard import typechecked

# atividade 1

class Carro:
    def __init__(self, marca: str, potencia: str, consumo: str):
        self.marca = marca
        self.potencia = potencia
        self.consumo = consumo


opala = Carro("Opala", "171 cavalos", "6 km/l")
pumaGTE = Carro("PumaGTE", "60 cavalos", "13km/l")

print("%s: Potência: %s ; Consumo (km/L): %s" %
      (opala.marca, opala.potencia, opala.consumo))
print("%s: Potência: %s ; Consumo (km/L): %s" %
      (pumaGTE.marca, pumaGTE.potencia, pumaGTE.consumo))

print("")

# atividade 2


class Pessoa:
    def __init__(self, cpf: str, nome: str, dependente=None):
        self.cpf = cpf
        self.nome = nome
        self.dependente = dependente


filho = Pessoa("965.842.200-44", "Rodrigo")
pai = Pessoa("802.986.670-45", "Fernando", filho)

# pai
print("%s: CPF: %s ; Dependente: %s" % (pai.nome, pai.cpf, pai.dependente.nome))

# filho
print("%s: CPF: %s ; Dependente: %s" %(filho.nome, filho.cpf, filho.dependente))

print("")

# atividade 3

@typechecked
class Veiculo:
    def __init__(self, peso: float, potencia: int, rodas: int):
        self.peso = peso
        self.potencia = potencia
        self.rodas = rodas

    def dist_percorrida(self):
        temp = (self.potencia / self.peso) * 1000
        distancia = "Distância Percorrida: %.2f quilômetros." %temp
        return distancia

class Onibus(Veiculo):
    def __init__(self, peso, potencia, rodas, ano: int):
        Veiculo.__init__(self, peso, potencia, rodas)
        self.ano = ano


class Moto(Veiculo):
    def __init__(self, peso, potencia, rodas, marca: str):
        Veiculo.__init__(self, peso, potencia, rodas)
        self.marca = marca


class Carro(Veiculo):
    def __init__(self, peso, potencia, rodas, portas: int):
        self.portas = portas
        Veiculo.__init__(self, peso, potencia, rodas)


opala = Carro(1125, 171, 4, 4)
r3_Monster = Moto(171, 55, 2, "Yamaha")
sênior = Onibus(3350, 340, 6, 2018)

print("Opala: Peso: %d kg; Potência: %d cavalos; Rodas: %d, Portas: %d" %(opala.peso, opala.potencia, opala.rodas, opala.portas))
print("R3_Monster: Peso: %d kg; Potência: %d cavalos; Rodas: %d, Marca: %s" %(r3_Monster.peso, r3_Monster.potencia, r3_Monster.rodas, r3_Monster.marca))
print("Micro-Ônibus Sênior: Peso: %d kg; Potência: %d cavalos; Rodas: %d, Ano: %d" %(sênior.peso, sênior.potencia, sênior.rodas, sênior.ano))

print("")

# atividade 4

print(opala.dist_percorrida())
print(r3_Monster.dist_percorrida())
print(sênior.dist_percorrida())

