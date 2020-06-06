import time
import tkinter as tk


class Stopwatch:
    def displaytime(self):
        current_time = time.strftime('%H:%M:%S')
        print(current_time)

    def Digital_clock(self):
        root = tk.Tk()
        root.title("Take rest")
        label = tk.Label(root, font='ariel 80', bg='white', fg="red")
        root.mainloop()
