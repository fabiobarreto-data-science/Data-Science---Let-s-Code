"""
Faça um programa como o do item anterior, porém que imprima a média sem considerar a maior e
menor nota do aluno (nesse caso o número de provas precisa ser obrigatoriamente maior que dois).

Dica: crie uma cópia com a lista de todas as notas antes de fazer a média.
"""

nota = []
lista = []
nota_g = []

# Adiciona o nome
nome = str(input("NOME: "))
lista.append(nome)

# Adiciona a idade
idade = int(input("IDADE: "))
lista.append(idade)

# Adiciona as notas
num_provas = int(input("NÚMERO DE PROVAS: "))
for c in range(1, num_provas + 1):
    nota.append(float(input(f"NOTA{c} ")))

nota_g = nota.copy()
lista.append(nota_g)

# Adiciona a média
nota_maxima = max(nota)
nota_minima = min(nota)

nota.remove(nota_maxima)
nota.remove(nota_minima)

lista.append(nota)

soma = media = 0
for num in nota:
    soma = soma + num

media = soma/len(nota_g)
lista.append(media)
if media > 5:
    lista.append(True)
else:
    lista.append(False)

print(lista)


