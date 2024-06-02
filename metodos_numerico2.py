# Definimos la función f(x) = x^2 - 6.8x^{1.01} + 9
def f(x):
    return x**2 - 6.8*x**1.01 + 9

# Método de bisección
def bisection_method(x_izq, x_der, iteraciones):
    print("Método de Bisección:")
    for i in range(iteraciones):
        x_nuevo = (x_izq + x_der) / 2
        print(f"Iteración {i+1}: x_izq = {x_izq}, x_der = {x_der}, x_nuevo = {x_nuevo}")
        if f(x_nuevo) * f(x_izq) < 0:
            x_der = x_nuevo
        else:
            x_izq = x_nuevo

# Método de la secante
def secant_method(x_0, x_1, iteraciones):
    print("\nMétodo de la Secante:")
    for i in range(iteraciones):
        x_nuevo = x_1 - f(x_1) * (x_1 - x_0) / (f(x_1) - f(x_0))
        print(f"Iteración {i+1}: x_{i+2} = {x_nuevo}")
        x_0, x_1 = x_1, x_nuevo

# Parámetros iniciales para el ejercicio
x_izq = 1.5
x_der = 3
x_0 = 1.2
x_1 = 1.6
iteraciones = 5

# Ejecutar los métodos
bisection_method(x_izq, x_der, iteraciones)
secant_method(x_0, x_1, iteraciones)