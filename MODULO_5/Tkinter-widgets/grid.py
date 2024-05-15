import tkinter as tk

window = tk.Tk()

window.rowconfigure(index = 0, weight = 1)
window.rowconfigure(index = 1, weight = 1)
window.rowconfigure(index = 2, weight = 1)
window.rowconfigure(index = 3, weight = 1)


window.columnconfigure(index = 0, weight = 1)
window.columnconfigure(index = 1, weight = 1)
window.columnconfigure(index = 2, weight = 1)

frame_1 = tk.Frame(master= window, bg = "blue", width = 100, height = 50)
frame_2 = tk.Frame(master= window, bg = "gray", width = 100, height = 50)
frame_3 = tk.Frame(master= window, bg = "red", width = 100, height = 50)
frame_4 = tk.Frame(master= window, bg = "green", width = 100, height = 50)
frame_5 = tk.Frame(master= window, bg = "black", width = 200, height = 50)
frame_6 = tk.Frame(master= window, bg = "cyan", width = 100, height = 50)
frame_7 = tk.Frame(master= window, bg = "yellow", width = 100, height = 100)
frame_8 = tk.Frame(master= window, bg = "lightgreen", width = 100, height = 50)
frame_9 = tk.Frame(master= window, bg = "lightblue", width = 100, height = 50)
frame_10 = tk.Frame(master= window, bg = "pink", width = 100, height = 50)
frame_11 = tk.Frame(master= window, bg = "orange", width = 100, height = 50)
frame_12 = tk.Frame(master= window, bg = "lightgray", width = 100, height = 50)

frame_1.grid(row = 0, column = 0) 
frame_2.grid(row = 0, column = 1) 
frame_3.grid(row = 0, column = 2)
frame_4.grid(row = 1, column = 0) 
frame_5.grid(row = 1, column = 1, columnspan =2) 
frame_7.grid(row = 2, column = 0, rowspan = 2) 
frame_8.grid(row = 2, column = 1) 
frame_9.grid(row = 2, column = 2)
frame_11.grid(row = 3, column = 1) 
frame_12.grid(row = 3, column = 2) 

label = tk.Label(
    master = frame_5,
    text = "label 1",
    font = ("arial", 20),
    fg = "white",
    bg = "green"
)
label.grid(row = 0, column = 0) 

label = tk.Label(
    master = frame_5,
    text = "label 2",
    font = ("arial", 20),
    fg = "white",
    bg = "green"
)
label.grid(row = 0, column = 1) 

label = tk.Label(
    master = frame_5,
    text = "label 3",
    font = ("arial", 20),
    fg = "white",
    bg = "green"
)
label.grid(row = 0, column = 2) 

label = tk.Label(
    master = frame_5,
    text = "label 4",
    font = ("arial", 20),
    fg = "white",
    bg = "green"
)
label.grid(row = 1, column = 0, columnspan = 3) 

window.mainloop()