# Diccionarios -> Estructura de datos modificable
# Permite un recuperacion de informacion mas eficiente ya que no que se busca por un indice numerico sino por una llave/key
# Los diccionarios guardan elementos de tipo key:value / llave:valor
# Secuencia ordenada y mutable

"Creacion de diccionarios"
dictionary = {
    'app': 'Telegram',
    'descargas': 100_000_000,
    'creador': 'Persona millonaria',
    'release': 2010
}

dicttionary_func_lists = dict([
    ('Nombre', 'Juan Carlos'),
    ('dni', 8888888),
    ('country', 'Peru')
])

keys = ['Nombre Mascota', 'Edad', 'Genero']
values = ['Moka', '1', 'F']
dictionary_from_lists = dict(zip(keys, values))

keys_students = ['Guillermo', 'Marco', 'Alexander', 'Jeriot']
notas = 0
dictionary_default_value = dict.fromkeys(keys_students, notas)

empty_dict = {}
empty_dict['Marca de laptop'] = 'apple'


# Metodo update
empty_dict.update({
    ('Direccion', 'Mi direccion de mi casa es:')
})

dict_parameters = dict(
    pais = 'Peru',
    edad = 22,
)

print(f"""
1. {dictionary} | {type(dictionary)}
2. {dicttionary_func_lists} | {type(dicttionary_func_lists)}
3. {dictionary_from_lists} | {type(dictionary_from_lists)}
4. {dictionary_default_value} | {type(dictionary_default_value)}
5. {empty_dict} | {type(empty_dict)}
5. {dict_parameters} | {type(dict_parameters)}
""")

dictionary.update({
    ('app', 'Facebook')
})
print(f"1. {dictionary} | {type(dictionary)}")

# Retornar valores:

print(dictionary['descargas'])
print(len(dictionary))

# Items
print(dictionary.items())

# Mostrar datos
for key, values in dictionary.items():
    print(f" Key: {key}, Values: {values}")

value_search = 'Facebook'
for keys, value in dictionary.items():
    if value_search == value:
        print(f"Se encontro la key buscada: {keys}")