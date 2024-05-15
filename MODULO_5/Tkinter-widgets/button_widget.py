import tkinter as tk

window = tk.Tk() 

contador = 0

def onTap():
    global contador
    contador += 1
    label.config(text = f"Contador: {contador}")

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

label = tk.Label(
    window,
    text = "Contador: 0",
    font = ("Arial", 20, "italic"),
    fg = "green"
)
label.pack()

window.mainloop()