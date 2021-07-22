"""
Enunciado
Faça um programa que olhe todos os itens de uma lista e diga quantos deles são pares.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista_pares = []
pares = 0
for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
        pares = pares + 1
print(f"{pares} são pares, são eles {lista_pares}")