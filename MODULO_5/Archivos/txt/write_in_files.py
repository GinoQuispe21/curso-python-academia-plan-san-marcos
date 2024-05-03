with open("MODULO_5/Archivos/txt/example_write.txt", mode = 'w') as stream_write:
    stream_write.write("Primera linea\nSegunda Linea\nTercera linea\n")
    stream_write.writelines([
        "Soy la primera linea del writelines\n",
        "Soy la segunda linea del writelines\n",
        "Soy la tercera linea del writelines\n"
    ])
    stream_write.write(
        """
Gino
Jorge
Rodrigo
Marcelo
Juan
""")
    
with open("MODULO_5/Archivos/txt/example_write.txt", mode = 'a') as stream_append:
    stream_append.write("Soy una nueva linea agregada por la apertura append\n")
    stream_append.write("Soy la segunda linea agregada por la apertura append\n")
    stream_append.writelines([
        "1\n",
        "2\n",
        "3",
    ])
