a = 10
b = 5

# Suma: +
print("Suma:", a + b)

# Resta: -
print("Resta:",a - b)

# Multiplicacion: *
print("Multiplicacion:", a * b)

# Division: /
print("Division:", a / b)
print("Division:", 11 / 2)
# Diviones que retornan un valor exacto: //
print("Division exacta: ", a // b)
print("Division exacta: ", 10 // 3)

# Resto/ Modulo: %
print("El resto:", 33 % 5)

# Potencia: ** (doble asterisco)
print("Potencia: ", 3 ** 4)
print("Potencia: ", 11 ** 2)


ecuacion = (40 - 5 * 4) * 2 - 4 ** 2
#        = (40 - 20) * 2 - 4 ** 2
#        = (20) * 2 - 4 ** 2
#        = 20 * 2 - 16
#        = 40 - 16
print(ecuacion)

# Para la potenciacion no iremos de deracha a izquierda como dicen las reglas de orden de calculo de python
# Se debe operar de derecha a izquierda
potencias = 2 ** 2 ** 3
print(potencias)