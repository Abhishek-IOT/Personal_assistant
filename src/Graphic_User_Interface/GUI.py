from tkinter import *

from src.Personal_Assistant.Speaking import Speaking


class GUI:
    speak = Speaking()
    root = Tk()
    global var
    var = "Listening...."
    root.geometry("500x500")
    lab = Label(root, text=var, bg="#FAB60C")
    lab.config(font=("Courier", 20))
    var.set("User Said:")
    lab.pack()
    root.title("Year")
    button = Button(root, text="Press for Command", command=speak.takeCommand)
    button.pack()
    root.mainloop()
