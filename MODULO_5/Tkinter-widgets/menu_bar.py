import tkinter as tk

window = tk.Tk()

menu_bar = tk.Menu(master = window)

menu_bar.add_command(label = "File", command = lambda:print("Opcion file"))
menu_bar.add_command(label = "Save", command = lambda:print("Opcion save"))

options_tab = tk.Menu(
    master = menu_bar,
    font = ("My boli", 20),
    tearoff = 0
)
menu_bar.add_cascade(label = "More options", menu = options_tab)

options_tab.add_command(label = "Exportar arhcivo", command = lambda:print("Exportar archivo"))
options_tab.add_command(label = "Importar arhcivo", command = lambda:print("Importar archivo"))
options_tab.add_separator()
options_tab.add_command(label = "Eliminar arhcivo", command = lambda:print("Eliminar archivo"))

window.config(menu = menu_bar)

window.mainloop()