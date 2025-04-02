# atividade 6

def encontrado(lista, valor):
    for elem in lista: return True if valor == elem else False

array = ['pedro', 'thiago', 'joão']

print(encontrado(array, 'pedro'))

print("")

# atividade 7

def idxencontrado(lista, valor) -> tuple:
    for idx,elem in enumerate(lista): return (True,idx) if elem == valor else False

print(idxencontrado(array, 'pedro'))

print("")

# atividade 8

def printtype(*args):
    for thing in args:
        print(type(thing))

printtype("pedro", 123, True)

print("")

# atividade 9

def quote(func):
    def inner_func(text):
        return '"' + func(text) + '"'
    return inner_func

@quote
def lowerchar(text):
    return text.lower()

print(lowerchar('PEDRO É UM CARA LEGAL'))

print("")

# atividade 10

def recursiva(num):

    if num == 0:
        return print(0)

    print(num // 3)
    recursiva(num-1)

recursiva(10)
    

