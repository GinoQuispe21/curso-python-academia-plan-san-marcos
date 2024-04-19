def fibonacci(number):
    if number <= 0:
        # Mensaje de error para valores negativos o 0
        print("La posicion debe ser mayor a 0")
        return 0
    elif number == 1:
        return 0
    elif number == 2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
    
print(fibonacci(8))