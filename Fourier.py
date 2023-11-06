import tkinter as tk
from numpy import pi
import scipy.integrate as spi


# Para ignorar los warnings


funciones = []
rangos = []

def pedir_numero_intervalos():
    funciones.clear()
    num_intervalos = int(entrada_intervalos.get())
    ventana = tk.Toplevel(app)
    ventana.destroy()  # Cerrar la ventana principal de entrada de intervalos
    crear_ventana_intervalo(0, num_intervalos)

def crear_ventana_intervalo(i, num_intervalos):
    if i >= num_intervalos:
        # Se han ingresado todos los intervalos, puedes realizar la acción deseada aquí
        calcular_serie_fourier()
        
        return

    font_base = ("Arial", 15)
    ventana = tk.Toplevel(app)
    ventana.geometry("370x200")    
    ventana.title(f"Intervalo {i + 1}")
    etiqueta_funcion = tk.Label(ventana, text=f"Función para Intervalo {i + 1}:", font=font_base)
    etiqueta_funcion.pack()

    entrada_funcion = tk.Entry(ventana, width=25, font=font_base)
    entrada_funcion.pack()
    
    etiqueta_rango = tk.Label(ventana, text=f"Rango para Intervalo {i + 1} (ejemplo: a b):", font=font_base)
    etiqueta_rango.pack()

    entrada_rango_desde = tk.Entry(ventana, width=25, font=font_base)
    entrada_rango_desde.pack()
    
    entrada_rango_hasta = tk.Entry(ventana, width=25, font=font_base)
    entrada_rango_hasta.pack()

    boton_siguiente = tk.Button(ventana, text="Siguiente", command=lambda i=i: guardar_datos(ventana, i, entrada_funcion.get(), entrada_rango_desde.get(), entrada_rango_hasta.get(), num_intervalos), font=font_base)
    boton_siguiente.pack()      


def guardar_datos(ventana, i, funcion, rango_desde, rango_hasta, num_intervalos):
    # Aquí puedes procesar y guardar los datos ingresados en la ventana actual
    get_entrada_function = funcion
    funciones.append(get_entrada_function)
    get_entrada_rango_desde = rango_desde
    rangos.append(get_entrada_rango_desde)
    get_entrada_rango_hasta = rango_hasta
    rangos.append(get_entrada_rango_hasta)
    ventana.destroy()  # Cerrar la ventana actual
    crear_ventana_intervalo(i + 1, num_intervalos)  # Avanzar a la siguiente ventana

def funcion_a_integrar(t):
    # for elemento in funciones:
    #     g += int(elemento)
    return t+2

def calcular_serie_fourier():
    # Aquí puedes utilizar las listas 'funciones' y 'rangos' para realizar los cálculos de la serie de Fourier.
    ventana = tk.Toplevel(app)
    ventana.geometry("370x200")
    ventana.title(f"Resultado de la serie de Fourier")
    
    # resultado.set("Resultado de la serie de Fourier")
    etiqueta_rango = tk.Text(ventana, height=10, width=25, font=font_base)
    etiqueta_rango.pack()
    
    # etiqueta_rango.delete(1.0, tk.END)
    for dato in funciones:
        etiqueta_rango.insert(tk.END, dato + '\n')  # Agregar cada elemento de la lista con un salto de línea

    for dato1 in rangos:
        etiqueta_rango.insert(tk.END, dato1 + '\n')  # Agregar cada elemento de la lista con un salto de línea

    

    dato_1 = int(rangos[-1])
    dato_2 = int(rangos[0]) 
    rango_f_ = (dato_1 - dato_2)
    rango_f = str(rango_f_)
    # etiqueta_rango.insert(tk.END, rango_f + '\n')

    
    
    resultado, error = spi.quad(funcion_a_integrar, -rango_f_, rango_f_)
    rs2 = (1 / (2 * rango_f_)) * resultado
    print("Resultado de la integral:", rs2)

# Diseño
app = tk.Tk()
app.title("Pedir Intervalos")
app.geometry("300x250")
app = tk.Frame(app)
app.pack(fill="both", expand=True)
app.place(relx=0.5, rely=0.5, anchor="center")
font_base = ("Arial", 15)

# Solicitar datos
etiqueta_intervalos = tk.Label(app, text="Número de intervalos:", font=font_base)
etiqueta_intervalos.pack()
entrada_intervalos = tk.Entry(app, width=25, font=font_base)
entrada_intervalos.pack()
boton_iniciar = tk.Button(app, text="Iniciar", command=pedir_numero_intervalos, font=font_base)
boton_iniciar.pack()



app.mainloop()
