# atividade 1

numeros = [1,10,6,7,8,10]

soma = 0

for num in numeros: soma += num

print("A soma dos números nesta lista é %d" %soma)

print("")

# atividade 2

valores = [num for num in range(1, 101)]

for num in valores: print(num)

print("")

# atividade 3

lista1 = [30,4,43,52,65,-10]

lista2 = [43,2,4,76,32,65,3]

uniqueval1 = [num for num in lista2 if num not in lista1]

uniqueval2 = [num for num in lista1 if num not in lista2]

uniquefinal = uniqueval1 + uniqueval2

print(uniquefinal)

print("")

# atividade 4

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

entrada = int(input("Digite o mês do ano em que você nasceu: "))

print("")

print("Você nasceu no mês de %s" %meses[entrada-1])

print("")

# atividade 5

fevereiro = [num for num in range(1, 29)]

dia = int(input("Digite o dia em que você nasceu: "))

fevereiro.remove(dia)

print("")

print(fevereiro)

