import numpy as np

# Definimos la función f(x) = x^2 - 4.9x + 5.7cos(0.01x)
def f(x):
    return x**2 - 4.9 * x + 5.7 * np.cos(0.01 * x)

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
a = 1.6
b = 2.4
iterations = 5

# Obtención de raíces
roots = false_position_method(f, a, b, iterations)

# Impresión de resultados
print("Método de la Falsa Posición:")
for i, root in enumerate(roots, start=1):
    print(f"Iteración {i}: x = {root:.6f}")
