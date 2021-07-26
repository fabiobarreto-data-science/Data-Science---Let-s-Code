"""
Enunciado
Faça uma função que recebe um nome e um horário e imprime “Bom dia, [nome]”,
caso seja antes de 12h, “Boa Tarde, [nome]”, caso seja entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.
"""


def nomeHora(nome, hora):
    if hora < 12:
        print(f"Bom dia, {nome}")
    elif hora <18:
        print(f"Boa tarde, {nome}")
    else:
        print(f"Boa noite, {nome}")


nomeHora("Fábio", 19)