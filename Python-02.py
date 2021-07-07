#3) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês

ganHora = float(input("Quanto ganha por hora? "))
horMes = int(input("Quantas horas trabalhada por mês? "))

salario = ganHora * horMes
print(f"Seu salário será de R$ {salario:.2f}")