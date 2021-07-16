"""
Enunciado
Faça um programa que peça 10 números para o usuário e guarde os números em uma lista. Com a lista preenchida descubra quantos números são pares.
"""
lista = []
for c in range(0, 10):
    numero = int(input(f"Digite o {c + 1}º valor inteiro: "))
    lista.append(numero)

num_pares = 0
for num in lista:
    if num % 2 == 0:
        num_pares = num_pares + 1

print(lista)
print(f"{num_pares} números são pares")