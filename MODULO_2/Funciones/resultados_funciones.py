# Retornar valor -> palabra reservada return

def multiplicacion(a, b):
    return a * b

resultado = multiplicacion(10, 20)
print(resultado, type(resultado))

def conteo(feliz):
    print("Tres")
    print("Dos")
    print("Uno")
    if feliz == False: return
    print("Feliz Cumpleanios")

conteo(False)


# None: No tener valor
def numero_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return  
    
resultado = numero_par(111)
print(resultado)