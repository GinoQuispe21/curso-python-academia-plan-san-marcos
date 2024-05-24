from datetime import date

class CalculadoraContable:

    @staticmethod
    def calcular_salario(salario_base, tiempo_empresa, porcentaje_aumento):
        if tiempo_empresa > 6:
            aumento = (tiempo_empresa - 6) * salario_base * porcentaje_aumento
            return salario_base + aumento
        else:
            return salario_base

    @staticmethod
    def pago_cts(empleado):
        current_date = date.today().month
        if current_date == 5 or current_date == 11:
            cts = empleado.salario * empleado.tiempo_empresa / 12
            print(f"La CTS del empleado {empleado.apellido} es: {cts}")
        else:
            print("No es una fecha de pago de CTS")

class Empleado:

    def __init__(self, nombre, apellido, dni, tiempo_empresa) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tiempo_empresa = tiempo_empresa

    def mostrar_info_trabajador(self):
        print(f"Nombre: {self.nombre}")
        print(f"apellido: {self.apellido}")
        print(f"dni: {self.dni}")
        print(f"Tiempo en empresa: {self.tiempo_empresa}")

class Desarrollador(Empleado):
    
    salario_base = 3_500
    porcentaje_aumento = 0.05

    def __init__(self, nombre, apellido, dni, tiempo_empresa, lenguaje_programacion) -> None:
        super().__init__(nombre, apellido, dni, tiempo_empresa)
        self.salario = CalculadoraContable.calcular_salario(
            tiempo_empresa = tiempo_empresa,
            salario_base= self.salario_base,
            porcentaje_aumento = self.porcentaje_aumento
        )
        self.lenguaje_programacion = lenguaje_programacion

    def mostrar_info_trabajador(self):
        super().mostrar_info_trabajador()
        print(f"Salario: {self.salario}")
        print(f"Lenguaje de programacion: {self.lenguaje_programacion}")
        print("-"*50)



class Designer(Empleado):
    
    salario_base = 2_200
    porcentaje_aumento = 0.03

    def __init__(self, nombre, apellido, dni, tiempo_empresa, programa_ui_ux) -> None:
        super().__init__(nombre, apellido, dni, tiempo_empresa)
        self.salario = CalculadoraContable.calcular_salario(
            tiempo_empresa = tiempo_empresa,
            salario_base= self.salario_base,
            porcentaje_aumento = self.porcentaje_aumento
        )
        self.programa_ui_ux = programa_ui_ux

desarrollador_1 = Desarrollador("Jorge Andres", "Ramirez Castillo", "12345678", 5, "javascript")
desarrollador_2 = Desarrollador("Lucas Gabriel", "Mendoza Vasquez", "12345672", 10, "python")

desarrollador_1.mostrar_info_trabajador()
desarrollador_2.mostrar_info_trabajador()

designer_1 = Designer("Jorge Andres", "Ramirez Castillo", "12345678", 5, "Figma")
CalculadoraContable.pago_cts(designer_1)