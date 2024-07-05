# para criar sua própria classe iterável no python
# é preciso definir dois métodos iniciais já usados anteriormente
# o método __iter__ que é um construtor especial das classes iteráveis
# e o método __next__ que é utilizado para retornar o próximo elemento do objeto iterável

class numbercollection:
    def __init__(self, maxnum): # método de inicialização padrão de classe
        self.max = maxnum

    def __iter__(self): # método construtor das classes iteráveis
        self.currentnum = 0 # define o primeiro número da nossa classe
        return self

    # os dois métodos acima são executados implicitamente na inicialização da classe

    # já o método __next__ é chamado sempre que for criado por exemplo um laço for
    # ou sempre que o método em si for chamado

    def __next__(self): # método utilizado para retornar o próximo elemento
        if self.currentnum < self.max:
            retorno = self.currentnum
            self.currentnum += 1 # soma +1 ao número inicial e subsequentes
            return retorno
        else:
            raise StopIteration("Não existe mais elementos para continuar a iteração")

collection = numbercollection(7)

# sempre que iteramos sobre um objeto iterável utilizando o for ou outra forma de iteração
# o método __next__ desse objeto iterável é chamado

for num in collection:
    print(num)

print("")

# perceba que o resultado é bem similar com algo que já vimos antes
# o método range() funciona exatamente da mesma maneira que vimos implementada acima

for num in range(7):
    print(num)

print("")

# e assim vale o mesmo para qualquer objeto iterável built-in do python
# podemos também tentar iterar para fora da quantidade de elementos dentro do objeto
try:
    iterador = iter(collection)
    next(iterador)
    next(iterador)
    next(iterador)
    next(iterador)
    next(iterador)
    next(iterador)
    next(iterador)
    next(iterador)
except StopIteration:
    print("Não há mais elementos para iterar.")

print("")

# também é possível utilizar métodos que podem ser utilizados em outros objetos iteráveis
# no nosso objeto iterável criado

print(4 in collection)
print(14 not in collection)

# para definir se uma classe é ou não um objeto iterável, basta adicionarmos ou não
# o método construtor de classes iteráveis __iter__






            