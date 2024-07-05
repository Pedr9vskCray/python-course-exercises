# quando se possui, por exemplo uma lista com outras listas dentro
# para acessar as variáveis das sublistas geralmente utilizamos 2 laços for dessa forma:

lista = [['pedro', 'programador'], ['joão', 'gerente'], ['romário', 'motorista']]

for element in lista:
    for info in element:
        print(info)
    print("")

# mas, para evitar o uso desnecessário de dois laços for, nós podemos fazer o unpacking
# dessas várias listas dentro de listas utilizando um laço só

# chamamos isso de unpacking 

array = [['carro', '2004'], ['moto', '2015'], ['bicicleta', '2020'], ['trator', '2013']]

for objeto,ano in array:
    print(objeto + " - " + ano)

print("")

# é possível também, fazer o unpacking é uma função iterável que vai retornar uma lista

def generator():
    yield [1, 1, -1, 7]
    yield [1, -1, 2, 3]
    yield [-2, 1, 1, 9]

for x, y, z, R in generator():
    print(f"|{x}|{y}|{z}|{R}")

print("")

# é possível utilizar funções geradoras aninhadas e fazer o unpacking das mesmas

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    for i in gen1():
        yield i, 'a'
        yield i, 'b'
        yield i, 'c'

for x,y in gen2():
    print(str(x) + " - " + str(y))


