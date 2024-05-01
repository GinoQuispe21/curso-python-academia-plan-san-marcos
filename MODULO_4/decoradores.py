def decorator(function):
    def function_modifier():
        print("Inicio de la modificacion")
        list_1 = function()
        print(list_1)
        print("Fin de la modificacion")
    return function_modifier

def create_list():
    return [i for i in range(10)]

def create_list_2():
    return [i for i in range(100)]

result = decorator(create_list)
result()

result_2 = decorator(create_list_2)
result_2()

@decorator
def set_name():
    return "Gino Quispe"

set_name()
