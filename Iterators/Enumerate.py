# para percorrer um objeto iterável, podemos utilizar o método enumerate
# a vantagem do método é que seu retorno é uma tupla, com o valor e a posição do mesmo
# juntando por exemplo formas de iterar direto no objeto iterável utilizando for
# com a forma de iterar por meio do range(len(objeto)) 

lista = ["pedro", "thiago", "joão", "luiz", "rodolfo", "ronaldo", "gabriel"]

for idx,nome in enumerate(lista):
    print(str(idx) + " - " + nome) 
    # idx -> é a posição
    # nome -> é o valor dentro da lista

print("")

# é possível utilizar o enumerate() em conjunto com o range()

for idx,num in enumerate(range(0, 21, 5)):
    print(str(idx) + " - " + str(num))

