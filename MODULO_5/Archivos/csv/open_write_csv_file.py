import csv

with open("MODULO_5\Archivos\csv\my_tasks.csv") as stream_csv:
    full_csv = csv.reader(stream_csv, delimiter = "|")
    for line in full_csv:
        print(line)

courses_data = [
    ['Curso', 'Numero de Modulos', 'Numero de horas', 'Profesor'],
    ['Python', '7 modulos', '56', 'Gino Quispe Calixto'],
    ['Flutter', '6 modulos', '60', 'Jorge Pedro Ramirez'],
    ['C++', '7 modulos', '70', 'Rodrigo Mazzarri Sabrera']
]

with open("MODULO_5\Archivos\csv\courses.csv", mode = 'w', newline='') as stream_write_csv:
    obj_writer = csv.writer(stream_write_csv, delimiter = ';')
    for course in courses_data:
        obj_writer.writerow(course)