import sqlite3 as sql

connection = sql.connect("university.db")
cursor = connection.cursor()

# cursor.execute("SELECT * FROM students WHERE age >= 30")

#cursor.execute("SELECT * FROM students WHERE email LIKE '%@gmail.com' ")
#cursor.execute("SELECT * FROM students WHERE last_name LIKE 'Quispe%' ")

# cursor.execute("SELECT * FROM students WHERE email LIKE '%@gmail.com' AND last_name LIKE 'Quispe%'")

cursor.execute("SELECT * FROM students WHERE email LIKE '%@gmail.com' OR last_name LIKE 'Quispe%'")

students = cursor.fetchall()

print("Nombre\t\tApellido\t\tEmail")
for student in students:
    print(f"{student[0]}\t\t{student[1]}\t\t{student[3]}")

connection.commit()
connection.close()