import datetime

from src.Personal_Assistant.Speaking import Speaking


class Date(Speaking):
    def __int__(self):
        pass

    def telltime(self):
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        sec = time[18:19]
        print(hour + min + sec)
        Speaking.speak(hour + "Hours" + min + "Minutes" + sec + "Seconds sir")
