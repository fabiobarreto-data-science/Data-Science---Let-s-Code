"""
**Exercício 5**

Dadas duas listas, mostre a união entre seus elementos, removendo os repetidos.

Imprima as duas listas originais e a lista uniao.

Exemplo:

lista_a = ['c', 5.0, 3]

lista_b = ['py', 3, 5.5]

uniao = ['c', 5.0, 3, 'py', 5.5]
"""

lista_a = ['c', 5.0, 3]

lista_b = ['py', 3, 5.5]


for abc in lista_a:
    if abc in lista_b:
        lista_b.remove(abc)

lista_uniao = lista_a + lista_b
print(f"{lista_uniao}")