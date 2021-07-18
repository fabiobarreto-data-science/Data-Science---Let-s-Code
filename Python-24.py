"""
Enunciado
Crie duas listas sobre um time de futebol com 11 jogadores: uma lista com a idade dos jogadores e outra com as alturas. Mostre na tela a idade do jogador mais alto.
"""


idade = [19, 20, 21, 30, 31, 26, 35, 18, 22, 29, 32]
altura = [1.67, 1.73, 1.76, 1.65, 1.75, 1.69, 1.79, 1.72, 1.68, 1.66, 1.71]

alto = 0
for jogador in altura:
    if jogador > alto:
        alto = jogador
        i = altura.index(alto)

print(f"A idade do jogador mais alto com {alto}m de altura é de {idade[i]} anos")