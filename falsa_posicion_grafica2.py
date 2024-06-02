import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x) = x^2 - 6.8x^1.01 + 9
def f(x):
    return x**2 - 6.8 * x**1.01 + 9

# Aproximaciones de las raíces obtenidas en el ejercicio
roots = [2.039682, 2.043900, 2.044028, 2.044032, 2.044032]

# Gráfico de la función y las aproximaciones de las raíces
x_values = np.linspace(1, 3, 400)
y_values = f(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='f(x)', color='blue')

# Dibujar líneas verticales en las aproximaciones de las raíces
for root in roots:
    plt.axvline(x=root, color='red', linestyle='--', linewidth=1.5)

# Agregar puntos en las raíces aproximadas
plt.scatter(roots, [f(root) for root in roots], color='red', label='Raíces Falsa Posición')

# Añadir título y etiquetas
plt.title('Gráfico de f(x) = x^2 - 6.8x^1.01 + 9 con aproximaciones de las raíces')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)

# Añadir leyenda
plt.legend()

# Mostrar la gráfica
plt.show()
