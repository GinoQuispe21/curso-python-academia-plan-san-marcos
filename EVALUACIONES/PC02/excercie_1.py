class Empleado:

    def __init__(self, nombre, apellido, edad, dni, tiempo_empresa) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        self.tiempo_empresa = tiempo_empresa

    def __calcular_salario():
        pass

    def mostrar_informacion():
        pass

class EmpleadoPlanilla(Empleado):

    def __init__(self, nombre, apellido, edad, dni, tiempo_empresa, salario_mensual) -> None:
        super().__init__(nombre, apellido, edad, dni, tiempo_empresa)
        self.salario_mensual = salario_mensual

    def __calcular_salario_mensual(self):
        if self.tiempo_empresa >= 3:
            bonificacion = 100
            
        
