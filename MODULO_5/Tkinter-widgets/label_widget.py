import tkinter as tk

window = tk.Tk()

window.geometry("700x500")

photo = tk.PhotoImage(file = "MODULO_5/Tkinter-widgets/assets/icon.png").subsample(4)
label = tk.Label(
    master = window,
    text = "Mi primer label en tkinter",
    font = ("Impact", 25, "bold"),
    foreground = "green",
    background = "pink",
    relief = "solid",
    border = 5,
    padx = 30, # horisontal
    pady = 20,
    image = photo,
    compound = "right" # posicion donde muestra mi imagen en relacion a mi label
)
label.pack(side="top")
# label.grid(row = 0, column = 0)

label1 = tk.Label(
    master = window,
    text = "Mi segundo label en tkinter",
    font = ("Impact", 25, "bold"),
    foreground = "red",
    background = "black",
    relief = "solid",
    border = 5,
    padx = 30, # horisontal
    pady = 20,
    compound = "right" # posicion donde muestra mi imagen en relacion a mi label
)
label1.pack(side="right") # Pack coloca el widget y lo gestiona la ventana para su posicionamiento, por defecto es en la posicion top
# label1.grid(row = 0, column = 1) # grid es la forma alternativa mas usada para colocar nuestros widgets en la ventana

window.mainloop()