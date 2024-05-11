import sqlite3 as sql
from datetime import datetime

class DataBaseManager:

    _connection = None
    _cursor = None

    def __init__(self, name_db: str, table_to_manage: str, path_db: str = None) -> None:
        self._name_db = name_db
        self._table_to_manage = table_to_manage
        self._path_db = path_db
        pass

    def start_conection(self):
        if self._path_db != None: 
            self._connection = sql.Connection(self._path_db + "/" + self._name_db)
        else:
            self._connection = sql.Connection(self._name_db)
        self._cursor = self._connection.cursor()

    def create_table(self):
        if self._connection != None and self._cursor != None:
            self._cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {self._table_to_manage} (
            id INTEGER PRIMARY KEY,
            id_usuario INTEGER,
            hora_registro DATETIME
            )
            """)
            self.__commit_changes()
            print("Se creo la tabla correctamente :D")
        else:
            print("No ha instanciado su conexio o cursor")

    def insert_data(self, id_user):
        datetime_now = self.__formato_fecha_hora(datetime.now())
        self._cursor.execute(f"""
                             INSERT INTO {self._table_to_manage} (id_usuario, hora_registro) 
                             VALUES (?,?)""", (id_user, datetime_now))
        self.__commit_changes()

    def drop_table(self):
        self._cursor.execute(f"DROP TABLE {self._table_to_manage}")

    def __formato_fecha_hora(self, fecha_hora):
        return fecha_hora.strftime('%Y-%m-%d %H:%M:%S')

    def __commit_changes(self):
        self._connection.commit()

    def close_conection(self):
        self._connection.close()

db_manager = DataBaseManager(
    name_db = "user_activity_record.db",
    path_db = "MODULO_5/sqlite3/ejercicios",
    table_to_manage = "activity_record"
)

def user_login(user_id):
    # ... validacion de credenciales
    db_manager.insert_data(id_user= user_id)

db_manager.start_conection()
#db_manager.drop_table()
db_manager.create_table()

user_login(100231)

db_manager.close_conection()

