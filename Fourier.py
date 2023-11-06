import tkinter as tk

def pedir_numero_intervalos():
    num_intervalos = int(entrada_intervalos.get())
    ventana = tk.Toplevel(app)
    ventana.destroy()  # Cerrar la ventana principal de entrada de intervalos
    crear_ventana_intervalo(0, num_intervalos)

def crear_ventana_intervalo(i, num_intervalos):
    if i >= num_intervalos:
        # Se han ingresado todos los intervalos, puedes realizar la acción deseada aquí
        return
    
    ventana = tk.Toplevel(app)
    ventana.title(f"Intervalo {i + 1}")

    etiqueta_funcion = tk.Label(ventana, text=f"Función para Intervalo {i + 1}:")
    etiqueta_funcion.pack()

    entrada_funcion = tk.Entry(ventana)
    entrada_funcion.pack()

    etiqueta_rango = tk.Label(ventana, text=f"Rango para Intervalo {i + 1} (ejemplo: a b):")
    etiqueta_rango.pack()

    entrada_rango_desde = tk.Entry(ventana)
    entrada_rango_desde.pack()

    entrada_rango_hasta = tk.Entry(ventana)
    entrada_rango_hasta.pack()

    boton_siguiente = tk.Button(ventana, text="Siguiente", command=lambda i=i: guardar_datos(ventana, i, entrada_funcion.get(), entrada_rango_desde.get(), entrada_rango_hasta.get(), num_intervalos))
    boton_siguiente.pack()

    if i == num_intervalos - 1:
        calcular_serie_fourier()


def guardar_datos(ventana, i, funcion, rango_desde, rango_hasta, num_intervalos):
    # Aquí puedes procesar y guardar los datos ingresados en la ventana actual
    ventana.destroy()  # Cerrar la ventana actual
    crear_ventana_intervalo(i + 1, num_intervalos)  # Avanzar a la siguiente ventana

def calcular_serie_fourier():
    # Aquí puedes utilizar las listas 'funciones' y 'rangos' para realizar los cálculos de la serie de Fourier.
    ventana = tk.Toplevel(app)
    ventana.title(f"Resultado de la serie de Fourier")
    # resultado.set("Resultado de la serie de Fourier")
    etiqueta_rango = tk.Label(ventana, text=f"El resultado es: ")
    etiqueta_rango.pack()

# Crear la ventana principal
app = tk.Tk()
app.title("Pedir Intervalos")
app.geometry("400x300")
etiqueta_intervalos = tk.Label(app, text="Número de intervalos:")
etiqueta_intervalos.pack()

entrada_intervalos = tk.Entry(app)
entrada_intervalos.pack()

boton_iniciar = tk.Button(app, text="Iniciar", command=pedir_numero_intervalos)
boton_iniciar.pack()


app.mainloop()
