stream = open("MODULO_5/Archivos/txt/example.txt", mode = "r")
print(stream.read())
stream.close() # Importante: cerrar archivos despues de modificarlos
#print(stream.read())

with open("MODULO_5/Archivos/example.txt", mode = "r") as stream_1:
    for line in stream_1.readlines():
        print(line.upper().rstrip())
    
#print(stream_1.read())