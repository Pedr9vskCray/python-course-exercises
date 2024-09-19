# função para a atividade 1

def strip_names(name: str):
    temp = name.split(" ")
    return (temp[0], temp[-1])

print(strip_names('pedro josé dos prazeres lobão'))