tuple_comp = tuple([n for n in range(10, 21) if n % 2 == 0])
print(tuple_comp, type(tuple_comp))

# De esta manera no se genera una tupla por comprension, lo que estamos logrando es generar un generator
generator_1 = (n for n in ["Gino", "Jose", "Rodolfo"])
generator_1 = (n for n in ["Gino", "Jose", "Rodolfo"])
print(next(generator_1))
print(generator_1, type(generator_1))

tuple_2 = (*(element for element in range(1, 100) if element % 2 != 0),)
print(tuple_2, type(tuple_2))