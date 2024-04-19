import random as rd

lista_des = [rd.randint(1, 10000) for _ in range(10000)]

def buble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i -1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j+1] =  aux
    print(lista)

buble_sort(lista_des)