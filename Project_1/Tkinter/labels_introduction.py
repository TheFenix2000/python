import tkinter as tk

root = tk.Tk() #tworzenie okna, musi być zawsze pierwszy

w = tk.Label(root, text="Hollo World") #nasza rtykieta, (<name of the parent window, czyli nasz root>, keayword)
w.pack() #metoda skalowania okna do tekstu

root.mainloop()#wywołanie okna bez tego się nie pojawi