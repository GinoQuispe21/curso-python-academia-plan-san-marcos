set_1 = {number + 10 if number > 15 else number - 10 for number in range(10, 21, 2)}
print(set_1, type(set_1))

employees  = {"natanael", "Rodrigo", "Alexander", "Piero", "Nathaly"}
set_employees_n = {nombre.capitalize() for nombre in employees if nombre[0].upper() == "N" }
print(set_employees_n)