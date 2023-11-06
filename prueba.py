
import tkinter as tk
import scipy.integrate as spi

# Definir una función que deseas integrar
def funcion_a_integrar(x):
    return x+2

# Calcular la integral definida de la función de 0 a 1
resultado, error = spi.quad(funcion_a_integrar, -4, 4)
rs2 = (1 / (2 * 4)) * resultado

print("Resultado de la integral:", rs2)