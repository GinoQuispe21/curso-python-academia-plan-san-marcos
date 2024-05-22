import tkinter as tk
from service_db import ServiceDB
from config import *

window = tk.Tk()
window.geometry("700x600")
window.resizable(width=False, height=False)
window.config(bg = "lightgreen")

service = ServiceDB(path = path_db, mock = True)

frame = tk.Frame(
    master = window,
    background = "lightblue",
    border = 5,
    relief = "raised"
)
frame.pack(expand = True, fill = "x", padx = 50)

frame.columnconfigure(index = 0, weight = 1)
frame.columnconfigure(index = 1, weight = 1)

# variables de control para mis entrys

email_variable = tk.StringVar()
password_variable = tk.StringVar()

label_title = tk.Label(
    master = frame,
    text = "Iniciar de Sesion",
    font = title_font,
    fg = "black",
    bg = "lightblue",
).grid(row = 0, column = 0, columnspan = 2)

label_email = tk.Label(
    master = frame,
    text = "Correo:",
    font = label_font,
    bg = "lightblue"
).grid(row = 1, column = 0, sticky = "e", pady = 10)

entry_email = tk.Entry(
    master = frame,
    font = label_font,
    bg = "lightgray",
    fg = "blue",
    textvariable = email_variable
).grid(row = 1, column = 1, sticky = "w", padx = 10, pady = 10)


label_password = tk.Label(
    master = frame,
    text = "Contrasena:",
    font = label_font,
    bg = "lightblue"
).grid(row = 2, column = 0, sticky = "e", pady = 10)

entry_password = tk.Entry(
    master = frame,
    font = label_font,
    bg = "lightgray",
    fg = "blue",
    show = "*",
    textvariable = password_variable
).grid(row = 2, column = 1, sticky = "w", padx = 10, pady = 10)

submit_button = tk.Button(
    master = frame,
    text = "Iniciar Sesion",
    font = button_font,
    fg = "white",
    bg = "green",
    command = lambda: service.login(
        window = window,
        service = service,
        email = email_variable.get(),
        password = password_variable.get()
    )
).grid(row = 3, column = 0, columnspan = 2, pady = 15)

window.mainloop()