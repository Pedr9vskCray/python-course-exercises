# atividade 1
from random import randrange
import calc_python as cpy
from meu_random import get_random_lista as grl
import sys
import os

def testepar(num):
    if num % 2 == 0:
        return "par" 
    else:
        return "ímpar"

numero1 = randrange(2, 100)
numero2 = randrange(2, 100)

print(f"o número {numero1} é {testepar(numero1)}")
print(f"o número {numero2} é {testepar(numero2)}")

print("")

# atividade 2

soma = 0
for i in range(0, 100):
    soma += randrange(2, 100)

print(soma)

print("")

# atividade 3

print("Somando os números %d + %d = %d" %(numero1, numero2, cpy.sumnum(numero1, numero2)))
print("Subtraindo os números %d - %d = %d" %(numero1, numero2, cpy.subnum(numero1, numero2)))

# printando a documentação

print(cpy.__doc__)
print(cpy.subnum.__doc__)
print(cpy.sumnum.__doc__)

print("")

# atividade 4

random_array = grl(1, 100, 25)
print(random_array)

print("")

# atividade 5

os.system("python teste_programa.py 10 15")