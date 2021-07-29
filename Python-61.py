"""
Enunciado
Faça uma função que recebe uma lista de palavras e retorna uma lista contendo as mesmas palavras da lista anterior, porém escritas em caixa alta.
"""


def palavrasMaiusculas(lista):
    lista2 = []
    for c in lista:
        x = c.upper()
        lista2.append(x)
    print(lista2)


lista = ["Mercúrio", "Vênus", "Terra", "Marte", "Júpiter", "Saturno", "Netuno", "Urano"]


palavrasMaiusculas(lista)