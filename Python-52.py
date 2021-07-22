"""
10
Enunciado
Desafio 3 - Faça um programa que pede para o usuário digitar o CPF e verifica se ele é válido. Para isso, primeiramente o programa deve multiplicar cada um dos 9 primeiros dígitos do CPF
pelos números de 10 a 2 e somar todas as respostas. O resultado deve ser multiplicado por 10 e dividido por 11. O resto dessa divisão deve ser igual ao primeiro dígito verificador
(10º dígito). Em seguida, o programa deve multiplicar cada um dos 10 primeiros dígitos do CPF pelos números de 11 a 2 e repetir o procedimento anterior para verificar o segundo
dígito verificador.

Exemplo:

Se o CPF for 286.255.878-87 o programa deve fazer primeiro:

x = (2*10 + 8*9 + 6*8 + 2*7 + 5*6 + 5*5 + 8*4 + 7*3 + 8*2)

Em seguida, o programa deve testar se x*10%11 == 8 (o décimo número do CPF). Se sim, o programa deve calcular:

x = (2*11 + 8*10 + 6*9 + 2*8 + 5*7 + 5*6 + 8*5 + 7*4 + 8*3 + 8*2)

e verificar se x*10%11 == 7 (o décimo primeiro número do CPF).
"""

cpf = str(input("Digite seu CPF: "))
lista = []
c = k = 0
for c in range(0, 9):  # 791716135-87    (7x10, 9x9, 1x8, 7x7, 1x6, 6x5, 1x4, 3x3, 5x2)
    num = int(cpf[c]) * (k + 10) # 8
    k = k - 1
    lista.append(num)

print(lista)
x = sum(lista)
teste = x * 10 % 11
print(teste)

lista2 = []
c = k = 0
for c in range(0, 10):  # 791716135-87    (7x11, 9x10, 1x9, 7x8, 1x7, 6x6, 1x5, 3x4, 5x3, 8x2)
    num = int(cpf[c]) * (k + 11) # 7
    k = k - 1
    lista2.append(num)

print(lista2)
x2 = sum(lista2)
teste2 = x2 * 10 % 11   # 11º
print(teste2)





