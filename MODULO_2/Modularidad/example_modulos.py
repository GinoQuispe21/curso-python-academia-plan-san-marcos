
"Maneras de llamar a un modulo"
# import modulo_1
# from modulo_1 import sumar, multiplicacion
# from modulo_1 import *
import modulo_1 as m

resultado = m.sumar(10, 90)
print(resultado)

resultado_2 = m.restar(3, 3)
print(resultado_2)

resultado_2 = m.multiplicacion(3, 3)
print(resultado_2)

print(m.correo)

# la carpeta __pycache__ se cra automaticamente cuando se haga el llamado de un modulo
# 