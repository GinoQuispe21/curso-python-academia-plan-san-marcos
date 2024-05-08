from datetime import date, datetime

date_1 = date.today()
date_2 = date(2001, 4, 21)

diference = date_1 - date_2
print(diference, type(diference))

datetime_1 = datetime.today()
datetime_2 = datetime(2010, 5, 2, 23, 15, 30)
print(f"Resultado: {datetime_1 - datetime_2}")

# Creadno de manera manual datetime

from datetime import timedelta

delta = timedelta(weeks = 2, days = 3, hours = 23, minutes = 30)
print(delta, type(delta))
print(delta.days)
print(delta.seconds)
print(delta.microseconds)