import tkinter as tk

root = tk.Tk()
tk.Label(
    text = "Red Text in Times New Roman",
    fg = "red",
    font = "Times").pack()
tk.Label(
    text = "Blue Text in Halvetica font on Dark green background",
    fg = "blue", #forground color
    bg = "dark green", #background color
    font = "Halvetica 16 bold italic").pack()
tk.Label(
    text = "White Text in Verdana bold on black background",
    fg = "white",
    bg = "black",
    font = "Verdana 10 bold").pack()
root.mainloop()