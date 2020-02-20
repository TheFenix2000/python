import tkinter as tk

root = tk.Tk()

tk.Label(root, text = "First Name").grid(row = 0)
tk.Label(root, text = "Last Nme").grid(row = 1)

entry1 = tk.Entry(root).grid(row = 0, column = 1)

entry2 = tk.Entry(root).grid(row = 1, column = 1)



root.mainloop()