# Mutabilidad -> capcidad de un objeto de poder cambiar su valor
# Listas, diccionarios, conjuntos/sets, clases

lista_1 = [1, 2, 3]
print(f"{lista_1} | {type(lista_1)} | {id(lista_1)}")
lista_1[0] = "Dos"
print(f"{lista_1} | {type(lista_1)} | {id(lista_1)}")

# Inmutabilidad -> Capacidad de un objeto de no poder modificar su valor
# Tipos de datos comunes, tuplas, range

rango = range(10)
# rango[0] = 1 -> no se puede hacer una reasginacion de valor ya que es inmutable
print(f"{rango} | {type(rango)} | {id(rango)}")

primera_tupla = (1, 2.9, "7")
print(f"{primera_tupla} | {type(primera_tupla)} | {id(primera_tupla)}")
# primera_tupla[0] = 100 -> no se puede hacer una reasginacion de valor ya que es inmutable

variable = 100
print(f"{variable} | {type(variable)} | {id(variable)}")
variable = variable + 100
print(f"{variable} | {type(variable)} | {id(variable)}")

# Excepcion de inmutabilidad -> El objeto tupla puede parecer que es mutable cuando almacena una lista
# ya que la lista si es mutable permitira cambiar su valor
segunda_tuple = (1, 2.0, "3", ["gino", "alexander", "jeriot", "guillermo"])
print(f"{segunda_tuple} | {type(segunda_tuple)} | {id(segunda_tuple)}")
segunda_tuple[3][0] = "Marce"
print(f"{segunda_tuple} | {type(segunda_tuple)} | {id(segunda_tuple)}")

# Excepcion de mutabilidad 
mi_lista = [1, 2, 3, ("Gino", "Alexander")]
print(f"{mi_lista} | {type(mi_lista)} | {id(mi_lista)}")
mi_lista[3][0] = "Marce"
print(f"{mi_lista} | {type(mi_lista)} | {id(mi_lista)}")