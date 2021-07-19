"""
Enunciado
Faça um programa que dadas duas listas de mesmo tamanho, imprima o produto escalar entre elas.

OBS: produto escalar é a soma do resultado da multiplicação entre o número na posição i da lista1 pelo número na posição i da lista2, com i variando de 0 ao tamanho da lista.
"""
lista1 = [1, 4, 5]
lista2 = [2, 2, 3]

lista_soma = []

for c in range(0, 3):
    if c == 0:
        somaa = lista1[c] + lista2[c]
        lista_soma.append(somaa)
    else:
        if c == 1:
            somab = lista1[c] + lista2[c]
            lista_soma.append(somab)
        else:
            if c == 2:
                somac = lista1[c] + lista2[c]
                lista_soma.append(somac)

print(sum(lista_soma))