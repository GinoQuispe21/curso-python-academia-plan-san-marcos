correo = "quispecalixtogino@gmail.com"
print(type("quispecalixtogino@gmail.com"))

# Concatenacion con el simbolo: '+'
mensaje = "Tu correo es: " + correo
print(mensaje)

# Saltos de linea

print("Gino\nAlexander\nRafael\nJeriot")

print(r"C:\documentos\nombre\Gino")

letra_cancion = """\
linea 1
linea 2
linea 3

inicio del coro
linea 1
linea 2\
"""
print(letra_cancion)


"""
Las 3 comillas no solo nos ayudan a realizar comentarios con multiples lineas,
sino que tambien nos ayuda a guardar strings sin necesidad de agregar saltos de lineas en cada espacio que uno desee.
"""

menu = """\
Ingrese una opcion de calculo:
1. Suma de dos numeros
2. Resta de dos numeros
3. Calcular interes ganados\
"""
print(menu)
# Agregamos el caracter '\' al inicio y al final para que no realice un salto de linea en nuestro string exrtenso de 3 comillas

# Concatencion sin el simbolo de '+'
nombre_completo = 'Gino ' 'Quispe ' 'Calixto'
print(nombre_completo)

presentacion = "Mi nombre es: " + nombre_completo
print(presentacion)

country = "Peru"

# Indexar => acceder a una parte de una cadena de texto mediante un indice
pais = "Republica Dominicana"
#     = 0123...
# Indexacion: variable[indice] => valor en la posicion del caracter
print("El indice de pais en la posicion 2 es: ", pais[9])
print("El indice negativo de pais en -4 es: ", pais[-4])

# La funcion len nos retorna la longitud de nuestra cadena de texto
print(len(pais))

# Slicings/ Cortes:
# El indice del lado derecho posterior a los dos puntos, es el indice limite del corte el cual no sera agregado al corte
print(pais[0:9])
print(pais[:9])
print(pais[10:])
print(pais[:-3])

# Formulita
print(pais[:9] + pais[9:])
