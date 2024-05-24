import sqlite3 as sql
from datetime import datetime

class ManagerDB:

    def __init__(self) -> None:
        self.__connection = sql.connect("EVALUACIONES/PC02/almacen.db")
        self.__cursor = self.__connection.cursor()

    def create_table(self):
        self.__cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              name TEXT NOT NULL,
                              description TEXT,
                              brand TEXT,
                              created_at DATETIME,
                              stock INTEGER,
                              price REAL
        )
        """)
        self.__connection.commit()

    def add_product(self, name, description, brand, stock, price):
        datetime_var = self.__formateo_fecha_hora()
        self.__cursor.execute("""
        INSERT INTO products (
                              name,
                              description,
                              brand,
                              created_at,
                              stock,
                              price
        ) VALUES (?, ?, ?, ?, ?, ?)""", (name, description, brand, datetime_var, stock, price))
        self.__connection.commit()

    def add_products(self, data):
        self.__cursor.executemany("""
        INSERT INTO products (
                        name,
                        description,
                        brand,
                        created_at,
                        stock,
                        price
        ) VALUES (?, ?, ?, ?, ?, ?) """, data)
        self.__connection.commit()

    def update_products(self, product_id, new_name, new_description):
        where_query = f"id = {product_id}"
        query = "UPDATE products SET name = ?, description = ? WHERE " + where_query
        self.__cursor.execute(query, (new_name, new_description))
        self.__connection.commit()

    def delete_products(self, product_id):
        self.__cursor.execute(f"DELETE FROM products WHERE id = {product_id}")
        self.__connection.commit()

    def __formateo_fecha_hora(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def cerrar_conexion(self):
        self.__connection.close()


manager = ManagerDB()
manager.create_table()
# manager.add_product(
#     name = "coca cola",
#     description = "gaseosa de 3 litros",
#     brand = "Coca Cola",
#     stock = 100,
#     price = 5.60
# )
#manager.update_products(product_id=1, new_name="inca cola", new_description = "gaseosa peruana de 3L")
manager.delete_products(product_id = 1)