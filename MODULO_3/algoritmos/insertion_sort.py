import random as rd
lista_des = [rd.randint(1, 10000) for _ in range(10000)]

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        aux = lista[i]
        j = i - 1
        while j >= 0 and aux < lista[j]:
            lista[j+1] = lista[j]
            j = j - 1
        lista[j + 1] = aux
    return lista

lista_ordenada = insertion_sort(lista_des)
print(lista_ordenada)