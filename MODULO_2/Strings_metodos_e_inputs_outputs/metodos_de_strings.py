nombre_alumno = "Rodolfo"

# 1. capitalize() -> El metodo capitalize coloca el primer caracter en mayuscula y el resto en minuscula
titulo_libro = "lA SOCIEDAD DE LA NIEVE"
titulo_correcto = titulo_libro.capitalize()
print("Metodo capitalize: ", titulo_correcto)

# 2. upper() -> El metodo upper transforma todos los caracteres a maysucula
print("Metodo upper: ", nombre_alumno.upper())

# 3. lower() -> El metodo lower transforma todos los caracteres a minusculas
print("HOLA ME LLAMO GINO".lower())

# 4. title() -> El primer caracter de todas las palbras sera en maysuculas y el resto en minusculas
print("Metodo title: ", titulo_libro.title())

# 5. strip() -> Nos ayuda a eliminar espacioes en blanco del inicio y del final
mensaje = "     me olvide lo que te iba a decir    "
print("Total de caracteres de mensaje: ", len(mensaje))
nuevo_mensaje = mensaje.strip()
print("Total de caracteres de mensaje tras eliminar espacios en blanco: ", len(nuevo_mensaje))
print(nuevo_mensaje)
# Adicional: esta fucnion tambien acepta un argumetno/parametro
print("abc oasmdkalmdlasmdlask abc".strip("abc"))

# 6. rstrip() -> right strip, derecha
# lstrip() -> left strip, izquiero
mensaje_bizarro = "abc oasmdkalmdlasmdlask    "
print(len(mensaje_bizarro))
nuevo_mensaje = mensaje_bizarro.rstrip()
print(len(nuevo_mensaje))

print("abc oasmdkalmdlasmdlask abc".rstrip("abc"))
print("abc oasmdkalmdlasmdlask abc".lstrip("abc"))


# Metodo isdigit() -> retorna true si los caracteres son digitos del 0 al 9
is_digit = "1234".isdigit()
print("Es un digito?", is_digit)
print("¹²³".isdigit())
print("Ⅳ".isdigit())

# Metodo isnumeric()
print("Ⅳ".isnumeric())

# Replace -> Remplazar un texto a por un texto b
lista_compras = "Leche, papel higienico, verduras, carnes, yogurt"
# El primer argumento es para encontrar la cadena de texto en el texto original, y el segundo argumento es el de remplazo
print(lista_compras.replace("papel higienico", "vino"))

# find -> Encontrar/ Lo que hace es encontrar el inidice de iniicio de cierta cadena de texto
print(lista_compras.find('papel')) # Retorna indices, la busqueda es de izquierda a derecha

# rfind -> La busqueda sera desde el lado derecho/right
nueva_lista_compras = "Leche, papel higienico, verduras, carnes, yogurt, Leche"
print(lista_compras.rfind('Leche'))

# count -> Contador, cuenta la cantidad de veces que aparece una cadena de texto en el texto original
print(nueva_lista_compras.count('Leche'))

# startswith() -> Retorna un valor booleano True si el caracter que se pase como a argumetno es el caracter o caracteres con el cual inicia el texto origianl
print("Hola mundo, que tal les va?".startswith('Hola mundo,'))

# endswith() -> Retorna valor booleano, funcionamiento similar a startswith pero desde el final
print("Hola mundo, que tal les va?".endswith('va?'))

# split() -> Este metodo retorna la lista de caracteres como un elemento de un arreglo/lista
print("Gino,Pedro,Rodrigo,Rodolfo,Jeriot".split(','))



