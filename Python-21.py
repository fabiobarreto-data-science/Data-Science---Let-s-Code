"""
Enunciado
Faça um script que leia números do usuário, enquanto ele não digitar 0. Armazene esses números em uma lista e ao final informe quantos números foram digitados, ignorando o 0.
"""

lista = []
numero = 1
cont = 0
while numero != 0:
    numero = int(input("Digite um valor: "))
    if numero == 0:
        break
    cont = cont + 1
    lista.append(numero)

print(f"Foram digitados {len(lista)} números")