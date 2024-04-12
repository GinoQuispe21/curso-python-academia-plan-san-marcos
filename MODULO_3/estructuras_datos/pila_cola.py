# Pila/ Stack -> estructura de dato donde el ultimo elemento en ser agregado es el primero en ser elminado/retirado
# LIFO -> last in first out

# Pila representada por una lista
pila = ['A', 'B', 'C', 'D']
# Push para la pila / append para la lista
pila.append('E')
print("Pila: ", pila)
# Metodo pop para retirar ultimo elemento agregado a la pila
pila.pop()
print("Pila: ", pila)

# Las pilas no son indexadas, en este caso representamos una pila como lista lo cual va a permitir su indexacion
# sin embargo, la estructura correcta no debe permitir ello
# print(pila[1])

# Cola/ Queue -> estructura de dato donde el primer elemento en ser agregado es el primer elemento en ser eliminado
# FIFO -> first in first out

# Cola representada por una lista
cola = ['A', 'B', 'C', 'D']

# Cola: enqueue / lista: append
cola.append('E')
print("Cola: ", cola)

# Cola: dequeue/ lista: pop(0)
cola.pop(0)
print("Cola: ", cola)