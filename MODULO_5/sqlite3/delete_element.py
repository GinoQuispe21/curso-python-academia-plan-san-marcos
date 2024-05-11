import sqlite3 as sql

connection = sql.connect("university.db")
cursor = connection.cursor()

cursor.execute("DELETE FROM students WHERE rowid = 4")

connection.commit()
connection.close()