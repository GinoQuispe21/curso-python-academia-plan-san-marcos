lista_numeros = [10, 32, 48, 1, 21, 100]
lista = [i for i in range(1, 100000) if i % 2 == 0]

def busqueda_lineal(elemento, lista):
    for index, element in enumerate(lista):
        if element == elemento:
            return index
        
indice_encontrado = busqueda_lineal(678, lista)
print(indice_encontrado)