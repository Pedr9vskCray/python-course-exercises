# é possível iterar por uma função utilizando a palavra chave yield
# ao usar o yield, o estado da função é salvo desde a última vez que ela foi chamada
# funções iteráveis criadas e utilizadas dessa maneira são chamadas de funções geradoras

def ancora():
    yield 2
    yield 3
    yield 1

for num in ancora():
    print(num)

print("")

# como a função se tornou um objeto iterável, é possível utilizar métodos e comparações
# que podem ser utilizados com outros objetos iteráveis na mesma

print(2 in ancora())

print("")

# funções iteráveis não são instâncias de classes, objetos de uma classe ou variáveis
# elas são simplesmente funções que podem ser iteradas como se fossem, por exemplo, arrays

# é possível também criar iteradores utilizando uma função iterável
# e utilizar métodos como o next nesses iteradores

iterador = iter(ancora())
print(next(iterador))
print(next(iterador))
print(next(iterador))

print("")

# outra forma de implementar algo parecido com a função range() como já vimos anteriormente
# é utilizando o yield e uma função iterável da seguinte maneira

def personalrange(stop, start=0, step=1):
    temp = start
    while temp < stop:
        yield temp
        temp += step

for num in personalrange(13):
    print(num)





