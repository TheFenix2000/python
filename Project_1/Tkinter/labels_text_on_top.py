#text on top of the image

import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="./image/logo.png")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily."""

#obrazek po prawej i tekst po lewej z padingiem 10
"""w = tk.Label(
    root,
    justify = tk.LEFT,
    padx = 10,
    compound = tk.LEFT, #umożliwia użycie tekstu i obrazka jednocześnie w CENTER
    text = explanation,
    image = logo).pack(side = "right")"""

#obrazek na środku i tekst również, tekst na obrazku
w = tk.Label(root,
             compound = tk.CENTER, #If the compound option is set to BOTTOM, LEFT, RIGHT, or TOP, the image is drawn correspondingly to the bottom, left, right or top of the text.
             text=explanation,
             image=logo).pack(side="right")
root.mainloop()
