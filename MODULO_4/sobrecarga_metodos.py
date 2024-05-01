class User:
    def __init__(self, email, password, username) -> None:
        self.email = email
        self.password = password
        self.username = username
    def signIn(self):
        pass

class Admin(User):

    __admin_email = "admin@gmail.com"
    __admin_password = "admin"
    __type_users_admin = {1: "Full Administrador", 2: "Administrador de BD", 3: "Administrador de publicaciones"}
    __security_token = ""

    def __init__(self, email, password, username, type_user) -> None:
        super().__init__(email, password, username)
        self.type_user = type_user

    @property
    def tipo_usuario(self):
        return self.type_user
    
    @tipo_usuario.setter
    def tipo_usuario(self, new_type_user):
        self.type_user = new_type_user

    @property
    def nombre_usuario(self):
        return self.type_user

    @nombre_usuario.deleter
    def nombre_usuario(self):
        del self.username

    def __validate_token(self) -> bool:
        return True if len(self.__security_token) > 0 else False
    
    def signIn(self):
        if (self.email == self.__admin_email and 
            self.password == self.__admin_password and
            self.type_user in self.__type_users_admin.keys()):
            # En una app real digamos que esto retrona un valor encriptado
            self.__security_token = "md1iu2h471n2809ena8da0sdn1-981j2893k9m9ouiamsdiomauiodmi1mijo2m391m29m9mx91%!$!@$!@$!"
    
    def manage_bd(self):
        if self.__validate_token() and self.type_user == 2:
            print("El usuario puede acceder a manejar la base de datos")
        elif self.type_user != 2:
            print("Este usuario administrador no tiene permisos para esta funcionalidad")
        else:
            print("Credenciales incorrectas")
   
    def manage_posts(self):
        if self.__validate_token() and self.type_user == 3:
            print("El usuario puede acceder a manejar la base de datos")
        elif self.type_user != 2:
            print("Este usuario administrador no tiene permisos para esta funcionalidad")
        else:
            print("Credenciales incorrectas")

admin_3_bd = Admin(email = "admin@gmail.com", username = "admin", password = "admin", type_user = 2)
admin_3_bd.signIn()
admin_3_bd.manage_bd()
print(admin_3_bd.type_user)