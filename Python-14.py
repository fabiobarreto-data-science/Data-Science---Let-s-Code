

"""
**Exercício 4**

Dadas duas listas de números inteiros, mostre todos os possíveis pares entre eles.
"""

lista_1 = [1, 2]

lista_2 = [1, 3, 5]

pares = (1, 1), (2, 1), (1, 3), (2, 3), (1, 5), (2, 5)

for c in lista_1:
    for d in lista_2:
        print(f"({c}, {d})")