"""
Enunciado
Dado um array de inteiros e o seu número de elementos, crie uma função recursiva que inverta a posição dos seus elementos.
"""


def inverter(lista):
    if not lista:  # lista vazia, retorna ela mesma
        return lista
    return lista[-1:] + inverter(lista[:-1])


print(inverter([1, 2, 3, 4, 5]))