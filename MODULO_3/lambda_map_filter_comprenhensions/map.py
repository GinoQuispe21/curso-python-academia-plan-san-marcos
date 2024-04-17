lista_1 = ["1", "2", "3", "4"]
obj_map = list(map(float, lista_1))
print(obj_map, type(obj_map), type(obj_map[0]))

lista_2 = [[1000, 21, 100, 1], [2, 3], [-20, -21], [2121, 4, 3]]
lista_2_map = tuple(map(min, lista_2))
print(lista_2_map)

# funciones lambda en accion

lista_3 = range(0, 10, 3)
lista_3_mapeado = list(map(lambda n: n + 200, lista_3 ))
print(lista_3_mapeado)

lista_4 = ["Jeriot", "Italo", "Victor", "Mariana"]
lista_4_mapead = list(map(lambda element: element.upper(), lista_4))
print(lista_4_mapead)