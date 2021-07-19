"""
Desafio 1 | Faça um programa que peça para o usuário digitar o nome e a idade de um aluno e o número de provas que esse aluno fez. Depois, o programa deve pedir para o usuário digitar as notas de cada prova do aluno. Ao final o programa deve imprimir uma lista contendo:

a. Nome do aluno na posição 0

b. Idade do aluno na posição 1

c. Uma lista com todas as notas na posição 2

d. A média do aluno na posição 3

e. True ou False, caso a média seja maior que 5 ou não, na posição 4
"""
nota = []
lista = []

nome = str(input("NOME: "))
lista.append(nome)
idade = int(input("IDADE: "))
lista.append(idade)
num_provas = int(input("NÚMERO DE PROVAS: "))
for c in range(1, num_provas + 1):
    nota.append(float(input(f"NOTA{c} ")))
lista.append(nota)

soma = media = 0

for num in nota:
    soma = soma + num

media = soma/len(nota)
lista.append(media)
if media > 5:
    lista.append(True)
else:
    lista.append(False)

print(lista)
