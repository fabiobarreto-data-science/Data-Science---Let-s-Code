"""
2
Enunciado
Faça um programa que lê uma indeterminada quantidade de números até que o 0 (zero) seja digitado. Ao final, mostre os três menores de forma decrescente.

"""
lista = []
numero = 1
while numero != 0:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    lista.append(numero)
    lista.sort(reverse=True)

print(lista)
print(lista[-3:])




