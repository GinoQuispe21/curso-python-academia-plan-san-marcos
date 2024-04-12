"""
# EJERCICIO 4: REGISTRO DE ESTUDIANTES

Supongamos que estás desarrollando un programa para gestionar el registro de estudiantes en una escuela. 
Cada estudiante tiene un número de identificación único y su información incluye nombre, edad y calificaciones en diferentes materias. 
Utiliza un diccionario para almacenar esta información y realiza las siguientes operaciones:

1. Crea un diccionario vacío llamado registro_estudiantes.

2. Agrega al menos tres estudiantes al registro. Cada estudiante debe tener un número de identificación 
   como clave del diccionario y un diccionario anidado como valor, que contenga su nombre, edad y calificaciones 
   en diferentes materias (por ejemplo, Matemáticas, Ciencias, Historia).

3. Implementa una función llamada agregar_estudiante que tome como argumentos el registro de estudiantes, 
   el número de identificación del estudiante, su nombre, edad y calificaciones en las materias mencionadas 
   anteriormente, y agregue esta información al registro.

4. Implementa una función llamada calcular_promedio que tome como argumentos el registro de estudiantes 
   y el número de identificación de un estudiante, y calcule el promedio de sus calificaciones.

5. Implementa una función llamada mostrar_informacion que tome como argumento el registro de estudiantes 
   y el número de identificación de un estudiante, y muestre toda su información (nombre, edad y calificaciones).
"""

registro_estudiantes = {}
registro_estudiantes[1] = dict(
    nombre = 'Jorge Mauricio',
    edad = 20,
    calificcaciones = {
        'Matemáticas': 20,
        'Ciencias': 19,
        'Historia': 20
    }
)
registro_estudiantes[2] = dict(
    nombre = 'Rodolfo Antonio',
    edad = 34,
    calificcaciones = dict(
        Matemáticas = 20,
        Ciencias = 18,
        Historia = 20
    )
)
registro_estudiantes[3] = dict(
    nombre = 'Gino Quispe',
    edad = 23,
    calificcaciones = {
        'Matemáticas': 10,
        'Ciencias': 12,
        'Historia': 19
    }
)

def agregar_estudiante(id_estudiante, nombre_estudiante, edad_estudiante, **kwargs):
    registro_estudiantes[id_estudiante] = {
        'nombre': nombre_estudiante,
        'edad': edad_estudiante,
        'calificcaciones': {
            'Matemáticas': kwargs['matematicas'],
            'Ciencias': kwargs['ciencias'],
            'Historia': kwargs['historia']
        }
    }

def calcular_promedio(id_estudiante):
    califaciones = registro_estudiantes[id_estudiante]['calificcaciones'].values()
    promedio = sum(califaciones) / len(califaciones)
    print(f"El estudainte {registro_estudiantes[id_estudiante]['nombre']} tiene el promedio: {promedio:.2f}")

def mostrar_informacion(id_estudiante):
    estudainte = registro_estudiantes[id_estudiante]
    print(f"Nombre: {estudainte['nombre']}")
    print(f"Edad: {estudainte['edad']}")
    print("Califaciones:")
    for curso, califacion in estudainte['calificcaciones'].items():
        print(f"{curso}: {califacion}")

agregar_estudiante(21, 'Jeriot', 21, matematicas = 20, ciencias = 18, historia = 19)
print(registro_estudiantes)
calcular_promedio(3)
mostrar_informacion(2)
