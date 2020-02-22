import tkinter as tk

root = tk.Tk()
logo = tk.PhotoImage(file="logo.png")


def write_slogan():
    print("Tkinter is easy to use!")

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   command=quit,
                   image=logo)
button.pack(side=tk.LEFT)

root.mainloop()