import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x) = x^2 - 6.8x^1.01 + 9
def f(x):
    return x**2 - 6.8 * x**1.01 + 9

# Método de Bisección
def bisection_method(f, x_left, x_right, iterations):
    bisection_roots = []
    for _ in range(iterations):
        x_mid = (x_left + x_right) / 2
        bisection_roots.append(x_mid)
        if f(x_left) * f(x_mid) < 0:
            x_right = x_mid
        else:
            x_left = x_mid
    return bisection_roots

# Método de la Secante
def secant_method(f, x0, x1, iterations):
    secant_roots = [x0, x1]
    for _ in range(2, iterations + 1):
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        secant_roots.append(x2)
        x0, x1 = x1, x2
    return secant_roots[2:]

# Parámetros
x_left = 1.5
x_right = 3
iterations = 5

x0 = 1.2
x1 = 1.6

# Obtención de raíces
bisection_roots = bisection_method(f, x_left, x_right, iterations)
secant_roots = secant_method(f, x0, x1, iterations)

# Gráfico de la función y las aproximaciones de las raíces
x_values = np.linspace(1, 3, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)', color='blue')

# Dibujar líneas verticales en las aproximaciones de las raíces de bisección
for root in bisection_roots:
    plt.axvline(x=root, color='red', linestyle='--', linewidth=1.5)

# Dibujar líneas verticales en las aproximaciones de las raíces de la secante
for root in secant_roots:
    plt.axvline(x=root, color='green', linestyle='-.')

# Agregar puntos en las raíces aproximadas
plt.scatter(bisection_roots, [f(root) for root in bisection_roots], color='red', label='Bisección')
plt.scatter(secant_roots, [f(root) for root in secant_roots], color='green', label='Secante')

# Añadir título y etiquetas
plt.title('Gráfico de la función f(x) con aproximaciones de las raíces')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
