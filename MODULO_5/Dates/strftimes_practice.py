from datetime import datetime, date

today = datetime.today()
today_strf = datetime.strftime(today, "%Y/%m/%d")
print(today_strf)

today_obj_date = date.today()
today_obj_date_strf = datetime.strftime(today_obj_date, "%Y/%m/%d")
print(today_obj_date_strf)

# Otro ejemplo:

from datetime import time

time_obj = time(21, 30, 45)
print(time_obj.strftime("%H:%M:%S"))

datetime_obj = datetime(2007, 12, 20)

print(datetime_obj.strftime("%Y %B %d %H:%M:%S"))

import time

today_time_stamp = time.time()
struct_time = time.gmtime(today_time_stamp)
print(f"Struct time: {struct_time} | {type(struct_time)}")

print(f"Timpo formateado: {time.strftime("%Y-%m-%d%T%H:%M:%S")}")

# strptime

datetime_obj_1 = datetime.strptime("2013/6/20T15:30:5", "%Y/%m/%dT%H:%M:%S")
print(datetime_obj_1)

import time as module_time

obj_time = module_time.strptime("2013/6/20T15:30:5", "%Y/%m/%dT%H:%M:%S")
print(obj_time)