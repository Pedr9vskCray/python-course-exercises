# atividade 1

numbers = [int(input("Digite os números: ")) for num in range(0, 5)]

final = 0

for temp in numbers: final += temp

print("")

print("A média aritmética entre esses números é: %d" %(final/len(numbers)))

print("")

# atividade 2

somaloop = [int(input("Digite os números: ")) for num in range(0, 5)]

somafinal = 0

for item in somaloop:
    if item > 0: somafinal += item

print("")

print("A soma desses números é: %d" %(somafinal))

print("")

# atividade 3

arbit = int(input("Digite a quantidade de números a serem lidos: "))

print("")

arbitfinal = [int(input("Digite os números: ")) for num in range(0, arbit)]

arbitsoma = 0

for item in arbitfinal: arbitsoma += item

print("")

print("A soma desses números é: %d" %(arbitsoma))

print("")

# atividade 4

parimpar = [num for num in range(2, 11)]

for item in parimpar:
    print("%d é par." %item) if item % 2 == 0 else print("%d é ímpar." %item)

print("")

# atividade 5

text = str(input("Digite um string que contém espaços: "))

blank = 0

for letter in text:
    if letter == " ": blank += 1

print("")

print("A string [%s] possui %d espaços em branco" %(text,blank))





