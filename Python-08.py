# Reverse a given integer number

numero = int(input("Digite um número inteiro de 3 dìgitos: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
print(f"O inverso do número é {unidade}{dezena}{centena}")