lista = [[0, 3, 5, 1], 2, 3, [2, [5, 6, 7, [1, 4, 6]], 3], 2, [3, 5, 10, [6]]]


def lerLista(lista):
    soma = 0
    for contador in lista:
        if type(contador) == int:
            soma = soma + contador
        elif type(contador) == list:
            soma = soma + lerLista(contador)

    return soma


print(lerLista(lista))
