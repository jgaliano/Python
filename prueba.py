"""
Prueba de funcionamiento de la integral con quad y spi
"""
# import tkinter as tk
# import scipy.integrate as spi

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
