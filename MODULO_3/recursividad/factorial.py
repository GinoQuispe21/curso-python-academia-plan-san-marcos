def factorial_recursivo(number):
    if number == 0:
        return 1
    else:
        return number * factorial_recursivo(number - 1)

def factorial_bucle_for(number):
    factorial = 1
    for i in range(1, number + 1):
        factorial = factorial * i
    return factorial

factorial_5_recursivo = factorial_recursivo(5)
print(factorial_5_recursivo)

factorial_5_bucle = factorial_bucle_for(5)
print(factorial_5_bucle)