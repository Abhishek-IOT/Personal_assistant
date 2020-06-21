import time
import tkinter as tk


class Digital_clock:
    def __init__(self, window):
        self.window = window
        self.window.title('Digital clock')
        self.clock_Label = tk.Label(self.window, font='ariel 80', bg='blue', fg='white')
        self.clock_Label.grid(row=0, column=1)
        self.display_the_time()

    def display_the_time(self):
        self.current_time = time.strftime('%H:%M:%S')
        self.clock_Label['text'] = self.current_time
        self.window.after(200, self.display_the_time)
