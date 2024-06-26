# atividade 1

banco = "100000"
banco = int(banco)
banco -= 1000
print("Meu saldo bancário é %d" %banco)

print("")

# atividade 2

saldo = 12439
zerado = None
if saldo <= 0:
    zerado = True
else:
    zerado = False

print("Vazio") if zerado else print("Cheio")

print("")

# atividade 3

altura = 1.85
altura = int(altura)
print("Minha altura arredondada é: %d" %(altura))