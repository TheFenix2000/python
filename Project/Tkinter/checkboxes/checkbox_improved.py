from tkinter import *
master = Tk()

def var_states():
   print("male: %d,\nfemale: %d" % (var1.get(), var2.get()))

Label(master,bg = "dark gray", text="Your sex:", width = 10).grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="male", variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text="female", variable=var2).grid(row=2, sticky=W)
Button(master, text='Quit', fg = "red", padx = 20, pady = 10, command=master.quit).grid(row=3, sticky=W, pady=10)
Button(master, text='Show', padx = 20, pady = 10, command=var_states).grid(row=4, sticky=W, pady=10)
mainloop()