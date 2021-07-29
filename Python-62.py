"""
Enunciado
Faça uma função que recebe duas listas e retorna a soma item a item dessas listas.

Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].
"""


def somaListas(lista1, lista2):
    for c in range(0, len(lista1)):
        lista_soma = lista1[c] + lista2[c]
        print(f"{lista_soma} ", end="")


lista_soma = []
lista1 = [1, 4, 3]
lista2 = [3, 5, 1]

somaListas(lista1, lista2)