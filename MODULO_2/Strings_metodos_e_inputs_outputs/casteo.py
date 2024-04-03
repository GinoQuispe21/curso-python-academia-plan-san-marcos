# Casteo: Transformar de un tipo de dato a otro tipo de dato
# En python la funcion de casteo es generalmente con el mismo nombre de la clase a la que hace referencia el tipo de dato

a = int(input("Ingrese un numero entero: "))
suma = a + 20
print(suma)

a = 1
print(type(a))

veracidad = bool(a)
print(type(veracidad))

numero = 100
texto_numero = str(numero)
print(texto_numero, type(texto_numero))