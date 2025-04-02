# função para a atividade 2

def abbreviate_name(name: str):
    temp = name.split(" ")
    ret = []
    for word in temp:
        ret.append(word[0].upper())
    return tuple(ret)