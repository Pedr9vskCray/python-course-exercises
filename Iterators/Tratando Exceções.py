# eventualmente um iterador pode gerar um erro
# por exemplo quando tentamos iterar além da quantidade de elementos existentes

# quando esse erro acontece, nós podemos fazer o tratamento dele da mesma forma que antes
# utilizando o try/except

lista = [1, 2, 3, 4]
iterador = iter(lista)

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except StopIteration:
    print("não existem mais elementos para iterar")

print("")

# caso seja da nossa vontade, também é possível reproduzir isso dentro de um laço while

iterador2 = iter(lista)

while True:
    try:
        print(next(iterador2))
        print(next(iterador2))
        print(next(iterador2))
        print(next(iterador2))
        print(next(iterador2))
    except:
        break
