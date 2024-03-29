import tkinter as tk

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (entry1.get(), entry2.get()))
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

master = tk.Tk()
tk.Label(master,
         text="First Name").grid(row=0)
tk.Label(master,
         text="Last Name").grid(row=1)

entry1 = tk.Entry(master)
entry2 = tk.Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

#entry1.insert(10, "John")   default values
#entry2.insert(10, "Miller") default values

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
tk.Button(master,
          text='Show', command=show_entry_fields).grid(row=3,
                                                       column=1,
                                                       sticky=tk.W,
                                                       pady=4)

tk.mainloop()