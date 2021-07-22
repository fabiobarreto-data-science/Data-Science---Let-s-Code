"""
Sorteie uma lista de 10 números e imprima:

a. uma lista com os 4 primeiros números;

b. uma lista com os 5 últimos números;

c. uma lista contendo apenas os elementos das posições pares;

d. uma lista contendo apenas os elementos das posições ímpares;

e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);

f. uma lista inversa dos 5 primeiros números;

g. uma lista inversa dos 5 últimos números.
"""
import random

lista = []
lista_pares = []
lista_impar = []
lista_inversa = []

for num in range(0, 10):
    numeros = random.randint(1, 100)
    lista.append(numeros)

print(lista)
print(f"Os 4 primeiros números são {lista[:4]}")
print(f"Os 5 últimos números são {lista[-5:]}")
for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
print(f"Os números pares da lista são {lista_pares}")

for c in lista:
    if c % 2 == 1:
        lista_impar.append(c)
print(f"Os números ímpares da lista são {lista_impar}")
lista.reverse()
print(f"O inverso da lista é {lista}")
print(f"Os 5 primeiros numeros da lista inversa é {lista[:5]}")
print(f"A lista inversa dos 5 últimos números é {lista[-5:]}")