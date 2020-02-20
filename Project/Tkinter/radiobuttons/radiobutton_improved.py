import tkinter as tk

root = tk.Tk()

v = tk.IntVar()
v.set(0)  # initializing the choice nie value tylko pozycję w kolejności od góry

languages = [
    ("Python", 0),
    ("Perl", 1),
    ("Java", 2),
    ("C++", 3),
    ("C", 4)
]

def ShowChoice():
    print(v.get())

tk.Label(root,
         text="""Choose your favourite 
programming language:""",
         justify = tk.LEFT,
         bg = "gray",
         padx = 20).pack()

for val, language in enumerate(languages):
    #jako typowe radio
    """tk.Radiobutton(root,
                  text=language,
                  padx = 20,
                  variable=v,
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)"""
    #jako blok tekstowy
    tk.Radiobutton(root,
                   text = language,
                   indicatoron = 0,
                   width = 20,
                   variable = v,
                   bg = "light blue",
                   command = ShowChoice(),
                   value = val).pack(anchor = tk.W)


root.mainloop()