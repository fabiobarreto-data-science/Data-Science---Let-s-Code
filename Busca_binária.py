def busca_binaria(lista, elemento):
    if len(lista) <= 1:
        if lista[0] == elemento:
            return True
        else:
            return False

    meio = len(lista) // 2
    
    if lista[meio] == elemento:
        return True
    else:
        if lista[meio] > elemento:
            return busca_binaria(lista[:meio], elemento)
        else:
            return busca_binaria(lista[meio + 1:], elemento)


print(busca_binaria([1, 2, 3, 4], 4))