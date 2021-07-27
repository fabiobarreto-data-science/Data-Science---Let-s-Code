"""
Enunciado
Faça uma função que recebe um número e retorna True se ele é par ou False, se ele é ímpar.
"""


def parImpar(num):
    if num % 2 == 0:
        print("TRUE")
    else:
        print("FALSE")


numero = int(input("Digite um número inteiro: "))
parImpar(numero)
