# Desafio 1 - Faça um programa que leia 3 números e informe o maior deles.

num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite um valor inteiro: "))
num3 = int(input("Digite um valor inteiro: "))
num4 = int(input("Digite um valor inteiro: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(f"O número {num1} foi o maior valor encontrado.")
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(f"O número {num2} foi o maior valor encontrado.")
elif num3 > num1 and num3 > num2 and num3 > num4:
    print(f"O número {num3} foi o maior valor encontrado.")
elif num4 > num1 and num4 > num2 and num4 > num3:
    print(f"O número {num4} foi o maior valor encontrado.")
elif num1 == num2 == num3 == num4:
    print(f"Todos os valores são iguais com valor {num1}")