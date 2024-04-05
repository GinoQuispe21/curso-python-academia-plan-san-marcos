# while -> usados mayormente para validar condicionales y que una porcion de codigo se ejecute muchas veces hasta que se rompa la condicional

# Codigo infinito -> La condicional del while nunca cambio a true
"""while True:
    print("Hola mundo")"""

numero = 1

# Codigo que temina y no es infinito porque la condicional esta siendo afectada por una varaible que cambia su valor constantemente
while numero <= 5:
    print("hola mundo")
    #numero = numero + 1
    numero += 1

conditional = True
while conditional:
    try:
        numero_1 = int(input("Ingrese el numero 1: "))
        numero_2 = int(input("Ingrese el numero 2: "))
        conditional = False
        print(numero_1 + numero_2)
    except Exception:
        print("Se encontro un error, intente nuevamente")

# for -> mayormente usado para recorrer listas u otras estructuras de datos

lista = [1, 2, 3, "Alexander", "Gino", "Alexander", "Alexander"]
for element in lista:
    print(element)

print("="*40)

for number in range(10, 0, -1):
    print(number)

print("="*40)

lista_alexanders = []
for element in lista[:]:
    print(element, lista)
    if element == "Alexander":
        lista_alexanders.append(element)
        lista.remove(element)

print(lista, len(lista))
print(lista_alexanders, len(lista_alexanders))

# enumarate()