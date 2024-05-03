def decorador_show_list(function):
    def wraper():
        lista = function()
        for index, element in enumerate(lista):
            print(f"Index: {index} | Element: {element}")
    return wraper

@decorador_show_list
def generador_lista():
    return [i for i in range(0, 10)]

# generador_lista()

class User:

    def __init__(self, email, password) -> None:
        self._user_email = email
        self.__user_password = password

    @property # solamente agrega logica de un getter -> obtener su valor
    def correo(self):
        return self._user_email
    
    @correo.setter # agrega logica de un setter -> actualizar el valor de un atributo de clase
    def correo(self, new_value):
        self._user_email = new_value

    @correo.deleter
    def correo(self):
        del self._user_email
        print("Se elimino el atributo _user_email de la isntancia de la Clase")

    def login(self): pass

user_12312 = User("gquispe@gmail.com", "1d2038u19nasnd")
# print(user_12312._user_password) # Obtener valor -> getter
# user_12312._user_password = "contrasena" # Asignar un valor -> setter
# print(user_12312._user_password)
print(user_12312.correo)
user_12312.correo = "salvador@outlook.com"
print(user_12312.correo)
del  user_12312.correo
#print(user_12312.correo)

from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):

    @abstractmethod
    def caluclar_area(): pass

    @abstractmethod
    def calcular_perimetro(): pass

class Rectangulo(FiguraGeometrica):

    def __init__(self, lado, ancho) -> None:
        self.lado = lado
        self.ancho = ancho

    def calcular_perimetro(self):
        return (2 * self.lado) + (2 * self.ancho)
    
    def caluclar_area(self):
        return (self.lado * self.ancho)

rectangulo_1 = Rectangulo(10, 20)
print(rectangulo_1.calcular_perimetro())
print(rectangulo_1.caluclar_area())