"""
Enunciado
Faça uma função que recebe um número n de entrada, sorteia n números aleatórios entre 0 e 100 e retorna a média deles.
"""
import random

lista = []


def numerosAleatorios(n):
    for cont in range(0, n):
        numero = random.randint(0, 100)
        if numero not in lista:
            lista.append(numero)
    lista.sort()
    soma =  0
    for c in lista:
        soma = soma + c
    media = soma / len(lista)
    print(lista)
    print(f"A média dos números sorteados é {media}")


numerosAleatorios(3)




