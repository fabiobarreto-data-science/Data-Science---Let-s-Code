"""
Enunciado
Faça um script que leia 10 números do usuário e devolva duas listas: uma com os números ímpares e outra com os números pares.
"""
lista_geral = []
lista_par = []
lista_impar = []

for c in range(0, 10):
    numero = int(input(f"Digite o {c}º valor: "))
    lista_geral.append(numero)

for num in lista_geral:
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(f"Lista dos números pares = {lista_par}")
print(f"Lista dos números impares = {lista_impar}")
