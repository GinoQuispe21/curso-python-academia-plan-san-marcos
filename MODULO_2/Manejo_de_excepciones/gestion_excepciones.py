x = 10
y = 0

"""try:
    resultado = x / y
except ZeroDivisionError as error:
    #print("Lo sentimos, no puede realziar una division entre 0")
    print("Lo sentimso, se encontre el siguiente error: \n", error)
"""


"""try:
    numero1 = int(input("Ingrese un numero 1: "))
    numero2 = int(input("Ingrese un numero 2: "))
    resultado_suma = numero1 + numero2
    resultado_division = numero1 / numero2
    print(resultado_suma)
    print(resultado_division)
except ZeroDivisionError:
    print("Lo sentimos, no puede realizar divisiones entre 0")
except ValueError:
    print("No ingreso un numero valido")
except KeyboardInterrupt:
    print("\nSe detuvo el programa")"""


# Crear nuestras propias excepciones
    
"""try:
    a = int(input("Ingrese un valor para el numero a: "))
    b = int(input("Ingrese un valor para el numero b: "))
    if b == 0:
        raise ZeroDivisionError("b no puede tomar el valor de 0", a, b)
    print(a/b)
except ZeroDivisionError as error:
    print(error)
    print(error.args[0])
    print(error.args[1])
    print(error.args[2])"""

try:
    a = int(input("Ingrese un valor para el numero a: "))
    b = int(input("Ingrese un valor para el numero b: "))
    resultado = a / b
except Exception:
    print("Ocurrio un error")
else: # En esta parte no se realiza una gestion de errores, y se ejecuta cuando se culmine la sentencia del try
    print("El resultado de la divsion es: ", resultado)
finally: # Esta sentencia es independiente y se ejecutara siempre sin importar que se lance alguna excepcion
    print("Se termino el programa")
