# Tuplas -> estructura de dato ordenada inmutable
# Similar a una lista, pero mas eficiente ya que no es modificable y no tiene los mismos metodos con los que si se crea una lista

"Formas de crear listas"

tupla_comun = (1. ,2, "3", "False")
tupla_func_list = tuple([1., 2, "3", True])
tuple_func_range = tuple(range(0, 10, 2))
tuple_without_parentesis = "Gino", "Quispe", "Calixto"
tuple_empty = ()
tuple_one_element = (1,)
values = 20, 40, 100, 300
tuple_values = tuple(values)

print(f"""
1. {tupla_comun} | {type(tupla_comun)}
2. {tupla_func_list} | {type(tupla_func_list)}
3. {tuple_func_range} | {type(tuple_func_range)}
4. {tuple_without_parentesis} | {type(tuple_without_parentesis)}
5. {tuple_empty} | {type(tuple_empty)}
6. {tuple_one_element} | {type(tuple_one_element)}
7. {tuple_values} | {type(tuple_values)}
""")

print("Slicings")
print(tupla_comun[1:3])
print(tupla_comun[:-2])
print(tupla_comun[:])

print("Concatenacio")
tuple_1 = tuple(range(0, 10))
tuple_2 = ("Gino", "Guillermo", "Alexander")
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
tuple_4 = tuple_2 * 2
print(tuple_4)

# Ver numeros de elementos de una tupla
print(len(tuple_1))
print(len(tuple_one_element))

# Mostrar elementos de una tupla
for element in tuple_1:
    print(element)