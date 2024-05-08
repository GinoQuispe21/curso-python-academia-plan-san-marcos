import csv
import random as rd

path_file_csv = "Archivos/csv/students.csv"
rows = []

with open(path_file_csv, mode = "r", encoding = "UTF-8") as stream_read_csv:
    obj_reader = csv.reader(stream_read_csv, delimiter = ";")
    for line in obj_reader:
        rows.append(line)

print("Agregando nueva columna")

rows[0].append("Nota3")
for index in range(1, len(rows)):
    rows[index].append(rd.randint(7, 20))

print(rows)

with open(path_file_csv, mode = "w", newline = "", encoding = "UTF-8") as stream_write_csv:
    obj_writer = csv.writer(stream_write_csv, delimiter = ";")
    obj_writer.writerows(rows)

print("Se actualizo el archivo csv")