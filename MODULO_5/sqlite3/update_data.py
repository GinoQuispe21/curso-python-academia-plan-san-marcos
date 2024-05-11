import sqlite3 as sql

connection = sql.connect("university.db")
cursor = connection.cursor()

# cursor.execute("""
# UPDATE students SET last_name = 'Diaz Castillo'
# WHERE fist_name = 'Ramiro' AND email = 'ramiroe@outlook.com'
# """)

cursor.execute("SELECT rowid, * FROM students")
all_students = cursor.fetchall()
for student in all_students:
    print(student)

cursor.execute("""
UPDATE students
SET last_name = "Diaz Perez",
    score_pc_1 = 20
WHERE rowid = 5
""")

connection.commit()
connection.close()