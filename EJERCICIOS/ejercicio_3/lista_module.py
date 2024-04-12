import random

list_is_created = False
numbers_list = []

def menu():
    print("""
=======================================
Menu de control de listas en Python :D
1. Crear una lista
2. Ver los datos de mi lista
3. Agregar un elemento a la lista
4. Actualizar un elemento de mi lista
5. Eliminar elemento de mi lista
6. Ordenar mi lista ascendentemente
7. Ordenar mi lista descendentemente
8. Buscar un elemento de mi lista
9. Volver a ver el menu
10. Terminar programa
=======================================
""")
    
def create_module_menu():
    print("""
1 > Crear la lista de forma manual
2 > Crear la lista de manear aleatoria señalando el total de números de la lista 
""")
    
def add_module_menu():
    print("""
1 > Agregar un elemento al final de la lista
2 > Insertar un elemento en una posicion especifica
""")
    
def delete_module_menu():
        print("""
1 > Eliminar elemento pasando su valor
2 > Eliminar elemento pasando su indice
""")
    
def create_list_manually():
    print("Ingrese todos los numeros que desee agregar a la lista.\nSi desea terminar escriba fin o FIN.")
    conditional = True
    while conditional:
        try:
            text_input = input("Ingrese un número: ")
            if text_input.upper() == 'FIN':
                conditional = False
            else:
                number = float(text_input)
                numbers_list.append(number)
        except Exception:
            print("Entrada erronea, intente nuevamente!")

def create_random_list():
    conditional = True
    while conditional:
        try:
            lenght_list = int(input("Ingrese el número de elementos de la lista: "))
            min_ran = int(input("Ingrese el número menor que se puede generar: "))
            max_ran = int(input("Ingrese el número mayor que se puede ser generado: "))
            if lenght_list <= 0:
                raise Exception("Valor ingresado incorrecto!")
            else:
                conditional = False
                for _ in range(lenght_list):
                    number_random = random.randint(min_ran, max_ran)
                    numbers_list.append(number_random)
        except ValueError:
            print("Dato erroneo, ingrese el numero de la opcion porfavor.")
        except Exception as error:
            print(error)

def create_list():
    global list_is_created
    if list_is_created:
        print("Ya se creo la lista, no puede acceder a esta opción")
    else:
        conditional_input = True
        while conditional_input:
            try:
                create_module_menu()
                option_create_list = int(input("Ingrese la opción para crear la lista: "))
                if option_create_list < 1 or option_create_list > 2: 
                    raise Exception("Valor ingresado incorrecto!")
                else:
                    conditional_input = False
                    if option_create_list == 1:
                        create_list_manually()
                    else:
                        create_random_list()
                list_is_created = True
            except ValueError:
                print("Dato erroneo, ingrese el numero de la opcion porfavor.")
            except Exception as error:
                print(error)

def show_list():
    global list_is_created
    if list_is_created:
        for index, element in enumerate(numbers_list):
            print(f"Indice: {index} | Elemento: {element}")
        pass
    else:
        print("No hay elementos agregados para poder mostrarlos")

def add_element():
    try:
        add_module_menu()
        option = int(input("Ingrese una opción: "))
        if option < 1 or option > 2: 
            raise Exception("Entrada erronea, intente nuevamente!")
        elif option == 1:
            element = float(input("Ingrese el número a agregar: "))
            numbers_list.append(element)
        else:
            element = float(input("Ingrese el número a agregar: "))
            index = int(input("Indice donde agregar: "))
            numbers_list.insert(index, element)
        print("-> Se agrego correctamente el elemento de la lista!")
    except ValueError:
        print('Valor ingresado erroneo, ingrese un número correcto')
    except Exception as error:
        print(error)

def update_element():
    try:
        element = float(input("Ingrese el número a actualizar: "))
        indice = int(input("Ingrese el indice del elemento a modificar"))
        numbers_list[indice] = element
        print("-> Se actualizo correctamente la lista!")
    except IndexError:
        print("Indice fuera")
    except Exception:
        print("Entrada erronea, intente nuevamente!")

def delete_element():
    try:
        delete_module_menu()
        element = int(input("Ingrese el número de la opción: "))
        if element < 1 or element > 2:
            raise Exception('Valor ingresado erroneo, ingrese las opciones mostradas')
        elif element == 1:
            element = float(input("Ingrese el elemento a eliminar: "))
            numbers_list.remove(element)
        else: 
            indice = int(input("Ingrese el indice del elemento a eliminar: "))
            del numbers_list[indice]
        print("-> Se elimino correctamente el elemento de la lista!")
    except ValueError:
        print("Debe ingresar un número!")
    except IndexError:
        print("Indice fuera")
    except Exception as error:
        print(error)

def order_ascd():
    numbers_list.sort()

def order_desc():
    numbers_list.sort(reverse = True)

def search_element():
    # Mostrar un menu de 2 opciones como en el programa:
    # donde la opcion 1 sea buscar el indice de un elemento por su valor
    # y la segunda opcion sea buscar el valor de un elemento por su indice
    # Hacer control de errores: try y excpet
    # ADICIONAL: Si la lista tiene numeros repetidos, retornar todos sus indices
    option = 1
    element_searched = 1
    index_searched = 2
    if option == 1: # La busqueda de un indice por su valor
        if numbers_list.count(element_searched) > 1:
            list_indix = []
            for index, number in enumerate(numbers_list):
                if number == element_searched:
                    list_indix.append(index)
            print(f"Los indices donde se encuentra el valor son: {list_indix}")
        else:
            index = numbers_list.index(element_searched)
            print(f"El indice del elemento buscado es: {index}")
    else:
        value = numbers_list[index_searched]
        print(value)
