import sqlite3 as sql

connection = sql.connect("university.db")
cursor = connection.cursor()

# cursor.execute("DROP TABLE teachers")

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               last_name TEXT,
               dni TEXT UNIQUE,
               course_name TEXT
)
""")

new_students = [
    ("Gino", "Quispe Calixto", "1", "Python para desarrollo web"),
    ("Anthony", "Aponte Felix", "2", "Matlab"),
]

# cursor.executemany("INSERT INTO teachers (name, last_name, dni, course_name) VALUES (?,?,?,?)", new_students)

cursor.execute("DELETE FROM teachers WHERE rowid = 3")

connection.commit()
connection.close()