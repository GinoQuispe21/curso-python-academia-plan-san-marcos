import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

def showMessageBox():
    messagebox.showinfo(
        title = "Importante!",
        message = "Este es el cuerpo del mensaje importante que debes saber para estar informado."
    )

def showWarningBox():
    messagebox.showwarning(
        title = "Advertencia!",
        message = "Este es el cuerpo de la advertencia que debes saber para estar informado."
    )

def showErrorBox():
    messagebox.showerror(
        title = "Error!",
        message = "Este es el cuerpo del error que debes saber para estar informado."
    )

def showQuestions(option):
    if option == 1:
        result = messagebox.askokcancel(
            title = "Pregunta de ok y cancelar",
            message = "Estas seguro que deseas eliminar este documento?"
        )
        if result:
            print("El usuario elimino el archivo")
        else:
            print("El usuario cancelo la accion de eliminar el archivo")
    elif option == 2:
        result = messagebox.askretrycancel(
            title = "Reintento de bloqueo",
            message = "Estas seguro de reintentar la accion?"
        )
        print(result)
    else:
        result = messagebox.askyesnocancel(
            title = "Ask yes no cancel",
            message = "Estas seguro de bloquear al usuario?"
        )
        print(result)
        if result == True: print("Se bloqueo al usuario")
        elif result == False: print("No se bloqueo al usuario")
        else: print("Se cancelo la accion de bloqueo")

tk.Button(
    master = window,
    text = "Open Message Box",
    font = ("comic sans", 20, "bold"),
    fg = "white",
    bg = "green",
    padx = 10,
    pady = 5,
    command = showMessageBox
).pack()

tk.Button(
    master = window,
    text = "Open Warning Box",
    font = ("comic sans", 20, "bold"),
    fg = "black",
    bg = "yellow",
    padx = 10,
    pady = 5,
    command = showWarningBox
).pack()

tk.Button(
    master = window,
    text = "Open Error Box",
    font = ("comic sans", 20, "bold"),
    fg = "black",
    bg = "red",
    padx = 10,
    pady = 5,
    command = showErrorBox
).pack()

tk.Button(
    master = window,
    text = "Open ask cancel",
    font = ("comic sans", 20, "bold"),
    fg = "black",
    bg = "cyan",
    padx = 10,
    pady = 5,
    command = lambda: showQuestions(1)
).pack()

tk.Button(
    master = window,
    text = "Open ask retry cancel",
    font = ("comic sans", 20, "bold"),
    fg = "white",
    bg = "orange",
    padx = 10,
    pady = 5,
    command = lambda: showQuestions(2)
).pack()

tk.Button(
    master = window,
    text = "Open ask yes no cancel",
    font = ("comic sans", 20, "bold"),
    fg = "white",
    bg = "purple",
    padx = 10,
    pady = 5,
    command = lambda: showQuestions(3)
).pack()

window.mainloop()