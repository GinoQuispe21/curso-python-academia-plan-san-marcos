# Colocar el tipo de dato para el parametro de una funcion solo servira de documentacion mas no sera una restriccion para el programa
def calcular_mensaje_calificacion(nota: int):
    if nota < 0  or nota > 20:
        raise Exception("La nota ingresada es erronea", nota)
    elif nota <= 5:
        return "Muy baja nota, a seguir estudiando!"
    elif nota <= 10:
        return "Baja nota, puedes hacerlo mejor!"
    elif nota <= 15:
        return "Nada mal, pero puedes mejorar!"
    else:
        return "Buen trabajo!"

try:
    mensaje_Gino = calcular_mensaje_calificacion(-1)
except Exception as error:
    print(f"Nota: {error.args[1]}. {error.args[0]}")
else:
    print(mensaje_Gino)
finally:
    mensaje_Gino = ""
    print("Se termino el programa!")
