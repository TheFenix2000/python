#tekst po lewej, a obrazek po prawej
import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="../image/logo.png")

w1 = tk.Label(root,image=logo).pack(side="right")

explenation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

w2 = tk.Label(
    root,
    justify=tk.LEFT,#LEFT/RIGHT/CENTER, wyrównanie tekstu w okienku
    padx = 10, #padding
    text=explenation).pack(side="left")
root.mainloop()