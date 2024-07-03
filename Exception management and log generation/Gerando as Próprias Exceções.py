# no python caso desejado, é possível levantar exceções propositalmente para tratá-las
# de formas diferentes código adentro

# por exemplo, podemos usar a palavra chave raise para levantar um erro genérico

try:
    raise Exception("Erro genérico levantado.")
except:
    pass

# também é possível, gerar exceções padrões ao python de forma forçada

try:
    raise IndexError("Essa posição não existe ou não pode ser acessada.")
except:
    pass

# um exemplo prático do uso do levantamento personalizado de exceções

def positivecheck(number):
    if number > 0:
        return number
    else:
        raise ValueError("This number is not positive, thus the function failed.")

try:
    print(positivecheck(-4))
except ValueError as ve:
    print("An error has occurred: %s" %ve)

print("")

# geralmente utilizado em conjunto com o levantamento de erros está o assert
# assert é uma palavra reservada do python que faz um levantamento lógico aonde
# caso seja verdadeiro o código continua sua execução normalmente
# e caso seja falso, o código é interrompido e será retornado um AssertionError

def negativecheck(number):
    assert (number < 0) # caso o número seja maior que zero, o código será interrompido
    return number


try:
    print(negativecheck(4))
except AssertionError as ae:
    print("An error has occurred: %s" %ae)
    # note que o AssertionError não possui uma mensagem própria

print("")

# também é possível, durante o tratamento do erro, você fazer o levantamento do mesmo
# é um caso de uso bem específico, mas é interessante saber que é possível

array = [1, 2, 3, 4, 5]
try:
    print(array[10])
except IndexError as error:
    raise error


