"""
Agora usando a função max() faça um programa que imprima os três maiores números de uma lista.

Dica: Use o método próprio de listas .remove().
"""
lista = [23, 2, 45, 106, 7, 1, 58, 12, 22, 53]

lista.sort()
print(lista[-3:])