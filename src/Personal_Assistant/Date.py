import datetime


class Date:
    def __int__(self):
        pass

    def telltime(self):
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        sec = time[18:19]
