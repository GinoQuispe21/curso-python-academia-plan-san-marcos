suma = lambda num1, num2: num1 + num2
print(suma(10, 20))

potencia = lambda num1, num2: num1 ** num2
print(potencia(2, 10))

def crear_lista_numeros(limite_lista, func):
    aux = [element for element in range(limite_lista) if func(element)]
    return aux

lisata_impares = crear_lista_numeros(20, lambda n: True if n > 5 else False)
print(lisata_impares)