class Persona:
    def __init__(self, nombre, dni, edad, genero, nacionalidad) -> None:
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.genero = genero
        self.nacionalidad = nacionalidad
    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tengo {self.edad} años, y soy {self.nacionalidad}")

# Al poner entre parentesis una clase, Python automaticamente definira esta como la clase padre/superclass de la clase que se esta definiendo
class Profesor(Persona):
    def __init__(self, nombre, dni, edad, genero, nacionalidad, tiempo_dictando, curso, institucion) -> None:
        super().__init__(nombre, dni, edad, genero, nacionalidad)
        self.tiempo_trabajando_meses = tiempo_dictando
        self.nombre_curso = curso
        self.nombre_institucion = institucion
    def presentacion_curso(self):
        print(f"Buenas tardes, mi nombre es {self.nombre}. Bienvenidos al curso de {self.nombre_curso}")

class Estudiante(Persona):
    pass

profesor_1 = Profesor("Gino Quispe Calixto", 123124124, 23, "Masculino", "Peruano", 12, "Python para desarrollo web", "Plan San Marcos")
profesor_1.presentarse()
profesor_1.presentacion_curso()

persona_1 = Persona("Mathias Cabezas", 123124122, 25, "Masculino", "Peruano")
persona_1.presentarse()
# persona_1.presentacion_curso()

print(Persona.__base__) # <class 'object'>
print(Profesor.__base__)

estudiante_1 = Estudiante("Piero Acevedo", 5124141, 23, "Masculino", "Peruano")
print(estudiante_1.nombre)