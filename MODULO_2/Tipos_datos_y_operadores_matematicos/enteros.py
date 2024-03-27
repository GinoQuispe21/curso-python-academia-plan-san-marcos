# Los numeros enteros pueden ser positivos, negativos e incluye el valor 0
# Las variables de tipos de dato enteros, almacenan objetos de la clase int

numero_mascotas = 2
print(type(numero_mascotas))

gastos_del_mes = -2000
print(type(gastos_del_mes))

zero = 0
print(type(zero))

# Para mejorar la legibilidad de lectura para nosotros, podemos agregar "_" en numeros grandes para separarlos cada miles
# No se puede separar usando "," ya que este tiene otro uso en el lenguaje, como en separar elementos en el llamado dentro de funciones.
# Ejm: print(a, b)
dinero_millonario = 111_110_000_001_001_010_100
print("EL dinero que tiene el millonario es: ", dinero_millonario)
print("El tipo de dato que almacena la variable dinero_millonario es: ", type(dinero_millonario))

# En Python la multiplicacion se da usando el caracter asterisco: "*"
multiplicacion = 2 * 3
print(multiplicacion)
# Y para el caso de un numero "a" elevado a la potencia "b" se realiza usando doble asterisco:
potencia = 2 ** 3
print(potencia)