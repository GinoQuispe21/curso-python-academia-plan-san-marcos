import tkinter as tk

window = tk.Tk()

value = tk.BooleanVar()

def allowedTerms():
    print(value.get())
    if value.get() == True:
        label.config(text = "Si se acepto los terminos y condiciones")
    else:
        label.config(text = "No se acepto los terminos y condiciones")

checkbutton = tk.Checkbutton(
    master = window,
    text = "Acepto terminos y condiciones de tratamiento de mis datos",
    font = ("IMPACT", 20),
    fg = "black",
    bg = "lightgreen",
    variable = value,
    onvalue = True,
    offvalue = False,
    command = allowedTerms
).pack()

label = tk.Label(
    master = window,
    text = "",
    font = ("arial", 20, 'bold'),
    fg = "blue",
)
label.pack(pady = 20)

window.mainloop()