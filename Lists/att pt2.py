# atividade 6

objetos = {"livro": "leitura", "carro": "transporte", "machado": "lenhar"}

selecionar = str(input("Digite o nome do objeto do qual você deseja saber a função: "))

print("")

print("A função do %s é %s" %(selecionar, objetos[selecionar]))

print("")

# atividade 7

negat = [num for num in range(-30, -19, 1)]

print(negat)

print("")

# atividade 8

num4_100 = [num for num in range(4, 101) if num % 4 == 0]

print(num4_100)

print("")

# atividade 9

num0_100 = [num for num in range(101) if num % 10 == 0]

print(num0_100)

print("")

# atividade 10

num0_20 = ['0' if num % 10 == 0 else '-' for num in range(21)]

print(num0_20)