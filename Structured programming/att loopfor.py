import math

# atividade 1

text = str(input("Digite um texto que contém espaços: "))

stringlen = 0

for letter in text:
    if letter != " ": stringlen += 1

print("")

print("A string [%s] possui %d caracteres sem contar os espaços" %(text,stringlen))

print("")

# atividade 2

fator = int(input("Digite um número: "))

fatorial = fator

for num in range(fator-1, 0, -1): fatorial *= num

print("")

print("O fatorial de %d é %d"%(fator, fatorial))

print("")

# atividade 3

qnt = int(input("Digite a quantidade de strings que você deseja ler: "))

print("")

texts = [str(input("Digite a string: ")) for txt in range(qnt)]

joinedtext = "-".join(texts)

print("")

print("A string concatenada = [%s]" %joinedtext)

print("")

# atividade 4

number = int(input("Digite um número para ver sua tabuada de divisão: "))

tabua = [num for num in range(number, (number*10)+1, number)]

print("")

for num in tabua:
    temp = num / number
    print("%d : %d = %d" %(num, number, temp))

print("")

# atividade 5

triple = [num for num in range(2, 31)]

print("")

def crivoerastostenes(numeros):
    for num in numeros:
        if num % 2 == 0 and num != 2:
            numeros.remove(num)

    for num in numeros:
        if num % 3 == 0 and num != 3:
            numeros.remove(num)

    for num in numeros:
        if num % 5 == 0 and num != 5:
            numeros.remove(num)

    for num in numeros:
        if num % 7 == 0 and num != 7:
            numeros.remove(num)

    for primo in numeros:
        print("%d é primo" %primo)

crivoerastostenes(triple)



