import sqlite3 as sql

connection = sql.connect("university.db")
cursor = connection.cursor()

# cursor.execute("""
# INSERT INTO students VALUES(
#     "Marce",
#     "Perez Godoy",
#     25,
#     "marce_25@gmail.com",
#     "1999-11-11",
#     17.5
# )
# """)

new_students = [
    ("Jorge", "Quispe Rodriguez", 30, "jorge@hotmail.com", "1995-10-12", 18.0),
    ("Ramiro", "Quispe Rodriguez", 21, "ramiroe@outlook.com", "2003-10-12", 20.0),
    ("Luis", "Quispe Rodriguez", 33, "luis@gmail.com", "1995-10-12", 14.0),
    ("Carlos", "Quispe Rodriguez", 40, "carlos@hotmail.com", "1984-10-12", 15.0)
]

def insert_elements():
    cursor.executemany("INSERT INTO students VALUES (?,?,?,?,?,?)", new_students)

insert_elements()

connection.commit()
connection.close()