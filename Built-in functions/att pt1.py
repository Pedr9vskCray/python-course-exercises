import math

# atividade 1

def retornasub(num1, num2):
    return (abs(num1) - abs(num2))

print(retornasub(-200, 100))

print("")

# atividade 2

def returnsoma(num1, num2):
    soma = num1 + num2
    soma = min(10000, soma)
    soma = max(0, soma)
    return soma

print(returnsoma(20,20))
print(returnsoma(5000, 6000))
print(returnsoma(10, -20))

print("")

# atividade 3

def retornamenor(*args):
    return min(args)



print(retornamenor(-4, 5, 14, -2.5, 15, 0, -6, -19.4))

print("")

# atividade 4

def bhaskara(a,b,c) -> list:
    delta = pow(b, 2) - (4 * a * c)
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    return [x1, x2]

resultados = bhaskara(2,9,10)

print("xI = %.1f ; x2 = %.1f" %(resultados[0], resultados[1]))

print("")

# atividade 5

def lowerupper(text):
    return text.swapcase()

print(lowerupper("PEDRO é MUITO gente BOA"))