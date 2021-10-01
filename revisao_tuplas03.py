"""
Enunciado
Crie uma função que recebe uma lista e retorna True se todos os seus elementos forem numéricos (int, float ou string contendo um int ou float) ou False do contrário.
A função deve também retornar a lista tratada: transformar todas as entradas não numéricas em numéricas ou, no melhor caso, devolver a lista apenas.
"""
lista = [1, "2", 3, 4, "5.5", "6", 7]
lista2 = ["Um", "dois", "Três"]


def tratar_lista(lista):
    for c in lista:
        if type(c) == int and type(c) == float and type(c) == f"{int}" and type(c) == f"{float}":
            return True, lista
        return False
    for c in lista:
        if type(c) == f"{int}":
            lista.append(int(c))
        elif type(c) == f"{float}":
            lista.append(float(c))
        else:
            lista.append(c)
    return lista


print(tratar_lista(lista))