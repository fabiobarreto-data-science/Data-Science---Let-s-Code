"""
Enunciado
Faça um programa, usando loops, que peça para um usuário digitar um número e que só finaliza quando o usuário digitar 0. Ao final imprima a soma de todos os números digitados
"""
numero = int(input("Digite um número inteiro: "))
soma = 0
while numero != 0:
    soma = soma + numero
    numero = int(input("Digite um número inteiro: "))
    if numero == 0:
        break

print(f"A soma de todos os números é {soma}")