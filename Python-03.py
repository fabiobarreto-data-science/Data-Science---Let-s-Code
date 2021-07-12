# Desafio 1 - Faça um programa que leia 3 números e informe o maior deles.

num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite um valor inteiro: "))
num3 = int(input("Digite um valor inteiro: "))

if num1 > num2 and num1 > num3:
    print(f"O número {num1} foi o maior valor encontrado.")
else:
    if num2 > num1 and num2 > num3:
        print(f"O número {num2} foi o maior valor encontrado.")
    else:
        if num3 > num1 and num3 > num2:
            print(f"O número {num3} foi o maior valor encontrado.")

