# Frozenset es un objeto inmutable a diferencia del set
# No permite cambiar su longitud ni cambiar sus valroes despues de haber sido reado
# Comparte caracteristicas similares a las de un set

conjunto_inmutable = frozenset({'a', 'b', 'c', 'd'})
print(f"Valores de conjunto: {conjunto_inmutable} | type: {type(conjunto_inmutable)}")

conjunto_inmutable_pares = frozenset(range(0, 20, 2))
print(f"Valores de conjunto pares: {conjunto_inmutable_pares} | type: {type(conjunto_inmutable_pares)}")

# conjunto_inmutable.add('e') # Excepcion: 'frozenset' object has no attribute 'add'
print(conjunto_inmutable)

print(len(conjunto_inmutable))