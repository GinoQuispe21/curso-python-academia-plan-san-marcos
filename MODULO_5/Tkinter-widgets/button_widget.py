import tkinter as tk

window = tk.Tk() 

contador = 0

def onTap():
    global contador
    contador += 1
    print(f"Valor de contador {contador}")

button = tk.Button(
    master = window,
    text = "Dame click!",
    font = ("Arial", 20),
    fg = "white",
    bg = "red",
    activebackground = "black", # color del fondo cuando se de click al boton
    activeforeground = "red", # color del texto cuando se de click al boton
    command = onTap
)
button.pack()

window.mainloop()