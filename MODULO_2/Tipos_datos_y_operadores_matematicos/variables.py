# variable = literal/constante
edad = 22
nombre = "Gino"

# La funcion print nos ayuda a mostrar la inforamcion como salida de nuestro programa en la consola
print("Mi edad es:", edad)
print("Mi nombre es:", nombre)

# Al asignar un nuevo valor literal a nuestras variables creadas previamente, lo que hace Python es descartar el valor anterior, y considerar ahora el nuevo valor
edad = 23
nombre = "Salvador"
print("Mi edad despues de modificarla:", edad)
print("Mi nombre despues de cambiarmelo:", nombre)

# Para agregar un comentario en Python se hace uso de # o 3 veces el caracter: "" de la siguiente manera:
"""
Este es un comentario
para varias lineas
- otra linea
print(nombre)
"""

a = 10
# En python la asignacion de variables no es como en las matematicas, primero se remplaza la variable "a", que esta posterior al signo igual, por su valor que en este caso es 10
a = a + 1
print("El valor de a ahora es: ", a)

# No podemos asginar nombres a nuestras variables con palabras reservadas de Python
# break = 10
# def = "hola"
# while = True

# Los tipos de datos hacen referencia a una clase a la que pertenece el valor del literal.
# La variable nombre_Edwin almacena la referencia del valor "Edwin", donde "Edwin" es un objeto de la clase str
nombre_Edwin = "Edwin"
print(type(nombre_Edwin))

numero_estudiantes = 26
print(type(numero_estudiantes))

# snake case -> Estilo de escritura/nomenclatura en Python para poner nombres a nuestras variables
dinero_ahorrado = 10000
mis_ahorros_1 = 20000