"""
Desenvolva um script que calcule a soma dos N primeiros números naturais. Utilize a recursividade para obter o resultado.
"""


def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n - 1)


print(soma(3))