import random as rd

my_list = [0, 1, True, False, {}, []]
list_filter = list(filter(None, my_list))
print(list_filter)

# Filter
# Aplicar una condicion como funcion que debe ser verdadera para agregar el elemento al nuevo iterable

def mayoria_edad(edad):
    return edad >= 18

edades_aleatorias = [rd.randint(10, 25) for _ in range(10)]
print(edades_aleatorias)
edades_filtradas = tuple(filter(mayoria_edad, edades_aleatorias))
print(edades_filtradas)

es_part = lambda n: n % 2 != 0
numeros_aleatorios_1= [rd.randint(1, 100) for _ in range(20)]
print(numeros_aleatorios_1)
numeros_pares= list(filter(es_part, numeros_aleatorios_1))
print(numeros_pares)

students = ["Alexander", "Jhon", "Rodolfo", "Alexis"]
students_a = set(filter(lambda student: student.startswith('A'), students))
print(students_a)



