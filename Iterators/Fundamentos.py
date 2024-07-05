# no python, iteradores são objetos que podem ser percorridos sequencialmente
# nós já vimos e estudamos 4 desses tipos de objetos

lista = [1,2,3,4] # arrays
tupla = (4,3,2,1) # tuples
hashset = {1: "valor1", 2: "valor2", 3: "valor3", 4: "valor4"} # hashsets ou dicts
sets = {10,20,30,40} # sets

# com um objeto iterável, é possível a partir dele criar uma classe que também é iterável
# e quando criamos essa classe por exemplo, podemos utilizar métodos como o método next
# que chama o próximo elemento no objeto iterável que utilizamos para criar a classe

array = [1, 2, 3, 5, 7]
foo = iter(array) # foo é um objeto iterador da lista
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(next(foo))
print(type(foo))

# quando chamamos o método next quando ele não possui mais elementos para iterar
# ele retorna um erro

try:
    print(next(foo))
except StopIteration:
    print("Não há mais elementos para iterar.")
