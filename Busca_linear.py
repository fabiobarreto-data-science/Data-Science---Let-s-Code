def busca_linear(lista, elemento):
    found = False
    for i in range(len(lista)):
        if elemento == lista[i]:
            found = True
            break
    if not found:
        i = None
    return i


print(busca_linear([5, 2, 8], 8))
