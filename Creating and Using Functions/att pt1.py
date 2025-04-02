# atividade 1

def e_negativo(num):
    return False if num > 0 else True

print(e_negativo(-14))

print("")

# atividade 2

def somalista(lista):
    soma = 0
    for num in lista: soma += num
    return soma
    
numeros = [1,3,5,7,9]

print(somalista(numeros))

print("")

# atividade 3

def contavogais(text):
    qntvogais = 0
    listavogais = ["a","e","i","o","u","A","E","I","O","U"]
    for letter in text: qntvogais += 1 if letter in listavogais else 0

    print("%s tem %d vogais" %(text, qntvogais))

contavogais("pedro")

print("")

# atividade 4

def returnlast(text):
    return text[-1]

print(returnlast("pedro"))

print("")

# atividade 5

def somasubtrac(num1, num2, opera):
    if opera == "soma":
        return num1 + num2
    elif opera == "subtração":
        return num1 - num2

print("%d + %d = %d" %(10, 30, somasubtrac(10,30,"soma")))
print("%d - %d = %d" %(10, 30, somasubtrac(10,30,"subtração")))

