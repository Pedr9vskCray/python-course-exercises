from datetime import datetime

# atividade 6

def countinstances(string, letter):
    return string.count(letter)

text = "o meu nome é pedro"
letter = "o"

print("Na string [%s] a letra %s aparece %d vezes!" %(text, letter, countinstances(text, letter)))

print("")

# atividade 7

def returninstances(string, letter):
    returnlist = []
    for idx,char in enumerate(string):
        if char == letter:
            returnlist.append(idx)
    return returnlist

print(returninstances("felipe henrique", "e"))

print("")

# atividade 8

def filtro(text, bannedwords):
    for word in bannedwords:
        if word in text:
            text = text.replace(word, "*")

    return text
                
chat = "eu gosto muito de azul"
bannedwords = ["muito", "azul"]

print(filtro(chat, bannedwords))

print("")

# atividade 9

def returnifupper(text):
    returnvar = True
    for letter in text:
        if letter.isupper():
            pass
        else:
            returnvar = False
    
    return returnvar

print(returnifupper("Pedro"))

print("")

# atividade 10

def extractint(textlist):
    numbers = []
    for item in textlist:
        if item.isdigit():
            numbers.append(int(item))
    numbers.sort()
    return numbers

inputarray = ['pedro', '12', 'felipe', 'True', 'False', '7', '19']

print(extractint(inputarray))

print("")

# atividade 11

nascimento = str(input("Digite sua data de nasicmento dd/mm/aa: "))

nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

today = datetime.today()

print("")

print("Você já viveu %d dias" %(today - nascimento).days)

print("")

# atividade 12

proximoaniver = str(input("Digite a data do seu próximo aniversário dd/mm/aa: "))

proximoaniver = datetime.strptime(proximoaniver, "%d/%m/%Y")

hoje = datetime.today()

print("")

print("Faltam %d dias pro seu próximo aniversário!" %(proximoaniver - hoje).days)








