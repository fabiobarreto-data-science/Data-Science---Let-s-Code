lista = [4, 7, 3, 8, 2, 1, 5, 6]
"""Aprenndendo a essência do Bubble Sort"""

def bubble_sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) -1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


print(bubble_sort(lista))
