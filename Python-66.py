"""
Enunciado
Faça uma função que recebe uma lista de números e retorna a média aritmética dos elementos dessa lista.
"""


def media(numeros):
    soma = 0
    for num in numeros:
        soma = soma + num
    media = soma/len(numeros)
    print(f"{media}")


lista = [1, 2, 3, 4, 5]
media(lista)