import tkinter as tk
from tkinter import filedialog

window = tk.Tk()

def saveFileDialog():
    path = filedialog.asksaveasfile(
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
    body_file = str(text.get(1.0, "end"))
    with open(path.name, mode = "w") as stream:
        stream.write(body_file)

text = tk.Text(
    master = window,
    fg = "blue",
    bg = "gray",
    font = ("comic sans", 20, "italic")
)
text.pack()

button = tk.Button(
    master = window,
    text = "Guardar archivo",
    font = ("Arial", 20),
    fg = "white",
    bg = "red",
    activebackground = "black",
    activeforeground = "red",
    command = saveFileDialog
)
button.pack()

window.mainloop()