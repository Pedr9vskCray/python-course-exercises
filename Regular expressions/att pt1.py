import re

# atividade 1

numeros = '35'
info = re.search('^([2][0-9])|([3][0-5])$', numeros)
if info != None:
    print("Número válido.", info.group())
else:
    print("Número inválido.")

print("\n")

# atividade 2

frase = 'eu amo python'
info = re.findall('python', frase)
if len(info) != 0:
    print("A palavra python está na string.")
else:
    print("A palavra python não foi encontrada na string.")

print("\n")

# atividade 3

dia = 'Sexta-Feira'
rexpress = '^(Segunda-Feira|Terça-Feira|Quarta-Feira|Quinta-Feira|Sexta-Feira|Sábado|Domingo)$'
info = re.search(rexpress, dia)
if info != None:
    print(f"{info.group()} é um dia da semana válido.")
else:
    print("Dia da semana inválido.")

print("\n")

# atividade 4

telefone = '95225478'
info = re.search('^([0-9]{8})$', telefone)
if info != None:
    print("Número de telefone válido -> ", info.group())
    info2 = re.search('^95([0-9]{6})$', telefone)
    if info2 != None:
        print('Seu número de telefone foi bloqueado, por favor aguarde.')
    else:
        print('Seu telefone é permitido e não foi bloqueado.')
else:
    print("Número de telefone inválido.")

print("\n")

# atividade 5

texto = 'meu nome é pedro e eu estou sorrindo e rindo enquanto estou saindo'
info = re.findall('([\w]+indo|ando|endo)+', texto)
if info != None:
    print(info)

print("\n")

# atividade 6

hora = '23:59'
info = re.search("^([0-1][0-9]|[2][0-3]):([0-5][0-9])$", hora)
if info != None:
    print("Horário válido ->", info.group())
else:
    print("Horário inválido.")

print("\n")

# atividade 7

texto = '420 - 69'
info = re.search('^ *(\d+ *(-|\+) *\d+) *$', texto)
if info != None:
    print("Conta válida ->", info.group())
else:
    print("Conta inválida.")