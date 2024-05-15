import tkinter as tk

window = tk.Tk()

def onTapOption():
    print(f"Opcion seleccionada: {variable_manager.get() + 1}")

options = [
    "Opcion 1",
    "Opcion 2",
    "Opcion 3",
    "Opcion 4"
]

variable_manager = tk.IntVar()

for index in range(len(options)):
    radioButtons = tk.Radiobutton(
        master = window,
        text = options[index],
        font = ("Comic sans", 20, "bold"),
        background = "lightblue",
        variable = variable_manager,
        value = index,
        command = onTapOption,
        activeforeground = "white",
        activebackground = "blue",
        selectcolor = "green",
        indicatoron = 0
    )
    radioButtons.pack(pady = 10)

window.mainloop()