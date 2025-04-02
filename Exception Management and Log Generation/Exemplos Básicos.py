# em python e em outros programas, é possível que seja necessário fazer o tratamento
# de casos específicos conhecidos como exceções, que nada mais são que erros no código
# mas erros que nós esperamos e sabemos como tratar

# por exemplo

print("Inicio")
lista = [1 ,2 ,3, 5, 7]
try:
    print(lista[10]) # tentamos printar um elemento em uma posição que não existe
except:
    print("Ocorreu um erro")
print("Fim")

print("")

# caso não ocorra erro o fluxo do código segue normalmente

print("Start")
try:
    print(lista[2])
except:
    print("Ocorreu um erro")
print("Fim")

print("")

# é possível também tratar a exceção, por exemplo salvando o erro
# e mostrando-o de volta para o usuário em uma mensagem preparada

print("Começo")
try:
    print(lista[10])
except Exception as error: # criamos um alias para a exceção gerada, chamada error
    print("Ocorreu um erro: %s" %error) # printamos a exceção de volta para o usuário
print("Fim")

print("")

# a forma mostrada acima trata de todas as exceções, mas também é possível tratar somente
# uma exceção específica, por exemplo

texto = "brasil"
try:
    int(texto)
except ValueError as ve:
    print("Ocorreu um erro: %s" %ve) # assim tratamos somente do erro ValueError

print("")

# outra parte do tratamento de erros é o finally, que é um bloco de código
# que será sempre executado, independente de ocorrer um erro ou não

print("Inicio do programa")
try:
    #aaaaa = 1 <- caso removermos a existência do objeto, um erro será produzido
    print(aaaaa)
except NameError as ne:
    print("Ocorreu um erro %s" %ne)
finally:
    print("Fim do programa") # mas essa linha sempre será executada, com ou sem erro

print("")

# assim como o finally, nós temos mais uma cláusula opcional no tratamento de exceções
# o except define um bloco de código que só será executado caso não ocorra nenhum erro

print("Começo do programa")
try:
    temp = [1, 2, 3, 5, 7]
    tempnum = 14
    hashset = {tempnum: "teste"}
except TypeError as te:
    print("Ocorreu um erro: %s" %te)
else:# será executado somente quando o programa não tiver erros
    print("O programa foi executado sem erros")
finally:
    print("Fim do programa")

# dessa forma a esquematização do gerenciamento de exceções é essa:

try: # código que pode dar erro
    pass

except: # código que vai ser executado caso ocorra um erro
    pass

else: # código que vai ser executado caso não ocorra um erro
    pass

finally: # código que vai ser executado sempre, independente da existência ou não de um erro
    pass


