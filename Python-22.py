"""
4
Enunciado
Faça um script que lê 10 números e mostra na tela aqueles que são maiores que a média.
"""

lista = []
lista2 = []
for c in range(0, 10):
    numero = int(input(f"Digite o {c + 1}º valor: "))
    lista.append(numero)

soma = 0
for num in lista:
    soma = soma + num
media = soma/len(lista)

for num in lista:
    if num > media:
        lista2.append(num)
print(media)
print(f"Os número maiores que a média são {lista2}")


