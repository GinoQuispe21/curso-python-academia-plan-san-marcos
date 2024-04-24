def binary_search(elemento, lista):
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        media = (izq + der)//2
        if lista[media] == elemento:
            return media
        elif lista[media] > elemento:
            der = media - 1
        else:
            izq = media + 1
    return -1

lista = [i for i in range(1, 100000) if i % 2 == 0]
indice_encontrado = binary_search(6780, lista)
print(indice_encontrado)