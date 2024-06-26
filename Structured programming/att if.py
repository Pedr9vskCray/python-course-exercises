# atividade 1

saldo = float(input("Por favor, digite seu saldo bancário: "))

print("Saldo positivo") if saldo > 0 else print("Saldo negativo")

print("")

# atividade 2

cpf = "384.159.720-32"

senha = str(input("Por favor digite sua senha: "))

print(cpf) if senha == "abc123" else print("Sua senha está incorreta.")

print("")

# atividade 3

idade = int(input("Por favor digite a sua idade: "))

if idade <= 3:
    print("Você é um bebê")
elif idade <= 13 and idade > 3:
    print("Você é uma criança")
elif idade <= 18 and idade > 13:
    print("Você é um adolescente")
elif idade <= 65 and idade > 18:
    print("Você é um adulto")
elif idade > 65:
    print("Você é um idoso")

print("")

# atividade 4

print("Calculadora")
print("")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operation = str(input("Escolha a operação desejada (+, -, /, *): "))

print("")

match operation:
    case "+":
        end = num1 + num2
        print("%.1f + %.1f = %.1f" %(num1,num2,end))
    case "-":
        end = num1 - num2
        print("%.1f - %.1f = %.1f" %(num1,num2,end))
    case "/":
        end = num1 / num2
        print("%.1f / %.1f = %.1f" %(num1,num2,end))
    case "*":
        end = num1 * num2
        print("%.1f * %.1f = %.1f" %(num1,num2,end))
