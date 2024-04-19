def print_count_down(number):
    if number > 0:
        print(number)
        print_count_down(number - 1)
    print(f"Termino la funcion print_count_down({number})")

print_count_down(5)