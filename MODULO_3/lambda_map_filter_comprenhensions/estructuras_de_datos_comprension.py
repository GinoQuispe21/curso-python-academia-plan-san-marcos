lista_base = range(0, 20, 1)
nueva_lista = [element for element in lista_base]
print(nueva_lista)

nueva_lista_2 = [element ** 2 for element in lista_base]
print(nueva_lista_2)

nueva_lista_3 = [element for element in lista_base if element % 2 == 0]
print(nueva_lista_3)

lista_estudiantes = ['Jeriot', 'Alexander', 'Guillermo', 'Rodrigo', 'Rafael', 'Marce', 'Anthony']
estudiantes_a = [student.upper() for student in lista_estudiantes if student[0] == 'A']
print(estudiantes_a)

lista_numeros_1 = [10, 21, 30, 14, 12]
lista_numeros_2 = [12, 22, 30, 15, 29]
numeros_iguales = [number1 for number1 in lista_numeros_1 for number2 in lista_numeros_2 if number1 == number2]
print(numeros_iguales)