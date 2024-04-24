numero = 20
# 20 que es literal -> es una instancia de la clase int
print(type(numero))
nombre = "Gino"
# la variable nombre almacena un objeto de la clase str
print(type(nombre))
print(nombre.upper())
# print(nombre.__dir__())

# Creando nuestra primera clase:
class Estudiante:
    # Atributo de clase
    nacionalidad = "Peruana"
    # Constructor
    def __init__(self, nombre, apellido, edad, curso, documento_identidad):
        print("Se llamo al constructor")
        # Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
        self.doc = documento_identidad
    # Metodos
    def realizar_examen(self):
        print(f"{self.nombre} esta haciendo el examen")
    def mirar_clase(self):
        print(f"El alumno registrado con documento: {self.doc} esta viendo la clase")

# estudiante_1 es una variable que almacena un objeto de la clase Estudiante
# objeto = instancia de una clase
estudiante_1 = Estudiante("Jorge", "Mauricio", 20, "Python para desarrollo web", 8123812)
print(estudiante_1.edad)
estudiante_1.realizar_examen()
estudiante_1.mirar_clase()
print(type(estudiante_1))