"""
Enunciado
Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
for c in lista:
    if c % 2 == 0:
        soma = soma + 1

print(f"{soma} números da lista são pares")