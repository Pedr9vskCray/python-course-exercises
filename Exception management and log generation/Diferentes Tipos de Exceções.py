# como visto anteriormente, podem existir códigos dentro do try que retornam diferentes
# tipos de erros, assim, para tratar múltiplos erros é necessário especificar qual ação
# o programa deve tomar dependendo do erro que foi gerado

# para tratar qualquer erro, podemos usar o caso genérico

print("Inicio")
try:
    funçãoquenãoexiste()
except Exception as error: # o primeiro erro, independente de qual seja será capturado aqui
    print("Ocorreu um erro: %s" %error)
finally:
    print("Fim")

print("")

# para casos mais específicos é preciso especificar qual erro desejamos tratar

print("Começo")
try:
    lista = [1, 2, 3, 5, 7]
    numero = 1
    hashset = {lista: "teste"} # conserte o erro nessa linha para verificar
    funçãoquenãoexiste()
except TypeError:
    print("Listas não podem ser usadas como chaves para dicionários.")
except NameError:
    print("A função que você tentou executar não existe.")

# note que o primeiro erro detectado é aonde o programa sai
# mas caso você conserte o erro, o programa vai passar para o segundo except

# ou seja, ficou claro que nós podemos ter diferentes erros em um único try
# e que podemos tratar cada um desses erros individualmente utilizando vários excepts
# ou podemos tratar o primeiro erro de forma genérica

print("")

# o python pode ter vários tipos de erro já implementados de forma padrão nele

# o site com a lista de todos os erros padrões do python é:
# https://docs.python.org/3/library/exceptions.html



