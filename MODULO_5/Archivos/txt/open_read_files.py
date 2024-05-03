"""stream = open("MODULO_5/Archivos/txt/example.txt", mode = 'r', encoding = None)
print(stream) # La variable stream esta guardando el manejador para gestionar el archivo
for element in stream.readlines():
    print(element.rstrip())"""

# Metodo readable -> nos retorna un booleano determinando si un archivo puede ser leeido
stream_1 = open("MODULO_5/Archivos/txt/prueba_2.txt")
stream_2 = open("MODULO_5/Archivos/txt/prueba.txt", mode = "w")
stream_3 = open("MODULO_5/Archivos/txt/prueba.txt", mode = "a")
stream_4 = open("MODULO_5/Archivos/txt/prueba.txt", mode = "w+")
stream_5 = open("MODULO_5/Archivos/txt/prueba.txt", mode = "r+")
for element in [stream_1, stream_2, stream_3, stream_4, stream_5]:
    print(f"Stream: {element.mode} | {element.readable()}")

# Metodo read() -> lee todo una archivo y lo retorna como un string

stream_read = open("MODULO_5/Archivos/example.txt")
#full_text = stream_read.read()
#print(full_text)

# Metodo readline() -> Lee solo la primera linea del archivo

# first_line = stream_read.readline()
# print(first_line.rstrip())

# Metodo readlines() -> Lee todas las lineas del archivo, y lo almacena en un elemento de una lista

list_lines = stream_read.readlines()
# print(list_lines)
list_lines_without_spaces = []

for line in list_lines:
    list_lines_without_spaces.append(line.rstrip('\n').lstrip())

print(list_lines_without_spaces)