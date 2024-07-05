# para juntar objetos iteráveis no python é possível utilizar o método join
# por exemplo, como vimos anteriormente podemos juntar string utilizando método join

texto1 = "abc"
textofinal = "-".join(texto1)
print(textofinal)

print("")

# o mesmo pode ser feito com listas

lista = ["pedro", "thiago", "joão"]
nomes = "_".join(lista)
print(nomes)

print("")

# é possível utilizar o método join, percorrendo um objeto iterável como um array de letras

letras = ['a', 'b', 'a', 'c', 'a', 'x', 'i']
texto = "minha fruta favorita é o " + "".join(letras)
print(texto)

print("")

# também é possível usar o join um objeto iterável gerado por list comprehension

fevereiro = "-".join([str(i) for i in range(29)])
print(fevereiro)

print("")

# é possível também utilizar o join em uma função geradora

def anos():
    for i in range(2005, 2025):
        yield str(i)

anos_passados = ".".join(anos())

print(anos_passados)