"""
Vale
10
Enunciado
Faça um programa que, dadas duas listas de mesmo tamanho, crie uma nova lista com cada elemento igual a soma dos elementos da lista 1 com os da lista 2, na mesma posição.

Exemplo: dadas lista1 = [1, 4, 5] e lista2 = [2, 2, 3], então lista3 = [1+2, 4+2, 5+3] = [3, 6, 8]
"""
lista1 = [1, 4, 5]
lista2 = [2, 2, 3]

lista_soma = []
# lista_soma = [lista_geral[0] + lista_geral[3], lista_geral[1] + lista_geral[4], lista_geral[2] + lista_geral[5]]

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


print(lista_soma)







