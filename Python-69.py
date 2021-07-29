"""
Enunciado
Desafio 2 - Faça uma função que recebe duas entradas: um input dado pelo usuário e um string que informa o tipo de dado ("idade", "salário" ou "sexo"),
e verifica se os dados digitados foram válidos, usando os seguintes critérios:

a. Idade: entre 0 e 150;

b. Salário: maior que 0;

c. Sexo: M, F ou Outro.
"""


def validar(idade, salario, sexo):
    if 0 < idade < 150 and salario > 0 and sexo == "M" or sexo == "F" or sexo == "OUTRO":
        print(f"Com idade de {idade} anos, salário de R$ {salario} e sexo {sexo} seu cadastero está válido!")


idade = int(input("Qual a sua idade? "))
salario = float(input("Qual o seu salário? R$ "))
sexo = str(input("Qual o seu sexo? [M/F/OUTRO]: ")).upper().strip()

validar(idade, salario, sexo)
