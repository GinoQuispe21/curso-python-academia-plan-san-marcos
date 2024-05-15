import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

def openFileDialog():
    path = filedialog.askopenfile(
        initialdir = "C:\\Users\\gino_\\Music",
        defaultextension = ".txt",
        filetypes = (
            ("Arhcivos de texto", ".txt"),
            ("Archivos csv", ".csv"),
            ('Archivos html', ".html"),
            ('Archivos json', ".json")
        )
    )
    if path == None: return
    with open(path.name, "r") as stream:
        rows = stream.readlines()
        label.config(text= rows[0])
        label.pack()
    

button = tk.Button(
    master = window,
    text = "Abrir archivo",
    font = ("Arial", 20),
    fg = "white",
    bg = "red",
    activebackground = "black",
    activeforeground = "red",
    command = openFileDialog
)
button.pack()

label = tk.Label(
    master = window,
    text = "",
    fg = "blue"
)

window.mainloop()