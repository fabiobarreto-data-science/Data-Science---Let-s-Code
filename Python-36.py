"""
Enunciado
Faça um programa que sorteia 10 números entre 0 e 100 e conte quantos números sorteados são maiores que 50.
"""

import random

lista = []
cont = 0

for c in range(0, 10):
    numero = random.randint(0, 101)
    lista.append(numero)
    if numero > 50:
        cont = cont + 1

print(lista)
print(f"Existem {cont} números maiores que 50")