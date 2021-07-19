"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média aritmética delas, usando listas.
"""
nota = []
for c in range(1, 5):
    nota.append(float(input(f"Digite a {c}ª nota: ")))

soma = 0
for i in nota:
    soma = soma + i
    media = soma / len(nota)

print(f"A média aritmédia entre as notas é de {media}")
