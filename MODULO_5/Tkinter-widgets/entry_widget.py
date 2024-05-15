import tkinter as tk

window = tk.Tk()

def submit_action():
    email = entry_email.get()
    password = entry_password.get()
    print(email)
    print(password)

def delete_action():
    entry_email.delete(0, "end")
    entry_password.delete(0, "end")

def delete_last_element():
    entry_email.delete(len(entry_email.get()) -1)

entry_email = tk.Entry(
    master = window,
    font = ("comic sans", 20, "bold"),
    fg = "green",
    bg = "gray"
)
entry_email.pack()
entry_email.insert(0, "gino_21@outlook.com")

entry_password = tk.Entry(
    master = window,
    font = ("comic sans", 20, "bold"),
    fg = "green",
    bg = "gray",
    show = "*"
)
entry_password.pack(pady = 10)

tk.Button(
    master = window,
    text = "submit",
    font = ("comic sans", 20, "bold"),
    fg = "white",
    bg = "green",
    padx = 10,
    pady = 5,
    command = submit_action
).pack()

tk.Button(
    master = window,
    text = "delete content",
    font = ("comic sans", 20, "bold"),
    fg = "white",
    bg = "red",
    padx = 10,
    pady = 5,
    command = delete_action
).pack()

button = tk.Button(
    master = window,
    text = "delete last",
    font = ("comic sans", 20, "bold"),
    fg = "white",
    bg = "yellow",
    padx = 10,
    pady = 5,
    command = delete_last_element
).pack()


window.mainloop()