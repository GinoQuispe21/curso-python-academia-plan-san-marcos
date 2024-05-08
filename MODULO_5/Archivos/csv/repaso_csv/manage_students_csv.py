import csv

class Student:

    def __init__(self, name, age, profession, email, test_1_score, test_2_score) -> None:
        self.name = name
        self.age = age
        self.profession = profession
        self.email = email
        self.test_1_score = test_1_score
        self.test_2_score = test_2_score

list_students = []

with open("Archivos/csv/students.csv", encoding = "UTF8") as stream_csv_reader:
    dict_students = csv.DictReader(stream_csv_reader, delimiter=";")
    for line in dict_students:
        list_students.append(
            Student(
                name = line["Alumno"],
                age = int(line["Edad"]),
                profession = line["Profesion"],
                email = line["Correo"],
                test_1_score = float(line["Nota1"]),
                test_2_score = float(line["Nota2"])
            )
        )

suma_edad = 0
suma_nota_1 = 0
suma_nota_2 = 0

for student in list_students:
    suma_edad = suma_edad + student.age 
    suma_nota_1 += student.test_1_score
    suma_nota_2 += student.test_2_score
    print(f"{student.name} - {student.profession} - {student.test_1_score}")

numero_decimal = 10.124124

print(f"El promedio de edades es: {suma_edad/len(list_students)}")
print(f"El promedio de la nota 1 es: {(suma_nota_1/len(list_students)):.2f}")
print(f"El promedio de la nota 2 es: {(suma_nota_2/len(list_students)):.2f}")
