import empleados_modulo as mod_emp

def app():
    fin_programa = False
    end_register_employee = False
    show_menu = False
    while not fin_programa:
        if not end_register_employee:
            print("Creando un nuevo usuario:")
            id_number = mod_emp.input_id()
            full_name = mod_emp.input_full_name()
            dni = mod_emp.input_dni()
            phone = mod_emp.input_phone()
            time_month = mod_emp.input_months()
            position = mod_emp.input_position()
            mod_emp.register_employee(id_number, full_name, dni, phone, time_month, position)
            end_register_employee = mod_emp.input_continue_register()
        else:
            if not show_menu:
                show_menu = True
                mod_emp.menu()
            option = mod_emp.input_menu_option()
            if option == 1:
                mod_emp.visualizar_informacion_empleado()
            elif option == 2:
                mod_emp.mostrar_empleado_minimo_tiempo_1()
            elif option == 3:
                mod_emp.actualiar_salario_empleado()
            else:
                fin_programa = True

app()