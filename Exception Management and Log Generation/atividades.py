# atividade 1

def convertesoma(text1: str, text2: str):
    try:
        num1 = float(text1)
        num2 = float(text2)
        return num1 + num2
    except ValueError as error:
        print("Ocorreu um erro: ", error)

print(convertesoma("140", "abc"))

print("")

# atividade 2

def acessarlista(lista: list, num: int):
    try:
        return lista[num]
    except IndexError:
        return None

print(acessarlista([1, 2, 3, 5, 7], 10))

print("")

# atividade 3

def receberusername():
    try:
        return str(input("Digite o seu nome de usuário: "))  
    except KeyboardInterrupt as kbi:
        print("\n\nVocê interrompeu o input.", kbi)
        return None

print(receberusername())

print("")

# atividade 4

class char:
    def __init__(self, character):
        if len(character) > 1:
            raise ValueError("character size cannot be greater than 1")
        else:
            self.__char = character

    def __returnchar(self):
        return self.__char

    def __setchar(self, new_character):
        if len(new_character) > 1:
            raise ValueError("character size cannot be greater than 1")
        else:
            self.__char = new_character

    character = property(__returnchar, __setchar)


letra = char("a")
print(letra.character)
letra.character = "b"
print(letra.character)
#letra.character = "brasil"
letra2 = char("abc")



        


