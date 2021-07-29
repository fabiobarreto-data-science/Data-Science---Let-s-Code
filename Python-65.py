"""
Enunciado
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
"""


def somaElementos(lista):
    soma = 0
    for c in lista:
        soma = soma + c
    print(soma)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

somaElementos(lista)