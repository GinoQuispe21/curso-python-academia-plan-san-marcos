x = 5 # = : Sirve para asignar un valor a una variable
# == : Operador de comparacion de un valor con otro valor, que retornara una valor booleano (True o False)

# Para ejecutar una condicion dentro de una sentencia if, el valor de la condicional siempre debe ser verdadera
if x < 10:
    print("x es menor que 10")
else: # El codigo dentro de la sentencia else se ejecuta cuando la condicional del if sea falsa
    print("x es mayor que 10")

a = 10 == 10
print(a)

b = 21 != 21 # != : Hace una comparacion de valores desiguales
print(b)

c = 21 >= 21
print(c)

a = "Gino"
b = "Pedro"

if a != b:
    print("Las variables tienen nombres diferentes")
else:
    print("Las variables tienen nombres iguales")

"Operadores Logicos"

# and : y
# or: o
# xor:
# not: negacion

arg1 = False
arg2 = True

print("Condicional and: ", arg1 and arg2)
print("Condicional or: ", arg1 or arg2)
print("Condicional xor: ", arg1 ^ arg2)
print("Negacion de arg1: ", not arg1)
print("Negacion de arg2: ", not arg2)

nombre = "Gino"

# in, not in
# in: esta dentro de
print('i' in nombre)
print('g' not in nombre)

print(nombre[0])