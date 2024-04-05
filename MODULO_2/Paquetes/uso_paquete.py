#import primer_paquete.modulo_matematica as mod_math
#import primer_paquete.modulo_mensajes as mod_str

# from primer_paquete.modulo_matematica import potencia, division # Importa solo las funciones seleccionadas
# from primer_paquete.modulo_matematica import * # Esto importa todas las funciones del modulo del paquete

import primer_paquete as paq
# import primer_paquete.subpaquete.modulo_usuario as mod_user

print(paq.potencia(2, 3))
print(paq.division(10,2))
paq.saludo()

print(paq.mostar_correo())