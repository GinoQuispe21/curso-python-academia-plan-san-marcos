from datetime import time

hour_random = time(18, 30, 45, 10100)
print(hour_random, type(hour_random))
print(f"Hora: {hour_random.hour}")
print(f"Minuto: {hour_random.minute}")
print(f"Segundo: {hour_random.second}")
print(f"Microsegundo: {hour_random.microsecond}")
print(f"TZinfo: {hour_random.tzinfo}")

import time as time_module

print("Empezando...")
# time_module.sleep(5) # Espera de 5 segundos en el programa
print("Continuando...")

today_timestamp = time_module.time()
print(today_timestamp)

print(f"Fecha actual: {time_module.ctime(today_timestamp)}")