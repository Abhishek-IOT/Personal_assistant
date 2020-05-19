from tkinter import *
from tkinter import ttk

class GUI:
    root = Tk()
    root.geometry("500x30")
    root.title("Abhi")
    Label1 = ttk.Label(root, text="Query")
    Label1.grid(row=0, column=0)
    Entry1 = ttk.Entry(root, width=75)
    Entry1.grid(row=0, column=1)
    root.mainloop()
