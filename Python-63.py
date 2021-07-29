"""
Enunciado
Faça uma função que receba duas listas e retorne o produto item a item dessas listas.

Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].
"""


def multListas(lista1, lista2):
    for c in range(0, 3):
        multiplica = lista1[c]*lista2[c]
        print(f"{multiplica} ", end="")


lista1 = [1, 4, 3]
lista2 = [3, 5, 1]
multListas(lista1, lista2)