diccionario_1 = dict(
    id = 1,
    nombre = 'Rodrigo',
    edad = 24,
    correo = 'rodrigogn@gmail.com',
    nacionalidad = 'peruana'
)

print(diccionario_1, type(diccionario_1))

# Los diccionarios no pueden ser buscados por indices numericos -> exception keyerror
# Si pueden ser buscado su valor por su llave de un elemento del diccionario
print(diccionario_1['correo'])

# Retorna el numero de elementos de mi diccionario
print(len(diccionario_1))

print('dni' in diccionario_1)
print('dni' not in diccionario_1)

# Al ser un diccionario mutable podemos agregar elementos
diccionario_1['dni'] = 76812426
print(diccionario_1)

diccionario_1.update({'genero': 'masculino'})
print(diccionario_1)

# Modificar un elemento ya creado de mi lista
diccionario_1['id'] = 21
print(diccionario_1)

diccionario_1.update({'nombre': 'Jeriot'})
print(diccionario_1)

# Vamos a retornar una llave por su valor
value_searched = 'rodrigogn@gmail.com'
print(diccionario_1.items())
for key, value in diccionario_1.items():
    if value == value_searched:
        print(key)

# Obtener solo las llaves/ keys de un diccionario
keys = diccionario_1.keys()
print(keys)

# Obtener solo los valores de un diccionario
values = diccionario_1.values()
print(values, type(values))
# print(values[0]) -> keyerror
for value in values:
    print(value)

# Ordenar diccionario
print(sorted(diccionario_1.keys()))
# print(sorted(diccionario_1.values()))

# Eliminar elemento de mi diccionario
del diccionario_1['genero']
print(diccionario_1)

"Diccionarios son mutables, por lo cual su paso es por referencia, al igual que una lista"
diccionario_2 = {
    1: '1',
    2: '2',
    3: '3'
}
# diccionario_3 = diccionario_2
# print(f"Diccionario 2: {diccionario_2} | id: {id(diccionario_2)}")
# print(f"Diccionario 3: {diccionario_3} | id: {id(diccionario_3)}")
# diccionario_3[1] = '100'
# print(f"Diccionario 2: {diccionario_2} | id: {id(diccionario_2)}")
# print(f"Diccionario 3: {diccionario_3} | id: {id(diccionario_3)}")

# metodo copy
diccionario_4 = diccionario_2.copy()
print(f"Diccionario 2: {diccionario_2} | id: {id(diccionario_2)}")
print(f"Diccionario 4: {diccionario_4} | id: {id(diccionario_4)}")
diccionario_4[1] = '100'
print(f"Diccionario 2: {diccionario_2} | id: {id(diccionario_2)}")
print(f"Diccionario 4: {diccionario_4} | id: {id(diccionario_4)}")