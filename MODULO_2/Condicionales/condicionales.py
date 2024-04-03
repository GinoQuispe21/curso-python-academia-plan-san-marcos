x = int(input("Ingrese un numero x: "))
y = int(input("Ingrese un numero y: "))

if x > y:
    print("x es mayor a y")
elif x < y:
    print("x es menor que y")
else:
    print("x es igual a y")

# Operadores Ternarios

numero_en_duda = int(input("Ingrese un numero: "))
resultado = "El numero es par" if numero_en_duda % 2 == 0 else "El numero es impar"
print(resultado)

if numero_en_duda % 2 == 0:
    resultado = "El numero es par"
else:
    resultado = "El numero es impar"

