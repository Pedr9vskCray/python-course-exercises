# atividade 1

nome = "Pedro José"
primeiro, segundo = nome.split(" ")

print(primeiro, segundo)

print("")

# atividade 2

texto = str(input("Digite o nome de um animal qualquer: "))
size = len(texto)
texto = texto[:size-1]

print(texto)

print("")

# atividade 3

vogais = "AaEeIiOoUu"
animal = str(input("Digite o nome de outro animal qualquer: "))
final = [letra for letra in animal if letra in vogais]
print(f"O nome que você digitou contém as seguintes vogais: {final}")

print("")

# atividade 4

cidade = str(input("Digite o nome da cidade aonde você mora: "))
cidade = "ABC" + cidade
print(cidade)

