import sqlite3 as sql

connection = sql.connect("university.db")
cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

# all_students = cursor.fetchall() # Obtiene todos los elementos de la consulta y lo retorna en una lista de tuplas
# print(all_students, type(all_students))

# one_student = cursor.fetchone() # Obtiene un elemento de la consulta y lo retorna como tupla
# print(one_student, type(one_student))

some_students = cursor.fetchmany(3) # Limita a los n primeros elementos leidos en la query
# print(some_students, type(some_students))

print("Nombre\t\tNota PC1")
for student in some_students:
    print(f"{student[0]}\t\t{student[-1]}")

connection.commit()
connection.close()