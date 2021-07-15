"""Enunciado
Faça a multiplicação entre dois números usando somente soma.
"""

num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite outro valor inteiro: "))
c = multiplicacao = 0
while c < num2:
    multiplicacao = num1 + multiplicacao
    c = c + 1
print(f"{multiplicacao}")
