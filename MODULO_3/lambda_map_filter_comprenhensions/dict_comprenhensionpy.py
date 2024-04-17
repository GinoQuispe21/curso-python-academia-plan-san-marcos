word = "aaaabbcccxa"

dict_palabras = {letra: word.count(letra) for letra in set(word)}
print(dict_palabras)

texto = "Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban trigo tres tristes tigres."
lista_palabras = texto.replace(",", "").replace(".", "").split()
dict_palabras_1 = {palabra: lista_palabras.count(palabra)  for palabra in set(lista_palabras)}
print(dict_palabras_1)

students = ["Rodrigo", "Rodlfo", "Jeriot", "Marce"]
nota = [13, 17, 17, 18]
object_zip = zip(students, nota)
print(object_zip, type(object_zip))

students_capps = {estudiante: nota for estudiante, nota in object_zip}
print(students_capps)