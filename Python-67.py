"""
Enunciado
Desafio 1 - Faça uma função que receba um número e calcule seu fatorial.
"""
from math import factorial


def facto(num):
    fatorial = factorial(num)
    print(f"O fatorial de {num} é {fatorial}")


facto(6)