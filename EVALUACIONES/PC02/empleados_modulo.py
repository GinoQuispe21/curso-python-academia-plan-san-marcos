registro_empleados = {}

salario_dict = dict(
    Limpieza = 1_025,
    Mesero = 1_500,
    Cajero = 1_500,
    Vigilante = 1_400,
    Gerente = 2_500
)

def menu():
    print("""
====================== Gestion de Empleados ========================
|| 1. Visualizar informacion de un empleado.                      ||
|| 2. Mostrar empleado cuyo tiempo en la empresa sea el menor     ||
|| 3. Actualizar salario de un empleado                           ||
|| 4. Terminar programa                                           ||
====================================================================
""")

def print_info_employee(employee):
    print(f"""
>>> Nombre: {employee["nombre_completo"]}
>>> DNI: {employee["dni"]}
>>> Telefono: {employee["telefono"]}
>>> Tiempo trabajando (meses): {employee["tiempo_trabajando"]}
>>> Cargo: {employee["cargo"]}
>>> Salario: {employee["salario"]}
>>> ============================================
""")

def print_info_employee_minimum_hour(id_employee):
    print(f"""
>>> Id: {id_employee}
>>> Nombre: {registro_empleados[id_employee]["nombre_completo"]}
>>> Tiempo trabajando (meses):  {registro_empleados[id_employee]["tiempo_trabajando"]}
""")

# Inputs del app

def input_id():
    completed = False
    while not completed:
        try:
            id_number = int(input("- Id: "))
            if id_number not in registro_empleados.keys():
                completed = True
                return id_number
            else:
                raise Exception(id_number)
        except ValueError:
            print("El valor ingresado es erroneo, ingrese un valor numerico.")
        except Exception as error:
            print(f"Ya hay un usuario registrado con el Id: {error.args[0]}. Intentelo nuevamente.")

def input_full_name():
    completed = False
    while not completed:
        try:
            full_name = input("- Nombre Completo: ")
            list_full_name = full_name.split()
            if len(list_full_name) >= 2:
                completed = True
                return full_name
            else:
                raise Exception("Debe ingresar un nombre y un apellido minimo.")
        except Exception as error:
            print(error)

def input_dni():
    completed = False
    while not completed:
        try:
            dni = input("- DNI: ")
            if len(dni) == 8:
                completed = True
                return dni
            else:
                raise Exception("El DNI debe tener 8 digitos. Intente nuevamente.")
        except Exception as error:
            print(error)

def input_phone():
    completed = False
    while not completed:
        try:
            phone = input("- Telefono: ")
            if len(phone) == 9:
                completed = True
                return phone
            else:
                raise Exception("El numero de celular debe tener 9 digitos. Intente nuevamente.")
        except Exception as error:
            print(error)

def input_months():
    completed = False
    while not completed:
        try:
            phone = int(input("- Tiempo trabajando (meses): "))
            if phone > 0:
                completed = True
                return phone
            else:
                raise Exception("Debe ingresar un mes mayor a 0.")
        except Exception as error:
            print(error)

def input_position():
    completed = False
    while not completed:
        try:
            position = input("- Cargo: ")
            position_capitalize = position.capitalize()
            if position_capitalize in salario_dict.keys():
                completed = True
                return position_capitalize
            else:
                raise Exception("El cargo ingresado es erroneo. Intentlo nuevamente.")
        except Exception as error:
            print(error)

def input_continue_register():
    completed = False
    while not completed:
        try:
            answer = input("> Quiere ingresar un nuevo empleado al registro? (Si/ No): ")
            answer_upper = answer.upper()
            if answer_upper == "NO" or answer_upper == "SI":
                completed = True
                return True if answer_upper == "NO" else False
            else:
                raise Exception("El valor ingresado es erroneo. Intente nuevamente.")
        except Exception as error:
            print(error)

def input_menu_option():
    completed = False
    while not completed:
        try:
            option = int(input("> Elija la opcion que desee realizar (1/2/3/4): "))
            if option > 4 or option < 1:
                raise Exception("Opcion ingresada erronea, ingrese entre la opción 1 al 4.")
            else:
                completed = True
                return option
        except ValueError:
            print("El valor ingresado es erroneo, ingrese un valor numerico.")
        except Exception as error:
            print(error)

# Funcionalidades del app

def register_employee(
        id: int, 
        nombre_completo: str, 
        dni: str, 
        telefono: str,
        tiempo_trabajando: int, 
        cargo: str
    ):
    cargo_capitalize = cargo.capitalize()
    if cargo_capitalize in salario_dict.keys():
        registro_empleados[id] = {
            "nombre_completo": nombre_completo,
            "dni": dni,
            "telefono": telefono,
            "tiempo_trabajando": tiempo_trabajando,
            "cargo": cargo,
            "salario": salario_dict[cargo_capitalize]
        }

def visualizar_informacion_empleado():
    print(">>> ========== Visualizar Información ==========")
    try:
        id_employee = int(input(">>> Ingrese el Id del empleado: "))
        if id_employee not in registro_empleados.keys():
            raise Exception(">>> Lo sentimos, no se encontro un empleado con ese Id.")
        else:
            employee = registro_empleados[id_employee]
            print_info_employee(employee = employee)
    except ValueError:
        print(">>> El valor ingresado es erroneo, debe ingresar un valor numerico.")
    except Exception as error:
        print(error)

def return_key_for_value(value_searched, dict_base):
    for key, element in dict_base.items():
        if element == value_searched:
            return key

def mostrar_empleado_minimo_tiempo():
    print(">>> ========== Empleado con menor tiempo en la empresa ==========")
    empleados = registro_empleados.items() # Dict_items = (1: {...})
    auxiliar_id_hour = dict() # Creamos un diccionario auxiliar que usaremos para registrar un guardado del Id y la hora de manera directa
    for id_empleado, empleado in  empleados:
        auxiliar_id_hour[id_empleado] = empleado["tiempo_trabajando"] # Agregamos los elementos al diccionario
    hours_list = list(auxiliar_id_hour.values()) # Luego tendremos solo una lista de las horas de los empleados
    hora_minima = min(hours_list) # Calculamos el minimo valor de la lista de horas
    if hours_list.count(hora_minima) > 1: # Para mostrar el resultado preguntamos si hay mas de un empleado con la hora minima
        list_id_minim_hours = [] # lista auxiliar para guardar Id's
        for aux_key, aux_value in auxiliar_id_hour.items(): # recorremos la lista para buscar los empleados con la hora minima
            if aux_value == hora_minima:
                list_id_minim_hours.append(aux_key) # si es asi, agregamos el id a la lista
        for id_employee in list_id_minim_hours: # recorremos la lista auxiliar agregada
            print_info_employee_minimum_hour(id_employee) # mostramos la informacion de los empleados con menores horas trabajadas
    else:
        id_employee = return_key_for_value(hora_minima, auxiliar_id_hour)
        print_info_employee_minimum_hour(id_employee) # mostramos la informacion del empleado con menor horas trabajadas

def actualiar_salario_empleado():
    print(">>> ========== Actualizar salario de un empleado ==========")
    try:
        id_employee = int(input(">>> Ingrese el Id del empleado: "))
        if id_employee not in registro_empleados.keys():
            raise Exception(">>> Lo sentimos, no se encontro un empleado con ese Id.")
        aumento = float(input(">>> Ingrese el aumento que recibira el empleado en soles: "))
        if aumento <= 0:
            raise Exception(">>> Lo sentimos, el aumento debe ser mayor a 0.")
        employee = registro_empleados[id_employee]
        employee["salario"] = employee["salario"] + aumento
        print(f">>> Se actualizo correctamente el salario de {employee["nombre_completo"]}.")
        print(f">>> Salario actualizado: {employee["salario"]}")
    except ValueError:
        print(">>> El valor ingresado es erroneo, debe ingresar un valor numerico.")
    except Exception as error:
        print(error)