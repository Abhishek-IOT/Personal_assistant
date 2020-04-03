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

    def set_Reminder(self, userhour, usermin, time_meridiem):
        time = str(datetime.datetime.now())
        print(time)
        hour = time[11:13]
        min = time[14:16]
        time_meridiemrealam = 'a.m'
        if time_meridiem == time_meridiemrealam:
            if userhour == hour and usermin == min:
                self.songs()

        elif time_meridiem == 'p.m':
            userhour = int(userhour) + 12
            userhour = str(userhour)
            if userhour == userhour and usermin == usermin:
                self.songs()
        print("the current hour" + hour)
        print("the current min" + min)

    def songs(self):
        Speaking.speak(self, "the reminder that u said is now sir")
        # music = 'D:\\Music'
        # songs = os.listdir(music)
        # os.startfile(os.path.join(music, songs[0]))
