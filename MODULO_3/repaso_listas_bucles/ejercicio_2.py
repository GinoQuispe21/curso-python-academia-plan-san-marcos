"""
# Ejercicio 2:
Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestre la suma del total de numeros, la cantidad de números ingresados y el promedio de estos numeros. 
Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente.
"""

condicional = True
lista_numeros = []
contador_numeros = 0
suma = 0
while condicional:
    try:
        texto_entrada = input("Ingrese el numero a agregar: ")
        if texto_entrada.upper() == 'FIN':
            condicional = False
        else:
            numero = float(texto_entrada)
            contador_numeros = contador_numeros + 1
            suma = suma + numero
            lista_numeros.append(numero)
    except ValueError:
        print("Debe ingresado un dato numerico")

print(f"""
1. La suma de los numeros: {suma}
2. El total de numeros ingresados: {contador_numeros}
3. El promedio de los numeros es: {suma / contador_numeros}
""")
