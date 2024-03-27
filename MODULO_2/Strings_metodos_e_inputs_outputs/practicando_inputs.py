print("Ingresa dos numeros para la sumatoria")
numero_1 = input("Ingrese el numero 1: ")
numero_2 = input("Ingrese el numero 2: ")
# Cuando se lee un input y se asigna a una variable, este sera una cadena de texto
a = int(numero_1) # Casteo / Transformar un tipo de dato a otro
b = int(numero_2)
print(type(a))
print(type(b))
print("La suma de los dos numeros es: ", a + b)

print(f"El resultado de la resta de {a} con el valor de {b} es igual a {a - b}")
print("El resultado de la resta de {0} con el valor de {1} es igual a {2}".format(a, b, a - b))

