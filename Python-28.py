"""
Enunciado
Faça um programa que imprima o maior número de uma lista, sem usar o método max().
"""

lista = [2, 25, 730, 89, 105, 1, 56, 44]

maior = 0
for c in lista:
    if c > maior:
        maior = c

print(f"O maior número da lista é {maior}")
