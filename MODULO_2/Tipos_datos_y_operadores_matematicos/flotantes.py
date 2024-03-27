# Los numeros con parte decimal son conocidos como flotantes, estos contienen el punto decimal o tambien llamado punto flotante

# Para separar en mis numeros la porcion entera de la decimal se usa "." y no la ",".
ahorros = 1000.50
print("Mis ahorros son:", ahorros)
print(type(ahorros))
# La variable ahorros almacena una referencia del objeto de la clase float

# En caso se tengo un valor termine o empieze en 0 como unica porcion entera o decimal, se puede omitir colocarlo
# Esto no significa que sea muy comun esta practica
medicion_pared = 3.
interes = .25
print(medicion_pared)
print(interes)

# Para numeros que almacenan gran cantidades de decimal, en ocaciones Python para poder mostrar en la consola hara uso de la notacion cientifica, de E o e
numero_decimal_grande = 0.000000000000000000001
print(numero_decimal_grande)