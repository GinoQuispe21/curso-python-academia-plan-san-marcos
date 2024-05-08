from datetime import date

today = date.today()
print(today, type(today))
print(f"Year: {today.year}")
print(f"Month: {today.month}")
print(f"Day: {today.day}")

birth_date = date(2001, 4, 21)
print(birth_date, type(birth_date))

# Marca de tiempo / timestamp
# Cantidad de segundos desde la Fecha Unix (01 de enero de 1970 hora UTC)

import time

timestamp = time.time()
print(timestamp)

current_date = date.fromtimestamp(timestamp)
print(f"Fecha actual calculada con la marca de tiempo: {current_date} | {type(current_date)}")

# ISO 8601

date_str_iso = "2014-04-30"
date_obj_iso = date.fromisoformat(date_str_iso)
print(date_obj_iso, type(date_obj_iso))

from datetime import datetime

datetime_str_iso = "2001-10-22T14:30:15"
datetime_obj = datetime.fromisoformat(datetime_str_iso)
print(datetime_obj, type(datetime_obj))
print(datetime_obj.date())
print(datetime_obj.time())

# Metodo replace

date_today_obj = date.fromtimestamp(timestamp)
print(date_today_obj)
new_date_today_obj = date_today_obj.replace(day = 30, year = 2012)
print(new_date_today_obj)

datetime_obj_1 = datetime.today()
print(datetime_obj_1)
new_datetime_obj_1 = datetime_obj_1.replace(hour=14)
print(new_datetime_obj_1)
print(new_datetime_obj_1.weekday())
print(new_datetime_obj_1.isoweekday())
