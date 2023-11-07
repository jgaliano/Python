"""
Prueba de funcionamiento de la integral con quad y spi
"""
import tkinter as tk
import scipy.integrate as spi

# # Definir una función que deseas integrar
# def funcion_a_integrar(x):
#     return x+2

# # Calcular la integral definida de la función de 0 a 1
# resultado, error = spi.quad(funcion_a_integrar, -4, 4)
# rs2 = (1 / (2 * 4)) * resultado

# print("Resultado de la integral:", rs2)

"""
Prueba de funcionamiento de integral cuando la sumatoria de la lista de la función tiene letras
"""
# f_total = 0
# lista = ["y+1", 0, 1]
# position_none = None

# for i, dato in enumerate(lista):
#     if not isinstance(dato, int):
#         position_none = i
#         break

# if position_none is not None:
#     d_position = lista[i]
#     print(d_position)
# else:
#     # Sumatoria de los valores de la lista
#     for f_dato in lista:
#         f_total+= f_dato
#     print(f_total)
"""
Prueba 2: Cuando hay números dentro de la cadena str
"""
# def yes_numero(lista):
#     for i, dato in enumerate(lista):
#         if not str(dato).isdigit():
#             return i
#     return -1
# f_total = 0
# datos_lista = ["2", "1", "0"]
# posicion = yes_numero(datos_lista)

# if posicion == -1:
#     for f_dato in datos_lista:
#         f_total+= int(f_dato)
#     print(f_total)
# else:
#     d_position = datos_lista[posicion]
#     print(d_position)

"""

"""
# ICE_suma = 0  # Inicializa la variable de suma acumulativa
# rango_f_ = 10  # Reemplaza con el valor deseado

# # Supongamos que tienes listas de valores an y bn
# an = [1, 2, 3, 4, 5]
# bn = [6, 7, 8, 9, 10]

# # Itera a través de los valores de an y bn
# for i in range(len(an)):
#     ICE_suma += (rango_f_ / 2) * ((an ** 2) + (bn ** 2))

# print("Resultado de ICE_suma:", ICE_suma)

"""
"""
# import tkinter as tk
# from tkinter import ttk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# import numpy as np

# # Función que quieres graficar (en este caso, el seno)
# def funcion(x):
#     return np.sin(x)

# # Crear una ventana tkinter
# ventana = tk.Tk()
# ventana.title("Graficar Función")

# # Crear un lienzo de matplotlib dentro de la ventana de tkinter
# frame = ttk.Frame(ventana)
# frame.grid(row=0, column=0)

# # Crear una figura de matplotlib
# fig = Figure(figsize=(5, 4), dpi=100)
# ax = fig.add_subplot(111)

# # Generar valores para x y y
# x = np.linspace(0, 2 * np.pi, 100)  # Valores de x desde 0 hasta 2π
# y = funcion(x)

# # Graficar la función
# ax.plot(x, y)

# # Crear un lienzo para mostrar la figura en tkinter
# canvas = FigureCanvasTkAgg(fig, master=frame)
# canvas_widget = canvas.get_tk_widget()
# canvas_widget.grid(row=0, column=0)

# # Iniciar el bucle principal de tkinter
# ventana.mainloop()
"""
"""
import matplotlib.pyplot as plt
import numpy as np


def fourier_suma_parcial(f, L, N):
    def suma_parcial(t):
        suma = 0
        for n in range(N + 1):
            an = (1 / L) * spi.quad(lambda t: f(t) * np.cos(2 * np.pi * n * t / (2 * L)), -L, L)[0]
            bn = (1 / L) * spi.quad(lambda t: f(t) * np.sin(2 * np.pi * n * t / (2 * L)), -L, L)[0]
            if n == 0:
                suma += an / 2
            else:
                suma += an * np.cos(2 * np.pi * n * t / (2 * L)) + bn * np.sin(2 * np.pi * n * t / (2 * L))
        return suma
    return suma_parcial

def sierra(t):
    if -1 <= t < 1:
        return t
    else:
        return 0

L = 1
N = 10

suma_parcial = fourier_suma_parcial(sierra, L, N)

# Valores de t en el intervalo [-1, 1]
t = np.arange(-1, 1, 0.01)
# Valores de la función original
#f_t = [sawtooth_wave(ti) for ti in t]
# Valores de la suma parcial
suma_t = [suma_parcial(ti) for ti in t]


              
# Graficar la función original y la suma parcial
plt.figure(figsize=(10, 4))
#plt.plot(t, f_t, lw=2, label='Función Original')
plt.plot(t, suma_t, lw=4, color="red", label=f'Suma Parcial (N={N})')
plt.title('Función Suma Parcial de Fourier')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.grid(True)
plt.show()