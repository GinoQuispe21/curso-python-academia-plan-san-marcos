my_lista = ["Edwin", "Marcela", 18.0, 21, True, False]
print(my_lista, type(my_lista), id(my_lista))
# Las listas hacen referencia a la clase "list"

# Indexacion
print(my_lista[0])
print(my_lista[3])
print(my_lista[-1])

# Mutabilidad -> Pueden ser modificados

my_lista[2] = "Rafael"
print(my_lista, id(my_lista))
my_lista[-1] = my_lista[0]
print(my_lista, id(my_lista))

# Inmutable -> Tipos de datos

a = 10
print(a, id(a))
a = a + 1
print(a, id(a))

# Determinar tamaño de una lista

print(f"El tamaño de mi lista es {len(my_lista)}")

# Asignacion de listas -> asignacion por referencia (asigna tanto el valor y la referencia de la direccion en memoria)

print("="*50)

lista_1 = [1, 2.0, "3"]
lista_2 = lista_1
print(lista_1, id(lista_1))
print(lista_2, id(lista_2))

lista_1[0] = "Hola mundo"

print("="*50)
print(lista_1, id(lista_1))
print(lista_2, id(lista_2))

# Slicing
nombre = "Gino Quispe"
print(nombre[5:])
lista_3 = lista_1[:]
lista_1[1] = "que tal"
print("="*50)
print(lista_1, id(lista_1))
print(lista_3, id(lista_3))

# Lista dentro de otra lista

lista_x_lista = [1, 2.0, "3", ["Rafael", "Edwin", "Guillermno"]]
print(lista_x_lista)
print(lista_x_lista[3])
print(lista_x_lista[3][1])

# Nueva lista usando slicings
lista_1 = [1, 2, 3, 4, 5]
# lista_3 = [lista_1[-1], lista_1[-2]]
lista_3 = lista_1[3:]
print(lista_3)
