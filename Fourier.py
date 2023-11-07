import tkinter as tk
from numpy import pi
import scipy.integrate as spi
import re

funciones = []
rangos = []

def pedir_numero_intervalos():
    funciones.clear()
    num_intervalos = int(entrada_intervalos.get())
    ventana = tk.Toplevel(app)
    ventana.destroy()  
    crear_ventana_intervalo(0, num_intervalos)

def crear_ventana_intervalo(i, num_intervalos):
    if i >= num_intervalos:
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
    get_entrada_function = funcion
    funciones.append(get_entrada_function)
    get_entrada_rango_desde = rango_desde
    rangos.append(get_entrada_rango_desde)
    get_entrada_rango_hasta = rango_hasta
    rangos.append(get_entrada_rango_hasta)
    ventana.destroy()  
    crear_ventana_intervalo(i + 1, num_intervalos)  

def yes_numero(lista):
    for i, dato in enumerate(lista):
        if not str(dato).isdigit():
            return i
    return -1

def funcion_a_integrar(x):
    y = 0
    datos_lista = funciones
    posicion = yes_numero(datos_lista)
    
    if posicion == -1:
        for f_dato in datos_lista:
            y+= int(f_dato)
        resultado = y
        # print(y)
    else:
        y = datos_lista[posicion]
        pattern = r'\d+'
        elemento_0 = y
        matches = re.findall(pattern, elemento_0)
        if matches: 
            numero = int(matches[0])
            resultado = x+numero
        # print(resultado)

    # print("hola")
    pr1 = x + resultado
    return resultado

def calcular_serie_fourier():
    ventana = tk.Toplevel(app)
    ventana.geometry("370x200")
    ventana.title(f"Resultado de la serie de Fourier")
    
    etiqueta_rango = tk.Text(ventana, height=10, width=25, font=font_base)
    etiqueta_rango.pack()
    
    for dato in funciones:
        etiqueta_rango.insert(tk.END, dato + '\n')  

    for dato1 in rangos:
        etiqueta_rango.insert(tk.END, dato1 + '\n')  


    dato_1 = int(rangos[-1])
    dato_2 = int(rangos[0]) 
    rango_f_ = (dato_1 - dato_2)
    rango_f = str(rango_f_)
    # etiqueta_rango.insert(tk.END, rango_f + '\n')

    resultado, error = spi.quad(funcion_a_integrar, -rango_f_, rango_f_)
    rs2 = (1 / (2 * rango_f_)) * resultado
    print("Resultado de la integral: ", rs2)

    resultado_integral, error = spi.quad(lambda x: funcion_a_integrar(x)**2, 0, 2)
    print("Resultado de la integral por partes: " + str(resultado_integral))

    resultado_n = resultado_integral*0.02
    print("Resultado N: " + str(resultado_n))


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
