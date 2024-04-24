class CuentaBancaria:
    # atributo de clase
    interes = 0.06
    # Constructor:
    def __init__(self, nombre, correo, dni) -> None:
        # atributos de instancia
        self.nombre_usuario = nombre
        self.correo_usuario = correo
        self.dni_usuario = dni
    
cuenta_bancaria_1 = CuentaBancaria("Alexander", "alexanderpatino@gmail.com", "75121312")
cuenta_bancaria_2 = CuentaBancaria("Gino", "gquispec@gmail.com", "751213123")
print(cuenta_bancaria_1.correo_usuario)
print(cuenta_bancaria_1.interes)

print(cuenta_bancaria_2.correo_usuario)
print(cuenta_bancaria_2.interes)

cuenta_bancaria_3 = CuentaBancaria(nombre = "Mathias", correo = "usuario123@gmail.com", dni = "12312412")

class Perro:
    __cansancio = 0 # atributo privado (__) -> solo puede ser accedido dentro de la clase
    # __init__ es un metodo que se conoce como constructor
    def __init__(self, nombre, edad, raza, peso) -> None:
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
    # metodo correr
    def correr(self, distancia = float):
        if self.__cansancio >= 50:
            print(f"{self.nombre} esta cansado. No puede correr por ahora.")
        else:
            print(f"{self.nombre} esta corriendo {distancia}km. ")
            self.__cansancio += 50
    # metodo correr
    def descanso(self, horas_descanso = int):
        if horas_descanso >= 6:
            self._resetear_cansancio()
        if horas_descanso <= 5:
            self.__cansancio -= (horas_descanso * 10)
            print(f"{self.nombre} ha descansado y su cansancio ahora es: {self.__cansancio}")
        else:
            print(f"{self.nombre} no duerme mas de 5 horas")
    def _resetear_cansancio(self): # metodo protegido (_) -> puede ser accedido desde fuera de la clase pero no deberia
        self.__cansancio = 0

fido = Perro(nombre = "Fido", edad = 4, raza = "Pitbull", peso = 10)
print(fido.nombre)
fido.correr(10.5)
fido.correr(10.5)
fido.descanso(4)
fido.correr(5)

peluchin = Perro(nombre = "Peluchin", edad = 17, raza = "Shitsu", peso = 7)
print(peluchin.nombre)
peluchin.correr(10)
peluchin._resetear_cansancio()
peluchin.correr(10)
