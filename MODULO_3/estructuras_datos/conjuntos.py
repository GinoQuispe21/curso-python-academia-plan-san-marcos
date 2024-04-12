# Conjuntos / sets
# Estructura de datos no ordenada y de datos unicos
# Los sets solo pueden almacenar elementos de tipos de datos hasehables/ tipos de datos basicos
# Los sets son mayormente usados para representar conjuntos de elementos unicos

grupo_a = set([1, 2, 3, 4, 5])
grupo_b = {'Jeriot', 'Guillermo', 'Rodolfo', 'Alexander'}
print(f"Group a: {grupo_a} | Tipo: {type(grupo_a)}")
print(f"Group b: {grupo_b} | Tipo: {type(grupo_b)}")

"Metodos de conjuntos"

# Agregar un elemento al conjunto
grupo_b.add('Marce')
print(f"Add: {grupo_b}")

# Remover un elemnto de un conjunto
grupo_a.discard(3)
print(f"Discard: {grupo_a}")

# Clear: limpiar el conjunto / borrar todos los elemtnos
grupo_a.clear()
print(f"Clear: {grupo_a}")

# Coppy: Copia por valor
group_c = grupo_b.copy()
print(group_c)

# pop(): al ejecutar el metodo pop en una estructura de dato no ordenada, eliminara de manera aleatoria cualquier elemento
group_c.pop()
print(group_c)

# metodo union -> unifica dos grupos
group_d = {'Sergio', 'Italo', 'Alexander'}
group_union = group_c.union(group_d)
print(group_union)

# metodo intersection -> interseccion de elementos iguales
group_intersection = group_c.intersection(group_d)
print(group_intersection)

# metodo diferencias
print("Metodo diferencia")
grupo_1 = {1, 3, 5, 19, 21, 30}
grupo_2 = {11, 12, 13, 39}
grupo_diferencia = grupo_1.difference(grupo_2)
print(grupo_diferencia)

# metodo isdisjoint -> retorna un true o false comprabando si dos conjuntos no tienen elementos iguales
print(grupo_1.isdisjoint(grupo_2))

# metodo issubset -> retorna un true o false si un conjunto es un subconjunto de otro
grupo_20 = {1, 3, 5, 19, 21, 30}
grupo_21 = {21, 1}
print(f"El grupo 21 esta incluido en el grupo 20: {grupo_21.issubset(grupo_20)}")

# metodo superset -> retorna un true o false si un conjunto contiene a otro:
print(f"El grupo 20 incluye al grupo 21: {grupo_20.issuperset(grupo_21)}")

# metodo update -> hace una union de los dos conjuntos, pero el valor de la respuesta del metodo sera igualado al conjunto origen
grupo_21.update(grupo_20)
print(grupo_21)

# metodo symetric difference -> diferencia simetrica
grupo_100 = {'Alexander', 'Jeriot', 'Jorge', 'Marce'}
grupo_101 = {'Alexander', 'Jhon', 'Rafael', 'Rodolfo'}
print(grupo_100.symmetric_difference(grupo_101))

# intersection_update
# grupo_100.intersection_update(grupo_101)
# print(grupo_100)

# difference_update
grupo_101.difference_update(grupo_100)
print(grupo_101)

# symetric_diference_update
grupo_100.symmetric_difference_update(grupo_101)
print(grupo_100)