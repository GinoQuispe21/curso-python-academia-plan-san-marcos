def my_function():
    print("Hola mundo, que tal les va")

a = 20
b = False
print("Suma", a+b)
# 
#
my_function()

# Los parametros de la funcion suma son a y b
def suma(a = int, b = int):
    print("La suma de los nuemeros es: ", a + b)

# El paso de valores se le conoce como asignarcion de argumentos de la funcion
suma(10, 2)
suma(1, 3)
suma(5, 20)
suma("gino", "quispe")
# suma("gino", 20)

a = 100
suma(3, 4)
print(a)

print("-"*20)

resultado = 20
print(resultado)
def division(numero1, numero2):
    resultado = numero1 / numero2
    print(resultado)

division(10, 2)
print(resultado)

# Varios parametros:

def presentacion(nombre, apellido_paterno, apellido_materno, edad, nacionalidad = "Peruana"):
    print(f"""
    Mi nombre es: {nombre}, 
    mis apellidos son: {apellido_paterno} {apellido_materno},
    tengo la edad de {edad} años,
    y mi nacionalidad es {nacionalidad}
    """)

# Paso de argumentos por parametro posicional
presentacion("Gino", "Quispe", "Calixto", 22)

# Paso de argumetnos por nombre de parametro
presentacion(edad = 22, nombre = "Jorge", apellido_paterno = "Rodriguez", apellido_materno = "Zarate")

presentacion("Rodrigo", "Mazzarri", "Leyva", 30)

