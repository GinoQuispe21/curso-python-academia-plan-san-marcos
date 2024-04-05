mi_lista = [1, 2, "Alexander", True, "Edwin"]
print(f"Lista inicial: {mi_lista}")

# append() -> agregar un nuevo elemento al final de la lista
mi_lista.append("Rafael")
print(f"append: {mi_lista}")

# extend() -> agrega un nueva lista a la lista original, lo hace agregandolo al final de la lista
nueva_lista = [15, 14, 20, 18]
mi_lista.extend(nueva_lista)
print(f"extend: {mi_lista}")

# insert() -> inserta un elemento nuevo en una posicion especifica
mi_lista.insert(3, "Gino")
print(f"insert: {mi_lista}")

# remove() -> eliminar un elemento de la lista, pasando como argumetno el elemento
mi_lista.remove("Gino")
print(f"remove: {mi_lista}")

# pop () -> elimina el ultimo elemento de la lista
mi_lista.pop()
print(f"pop: {mi_lista}")

# reverse() -> revertir los indices de la lista
mi_lista.reverse()
print(f"reverse: {mi_lista}")

# sort() -> ordena de menor a mayor los elementos de la lista
lista_enteros = [10, 2, 2000, 1, 3.0]
lista_enteros.sort()
print(f"sort de menor a mayor: {lista_enteros}")
# de mayor a menor
lista_enteros.sort(reverse = True)
print(f"sort de mayor a menor: {lista_enteros}")

# clear() -> eliminar todos los elementos de la lista, y dejar una lista vacia
lista_enteros.clear()
print(f"clear: {lista_enteros}")

# index() -> me va retornar el inidice de un elemento pasado como parametro del metodo
# si hay mas de un elemento igual, retornara el primer indice del elemento encontrado de izquierda a derecha
mi_lista.append('Alexander')
mi_lista.append('Alexander')
print(mi_lista)
print(f"Esta en el indice {mi_lista.index('Alexander')}")

# count() -> retorna la cantidad de veces que se encontro un elemento en la lista
print(f"Numero de veces que aparece: {mi_lista.count('Alexander')}")

# copy() -> Retorna una copia de la lista, pero pasada por valor, no por referencia

nueva_lista = mi_lista.copy()
print(f"Mi lista: {mi_lista}, id: {id(mi_lista)}")
print(f"Nueva lista: {nueva_lista}, id: {id(nueva_lista)}")

print(id(mi_lista) is id(nueva_lista))

# Operador
print("ALEXANDER" in nueva_lista)