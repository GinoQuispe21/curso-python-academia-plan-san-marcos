"""
# Ejercicio 1:
Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestre el mayor y menor numero ingresado. 
Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente.
"""

condicional = True
lista_numeros = []
while condicional:
    try:
        texto_entrada = input("Ingrese el numero a agregar: ")
        if texto_entrada.upper() == 'FIN':
            condicional = False
        else:
            numero = int(texto_entrada)
            lista_numeros.append(numero)
    except ValueError:
        print("Debe ingresado un dato numerico")

print(f"""
Menor numero encontrado: {min(lista_numeros)}
Mayor numero encontrado: {max(lista_numeros)}
""")