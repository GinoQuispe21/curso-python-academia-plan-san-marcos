import sqlite3 as sql

class ServiceDB:

    def __init__(self, path) -> None:
        self.__conection = sql.connect(path)
        self.__cursor = self.__conection.cursor()
        self.__launch_instance_db()

    def  __launch_instance_db(self):
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              email TEXT NOT NULL,
                              password TEXT NOT NULL
        )
        """)
        self.__conection.commit()

    def close_conection(self):
        self.__conection.close()