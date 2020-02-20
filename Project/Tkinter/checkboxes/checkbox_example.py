import tkinter as tk

root = tk.Tk()
var1 = tk.IntVar()
tk.Label(
    root,
    bg = "gray",
    text = """Do you like donuts?""").grid(row = 0, sticky = tk.W)
tk.Checkbutton(
    root,
    text = "Not so much",
    variable = var1).grid(row = 1, sticky = tk.W)
var2 = tk.IntVar()
tk.Checkbutton(
    root,
    text = "I do",
    variable = var2).grid(row = 2, sticky = tk.W)

root.mainloop()