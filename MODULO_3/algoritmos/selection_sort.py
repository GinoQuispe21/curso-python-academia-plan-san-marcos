import random as rd

lista_des = [rd.randint(1, 10000) for _ in range(10000)]
# lista_des = [rd.randint(1, 100) for _ in range(15)]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        index_min_value = i
        for j in range(i + 1, n):
            if lista[j] < lista[index_min_value]:
                index_min_value = j
        # La variable aux nos ayuda a tener un backup/respaldo al momento del intercambio de posiciones en el ordenamiento
        aux = lista[i]
        lista[i] = lista[index_min_value]
        lista[index_min_value] = aux
    return lista

print(f"Lista desordenada: {lista_des}")
lista_ordenada = selection_sort(lista_des)
print(f"Lista ordenada: {lista_ordenada}")