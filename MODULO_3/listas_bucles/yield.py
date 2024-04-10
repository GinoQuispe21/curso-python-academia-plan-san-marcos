# yield -> usado para funciones generadoras

def generador_suma(numero):
    yield numero + 1
    yield numero + 2
    yield numero + 3

generator = generador_suma(10)

# print(generator, type(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

for element in generator:
    print(element)

def generador_numeros_pares(limite):
    for number in range(0, limite + 1, 2):
        yield number

limite_number = 10
generator_pares = generador_numeros_pares(limite_number)
print(type(generator_pares))
for numero_par in generator_pares:
    print(numero_par)