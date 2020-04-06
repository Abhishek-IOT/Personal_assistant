import datetime
from datetime import date

from src.Personal_Assistant.Speaking import Speaking


class Date(Speaking):
    def __int__(self):
        pass

    def tellDay(self):
        day = datetime.datetime.today().weekday() + 1
        Day_dict = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
        if day in Day_dict.keys():
            day_of_the_week = Day_dict[day]
            print(day_of_the_week)
            Speaking.speak(self, "The day is " + day_of_the_week)

    def telldate(self):
        day = str(date.today())
        print(day)
        todaydate = day[8:10]
        this_Month = day[5:7]
        # print(todaydate + "")
        # print(this_Month)
        this_year = day[0:4]
        # print(this_year)

        if todaydate == '01':
            dateno = "First"
        elif todaydate == '21':
            dateno = "Twenty First"
        elif todaydate == '31':
            dateno = "Thirty First"
        elif todaydate == '02':
            dateno = "Second"
        elif todaydate == '03':
            dateno = "Third"
        elif this_Month == '01':
            month = "January"
        elif this_Month == '02':
            month = "February"
        if this_Month == '03':
            month = "March"
        if this_Month == '04':
            month = "April"
        if this_Month == '05':
            month = 'May'
        if this_Month == '06':
            month = 'June'
        if this_Month == '07':
            month = 'July'
        if this_Month == '08':
            month = 'August'
        if this_Month == '09':
            month = 'September'
        if this_Month == '10':
            month = 'October'
        if this_Month == '11':
            month = 'November'
        if this_Month == '12':
            month = 'December'
        elif todaydate == '03':
            dateno = "Third"
        if todaydate == '01' or todaydate == '02' or todaydate == '03' or todaydate == '31' or todaydate == '21':
            Speaking.speak(self, dateno + month + this_year)
        else:
            Speaking.speak(self, todaydate + month + this_year)
