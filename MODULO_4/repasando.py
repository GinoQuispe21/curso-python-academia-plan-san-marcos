class User:
    __is_login = False
    # Constructor de mi clase User
    def __init__(self, email, name, password) -> None:
        self.user_name = name
        self.user_email = email
        self.password = password

    def _was_login(self):
        if self.__is_login == True:
            print("El usuario ya ha tenido una sesion iniciada anteriromente")
            return True

    # Inicio de sesion
    def login(self, username, password):
        # Peticion a internet / request -> se espera una respuesta (response) -> token de seguridad
        if self._was_login() == True or (self.user_name == username and self.password == password):
            print("Usted ya tiene una sesion iniciada :)")
            self.__is_login = True
        else:
            print("Las credenciales son imbalidas")
            self.__is_login = False

    def show_products(self):
        if self.__is_login == True:
            print(f"Los productos recomendados para el usuario {self.user_name} son: ")
            print("Lista de productos...")
        else: 
            print("El usuario no ha iniciado sesion")


user_gino = User("gquispec@gmail.com", "ginoQuispe", "contrasena")
user_gino._was_login
# mucho codigo x

user_gino.login("ginoQuispe", "contrasena")
user_gino.show_products()