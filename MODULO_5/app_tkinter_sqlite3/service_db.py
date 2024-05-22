import sqlite3 as sql
from tkinter import messagebox
from datetime import datetime
from home_view import HomeView

class ServiceDB:

    def __init__(self, path, mock: bool = False) -> None:
        self.__conection = sql.connect(path)
        self.__cursor = self.__conection.cursor()
        self.__launch_instance_db()
        if mock == True:
            self.__add_mock_users()

    def login(self, window, service, email, password):
        self.__cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        usuario = self.__cursor.fetchone()
        if usuario != None:
            self.__register_login_hours(usuario[0])
            messagebox.showinfo(
                title = "Inicio de sesion exitoso!",
                message = "Se logro iniciar sesion correctamente!"
            )
            HomeView(window = window, service = service, user = usuario)
        else:
            messagebox.showerror(
                title = "Error al iniciar sesion!",
                message = "No se pudo iniciar sesion, intente nuevamente."
            )

    def add_product(self, name, description, price, stock) -> bool:
        try:
            current_datetimte = self.__get_current_datetime()
            self.__cursor.execute("""
            INSERT INTO products (product_name, description, price, stock, created_at)
            VALUES (?, ?, ?, ?, ?)""", (name, description, float(price), int(stock), current_datetimte))
            self.__conection.commit()
            return True
        except Exception as error:
            print(f"Excepction: {error}")
            return False

    def get_all_products(self):
        self.__cursor.execute("SELECT * FROM products")
        all_products = self.__cursor.fetchall()
        return all_products

    def __register_login_hours(self, user_id):
        current_date = self.__get_current_datetime()
        self.__cursor.execute("""
        INSERT INTO user_login_record (id_user, login_date_hour) VALUES (?, ?)
        """, (user_id, current_date))
        self.__conection.commit()

    def __get_current_datetime(self):
        return datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def  __launch_instance_db(self):
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            email TEXT NOT NULL,
                            password TEXT NOT NULL
        )
        """)
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_login_record (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            id_user INTEGER,
                            login_date_hour DATETIME
        )
        """)
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              product_name TEXT,
                              description TEXT,
                              price REAL,
                              stock INTEGER,
                              created_at DATETIME
        )
        """)
        self.__conection.commit()

    def __add_mock_users(self):
        data = {
            ("ginoquispecalixto@gmail.com", "password"),
            ("admin", "123"),
            ("alexander0232@outlook.com", "12345password")
        }
        self.__cursor.executemany("INSERT INTO users (email, password) VALUES (?, ?)", data)
        self.__conection.commit()

    def close_conection(self):
        self.__conection.close()