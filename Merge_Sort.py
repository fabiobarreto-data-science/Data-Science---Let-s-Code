def mergeSort(lista, inicio, fim):
    # Continuidade
    if not (fim - inicio <= 1):
        meio = (inicio + fim) // 2

        # Chamando lado esquerdo
        mergeSort(lista, inicio, meio)

        # Chamando lado direito
        mergeSort(lista, meio, fim)

        merge(lista, inicio, meio, fim)

        return lista


def merge(lista, inicio, meio, fim):
    lista_esquerda = lista[inicio: meio]
    lista_direita = lista[meio: fim]
    i = 0
    j = 0
    for list_index in range(inicio, fim):
        if i >= len(lista_esquerda):
            lista[list_index] = lista_direita[j]
            j = j + 1
        elif j >= len(lista_direita):
            lista[list_index] = lista_esquerda[i]
            i = i + 1
        elif lista_esquerda[i] <= lista_direita[j]:
            lista[list_index] = lista_esquerda[i]
            i = i + 1
        elif lista_direita[j] < lista_esquerda[i]:
            lista[list_index] = lista_direita[j]
            j = j + 1


print(mergeSort([3, 6, 1, 5, 4, 2], inicio=0, fim=len([3, 6, 1, 5, 4, 2])))
