import lista_module as lm

def options_action(option):
    if option == 1:
        lm.create_list()
    elif option == 2:
        lm.show_list()
    elif option == 3:
        lm.add_element()
    elif option == 4:
        lm.update_element()
    elif option == 5:
        lm.delete_element()
    elif option == 6:
        lm.order_ascd()
    elif option == 7:
        lm.order_desc()
    elif option == 8:
        lm.search_element()
    else:
        lm.menu()

def app():
    finish_program = False
    lm.menu()
    while not finish_program:
        try:
            option = int(input(">>> Ingrese el número de la opción que desee realizar: "))
            if option < 1 or option > 10: 
                raise Exception("Opcion ingresada no valida")
            elif option != 10:
                options_action(option)
            else:
                finish_program = True
        except ValueError:
            print("Dato erroneo, ingrese el numero de la opcion porfavor.")
        except Exception as error:
            print(error)


app()