"""
Enunciado
Informe, de forma decrescente todos os pares entre N (número fornecido pelo usuário) e -N.
"""

N = int(input("Digite um valor inteiro: "))

for numero in range(0, N, 2):
    print(f"{numero}, ", end="")

print()
print(f"{-1*N}")
