def factorial(n):
    print(n)
    if n == 1:
        return 1
    
    return n* factorial(n - 1)

n = int(input("Choose a integer => "))
print(factorial(n))

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

aplicar_operaciones(-2)