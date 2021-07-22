"""
10
Enunciado
Faça um programa que sorteie 10 números entre 0 e 100 e imprima:

a. o maior número sorteado;

b. o menor número sorteado;

c. a média dos números sorteados;

d. a soma dos números sorteados.

"""

import random

lista = []

for c in range(0, 10):
    numeros = random.randint(0, 100)
    lista.append(numeros)
print(lista)
print(max(lista))
print(min(lista))

soma = 0
for c in lista:
    soma = soma + c

media = soma/len(lista)
print(media)
print(soma)