import tkinter as tk

window = tk.Tk() # Creamos una ventana/window usando la clase Tk() del modulo tkinter

icon = tk.PhotoImage(file = "D:\curso-python-academia-plan-san-marcos\MODULO_5\Tkinter-widgets\icon.png")
icon = tk.PhotoImage(file = "MODULO_5/Tkinter-widgets/assets/icon.png")

window.geometry("700x500") # ancho x alto | width x height -> setea los valores de longitud y ancho de mi ventana
window.resizable(width=True, height=True) # Permite que se reajuste el tamanio de la ventan
window.minsize(width=500, height=300)  # Colocar el limite minimo de las dimensiones de la venta
window.maxsize(width=900, height=700) # Colocar el limite maximo de las dimensiones de la venta
window.title("Mi primera ventana en TKinter :D") # Colocar el nombre de la ventana
window.iconphoto(True, icon) # Para cambiar la foto del icono de la ventana
window.config(background = "#dbf720") # el background/ fondo -> permite colocar el color de manera textual: "green" o poniendo el codigo hexadecimal

window.mainloop() # Importante: para que nuestro programa lance la window debemos ejecutar este metodo del window