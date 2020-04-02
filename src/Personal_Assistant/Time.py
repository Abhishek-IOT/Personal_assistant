import datetime

from src.Personal_Assistant.Speaking import Speaking


class Time(Speaking):
    def __int__(self):
        pass

    def tellTime(self):
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        Speaking.speak(self, "The time is sir" + hour + "Hours and" + min + "Minutes")
