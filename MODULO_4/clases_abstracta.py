from abc import ABC, abstractclassmethod, abstractmethod

class User(ABC):
    @abstractclassmethod
    def login(self): pass
    @abstractclassmethod
    def register(self): pass

class User_not_deprecated(ABC):
    @classmethod
    @abstractmethod
    def login(self): pass

class Customer(User):
    def __init__(self, nombre, email, password) -> None:
        self.nombre = nombre
        self.email = email
        self.password = password
        super().__init__()
    def login(self):
        print("Se realizo el login correctamente")
    def register(self):
        print("Se registro correctamente")

class Admin(User_not_deprecated):
    def __init__(self, nombre, email, password) -> None:
        self.nombre = nombre
        self.email = email
        self.password = password
        super().__init__()
    def login(self):
        print("Se realizo el login correctamente usando la manera nueva")

customer_1 = Customer("Pedro", "pedro@gmail.com", "123456")
customer_1.login()

admin_1 = Admin("Juan", "juan@gmail.com", "123456")
admin_1.login()

    
