import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x) = x^2 - 4.9x + 5.7cos(0.01x)
def f(x):
    return x**2 - 4.9*x + 5.7*np.cos(0.01*x)

# Rango de valores de x para graficar
x_values = np.linspace(1, 3, 400)
y_values = f(x_values)

# Configuración de la figura
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)', color='blue')

# Aproximaciones de las raíces
bisection_root = 1.975  # Raíz aproximada por el método de bisección
secant_root = 1.986     # Raíz aproximada por el método de la secante

# Dibujar líneas verticales en las aproximaciones de las raíces
plt.axvline(x=bisection_root, color='red', linestyle='--', linewidth=1.5, label='Bisección')
plt.axvline(x=secant_root, color='green', linestyle='-.', linewidth=1.5, label='Secante')

# Agregar puntos en las raíces aproximadas
plt.scatter([bisection_root], [f(bisection_root)], color='red')
plt.scatter([secant_root], [f(secant_root)], color='green')

# Añadir título y etiquetas
plt.title('Gráfico de la función f(x) con aproximaciones de las raíces')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()

