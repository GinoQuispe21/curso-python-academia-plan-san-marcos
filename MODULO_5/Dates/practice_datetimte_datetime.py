from datetime import datetime, timezone

random_datetime = datetime(1978, 11, 8, 23, 22, 45, 102103, timezone.utc)
print(random_datetime, type(random_datetime))
print(f"Fecha: {random_datetime.date()}")
print(f"Tiempo: {random_datetime.time()}")

# Metodos de datetime

print(f"Datetime today: {datetime.today()}")
print(f"Datetime now: {datetime.now()}")
print(f"Datetime utcnow: {datetime.utcnow()}")
print(f"Datetime now no depreado: {datetime.now(timezone.utc)}")

# Marca de tiempo en clase datetime

obj_datetime_1 = datetime(2020, 3, 15, 23, 50, 12)
print(f"Marca de tiempo random: {obj_datetime_1.timestamp()}")