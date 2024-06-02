import numpy as np

# Definimos la función f(x) = x^2 - 6.8x^1.01 + 9
def f(x):
    return x**2 - 6.8 * x**1.01 + 9

# Método de la Falsa Posición
def false_position_method(f, a, b, iterations):
    roots = []
    for _ in range(iterations):
        fa = f(a)
        fb = f(b)
        x_new = a - fa * (b - a) / (fb - fa)
        roots.append(x_new)
        fx_new = f(x_new)
        if fa * fx_new < 0:
            b = x_new
        else:
            a = x_new
    return roots

# Parámetros
a = 1.5
b = 3
iterations = 5

# Obtención de raíces
roots = false_position_method(f, a, b, iterations)

# Impresión de resultados
print("Método de la Falsa Posición:")
for i, root in enumerate(roots, start=1):
    print(f"Iteración {i}: x = {root:.6f}")
