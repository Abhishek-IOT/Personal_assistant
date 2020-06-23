from tkinter import *


class Stopwatch:
    global count
    count = 0

    def reset(self):
        global count
        count = 1
        self.var.set('00:00:00')

    def start(self):
        global count
        count = 0
        self.start_time()

    def start_time(self):
        global count
        self.timer()

    def stop(self):
        global count
        count = 1

    def timer(self):
        global count
        if (count == 0):
            self.data = str(self.var.get())
            hour, minute, second = map(int, self.data.split(":"))

            if (second < 59):
                second = second + 1
            elif (second == 59):
                second = 0
                if (minute < 59):
                    minute = minute + 1
                elif (minute == 59):
                    hour = hour + 1
            if hour < 10:
                hour = "0" + str(hour)
            else:
                hour = str(hour)
            if minute < 10:
                minute = "0" + str(minute)
            if second < 10:
                second = "0" + str(second)
            self.data = str(hour) + ":" + str(minute) + ":" + str(second)
            self.var.set(self.data)
            if (count == 0):
                self.root.after(1000, self.start_time)

    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x200")
        self.var = StringVar()
        self.var.set("00:00:00")
        self.lab = Label(self.root, textvariable=self.var, font=("Courier 40 bold"))
        self.but1 = Button(self.root, text="Start", command=self.start, font=("Courier 12 bold"))
        self.but2 = Button(self.root, text="Stop", command=self.stop, font=("Courier 12 bold"))
        self.but3 = Button(self.root, text="Reset", command=self.reset, font=("Courier 12 bold"))
        self.lab.place(x=120, y=10)
        self.but1.place(x=100, y=100)
        self.but2.place(x=255, y=100)
        self.but3.place(x=370, y=100)
        self.root.mainloop()
