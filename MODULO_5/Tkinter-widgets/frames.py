import tkinter as tk

window = tk.Tk()

frame = tk.Frame(master = window, bg = "pink")
frame.pack(side = "right")

frame_2 = tk.Frame(master = window, bg = "red")
frame_2.pack(side = "left")

tk.Button(master = frame, text = "W", fg = "white", bg = "green", width = 5, height = 2).pack(side = "top")
tk.Button(master = frame, text = "A", fg = "white", bg = "green", width = 5, height = 2).pack(side = "left")
tk.Button(master = frame, text = "S", fg = "white", bg = "green", width = 5, height = 2).pack(side = "left")
tk.Button(master = frame, text = "D", fg = "white", bg = "green", width = 5, height = 2).pack(side = "left")

tk.Entry(master = frame_2, font = ("impact", 20), fg = "pink", bg = "green").pack(side = "bottom")
tk.Entry(master = frame_2, font = ("impact", 20), fg = "white", bg = "black").pack(side = "top")

window.mainloop()