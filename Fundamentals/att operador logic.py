# atividade 1

faltarComida = False
diaSabado = True

if faltarComida or diaSabado:
    print("Eu preciso ir ao mercado.")
else:
    print("Eu não preciso ir ao mercado.")

print("")

# atividade 2

sinalVermelho = False
carroDireita = False
carroEsquerda = False

if sinalVermelho and (not carroDireita and not carroEsquerda):
    print("Posso atravessar a rua.")
else:
    print("Não posso atravessar a rua.")

print("")

# atividade 3

if sinalVermelho or (not carroDireita and not carroEsquerda):
    print("Posso atravessar a rua.")
else:
    print("Não posso atravessar a rua.")



