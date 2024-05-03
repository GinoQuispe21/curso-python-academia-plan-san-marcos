import csv

with open("MODULO_5\Archivos\csv\students.csv") as stream_read:
    lector_read_dict = csv.DictReader(stream_read, delimiter = ';')
    for row in lector_read_dict:
        print(row['Profesion'], row['Nota1'])

with open("MODULO_5\Archivos\csv\comidas.csv", mode = 'w', newline='') as stream_write:
    column_names = ['Id', 'Nombre', 'Precio']
    obj_writer = csv.DictWriter(stream_write, fieldnames=column_names)
    obj_writer.writeheader()
    data = [
        {'Id': 10, 'Nombre': 'Lomo saltado', 'Precio': 30},
        {'Id': 10, 'Nombre': 'Lomo saltado', 'Precio': 30},
        {'Id': 10, 'Nombre': 'Lomo saltado', 'Precio': 30},
        {'Id': 10, 'Nombre': 'Lomo saltado', 'Precio': 30}
    ]
    for row in data:
        obj_writer.writerow(row)