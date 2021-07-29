"""
Enunciado
Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e retorna o maior entre eles.
"""

import random


lista_maior = []


def numerosAleatorios():
    for cont in range(0, 11):
        numero = random.randint(0, 100)
        lista_maior.append(numero)
        lista_maior.sort()
    print(lista_maior)
    print(f"O maior número da lista é {max(lista_maior)}")


numerosAleatorios()


