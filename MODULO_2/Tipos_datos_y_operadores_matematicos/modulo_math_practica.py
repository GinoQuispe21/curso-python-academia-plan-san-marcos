import math

numero_1 = 25
# Raiz cuadrada: 
print("Raiz cuadrada: ", math.sqrt(numero_1))

# Potencia:
print("Potenciacion: ", math.pow(numero_1, 2))

# Exponencial
print("Exponencial: ", math.exp(10))
print("Exponencial en base 2:", math.exp2(8))

# Logaritmos
print("Logaritmo:", math.log(16, 2))
print("Logaritmo 2:", math.log(81, 3))
print("Logaritmo 3:", math.log(100))

# Seno, Coseno, Tangente
angulo_grados = 0
# Transformacion a radianes
angulo_radianes = math.radians(angulo_grados)
print("El seno del angulo 0 es: ", math.sin(angulo_radianes))
print("El coseno del angulo 0 es: ", math.cos(angulo_radianes))
print("La tangente del angulo 0 es: ", math.tan(angulo_radianes))

# Redondeos:

print("Redondeo hacia arriba: ", math.ceil(10.10))
print("Redondeo hacia abjao: ", math.floor(20.99))
print("Eliminar la parte decimal del numero flotantes: ", math.trunc(11.70))

# Factorial: 4! = 1 * 2 * 3 * 4

print(math.factorial(4))

# Constantes
print("El valor de pi es: ", math.pi)
print("El valor de e es: ", math.e)
print("El valor de un numero infinito: ", math.inf)
