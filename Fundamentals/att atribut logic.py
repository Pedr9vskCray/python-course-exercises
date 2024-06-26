# atividade 1

prova1 = float(input("Digite a nota da Prova 1: "))
prova2 = float(input("Digite a nota da Prova 2: "))

media = (prova1 + prova2) / 2

aprovado = None

print("")

if (media >= 7) or (prova1 >= 5 and prova2 >= 5):
    aprovado = True
else:
    aprovado = False

print("Aprovado!") if aprovado else print("Reprovado.")

print("")

# atividade 2

passwd = "123abc"

entrada = str(input("Digite a senha para acessar o sistema: "))

if entrada == passwd:
    print("\nAcesso validado.")
else:
    print("\nSenha incorreta, por favor tente novamente.")
