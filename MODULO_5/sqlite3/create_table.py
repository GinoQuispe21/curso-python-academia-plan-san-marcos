import sqlite3

connection = sqlite3.connect("university.db") # Establecemos la conexion con la bd
cursor = connection.cursor() # Creamos cursor para manejar la bd conectada

# Ejecutamos la query/consulta que realiza la creacion de la tabla
cursor.execute("""
CREATE TABLE students(
    fist_name TEXT,
    last_name TEXT,
    age INTEGEER,
    email TEXT,
    birth_date DATE,
    score_pc_1 REAL
)
""")

# Realizamos la confirmacion
connection.commit()
# Cerramos la conexion
connection.close()