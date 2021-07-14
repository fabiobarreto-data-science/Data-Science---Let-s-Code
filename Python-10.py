"""
Enunciado
Faça um programa que escreva todos os números múltiplos de 7 entre 1 e N, sendo N um valor introduzido pelo usuário. Por exemplos: 7, 14, 21, 28, 35.
"""
N = int(input("Digite um valor múltiplo de 7: "))
c = 0
print(1, end=" ")
while c <= N:
    c = c + 7
    print(f"{c}", end=" ")
