"""
Enunciado
Faça um programa para perguntar 10 números e informar a soma total destes números.

"""
c = soma = 0
while c < 10:
    num = float(input("Digite um valor qualquer: "))
    c = c + 1
    soma = soma + num

print(f"A soma total dos valores digitados é {soma}")