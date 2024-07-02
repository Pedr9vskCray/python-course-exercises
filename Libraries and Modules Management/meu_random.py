"""
Módulo contendo 1 função:

- get_random_lista(inicial, final, tam): Retorna uma lista de números randômicos
"""
from random import randrange

def get_random_lista(inicial, final, tam):
    """
    Retorna uma lista de números randômicos

    Parâmetros:
    
    inicial -> menor valor possível que pode existir dentro da lista
    final ->  maior valor  possível que pode existir dentro da lista
    tam -> quantidade de elementos dentro da lista
    """
    output = []
    for i in range(tam):
        temp = None
        temp = randrange(inicial, final+1)
        output.append(temp)
    
    return output






