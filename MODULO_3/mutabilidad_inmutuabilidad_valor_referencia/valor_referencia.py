# Asignacion por valor
# Las variables comunes como str, int, flotante, bool -> Inmutables

a = 10
b = a
print(f"a: {a}, id: {id(a)}")
print(f"b: {b}, id: {id(b)}")
a = a + 10
print(f"a: {a}, id: {id(a)}")
print(f"b: {b}, id: {id(b)}")

variable_1 = 10

def funcion_mostrar_valor(variable):
    variable = 21
    print(f"2. Variable 1: {variable} | id: {id(variable)}")

print(f"1. Variable 1: {variable_1} | id: {id(variable_1)}")
funcion_mostrar_valor(variable_1)
print(f"3. Variable 1: {variable_1} | id: {id(variable_1)}")

# Asignacion por referencia:

lista_1 = [1, 2, 3]
lista_2 = lista_1
print(f"lista_1: {lista_1}, id: {id(lista_1)}")
print(f"lista_2: {lista_2}, id: {id(lista_2)}")
lista_2[0] = "Jeriot"
print(f"lista_1: {lista_1}, id: {id(lista_1)}")
print(f"lista_2: {lista_2}, id: {id(lista_2)}")

lista_3 = [10, 21, 100]

def funcion_mostrar_referencia(lista):
    lista.append(10000)
    print(f"2. lista_3: {lista} | id: {id(lista)}")

print(f"1. lista_3: {lista_3} | id: {id(lista_3)}")
funcion_mostrar_referencia(lista_3)
print(f"3. lista_3: {lista_3} | id: {id(lista_3)}")

