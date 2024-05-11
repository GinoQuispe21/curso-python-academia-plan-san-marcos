import sqlite3 as sql

connection = sql.connect("university.db")
cursor = connection.cursor()

cursor.execute("select rowid, * from students order by score_pc_1 desc limit 4")

all_students = cursor.fetchall()

for student in all_students:
    print(student)

connection.commit()
connection.close()