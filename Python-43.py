"""
10
Enunciado
Faça um programa que imprima o maior número de uma lista, sem usar a função max().
"""

lista = [23, 2, 45, 106, 7, 1, 58, 12, 22, 53]
maior = 0
for c in lista:
    if c > maior:
        maior = c

print(f"O maior número é {maior}")