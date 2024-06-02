import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x) = x^2 - 4.9x + 5.7cos(0.01x)
def f(x):
    return x**2 - 4.9 * x + 5.7 * np.cos(0.01 * x)

# Aproximaciones de las raíces obtenidas en el ejercicio
roots = [1.677618, 1.679331, 1.679339, 1.679339, 1.679339]

# Gráfico de la función y las aproximaciones de las raíces
x_values = np.linspace(1, 3, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)', color='blue')

# Dibujar líneas verticales en las aproximaciones de las raíces
for root in roots:
    plt.axvline(x=root, color='red', linestyle='--', linewidth=1.5)

# Agregar puntos en las raíces aproximadas  hola mundo
plt.scatter(roots, [f(root) for root in roots], color='red', label='Raíces Falsa Posición')

# Añadir título y etiquetas
plt.title('Gráfico de f(x) = x^2 - 4.9x + 5.7cos(0.01x) con aproximaciones de las raíces')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
