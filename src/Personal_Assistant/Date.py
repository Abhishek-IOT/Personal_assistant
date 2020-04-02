from datetime import date

from src.Personal_Assistant.Speaking import Speaking


class Date(Speaking):
    def __int__(self):
        pass

    def telldate(self):
        day = str(date.today())
        print(day)
        todaydate = day[8:10]
        this_Month = day[5:7]
        # print(todaydate + "")
        # print(this_Month)
        this_year = day[0:4]
        # print(this_year)

        if todaydate == '1':
            dateno = "First"
        if todaydate == '21':
            dateno = "Twenty First"
        if todaydate == '31':
            dateno = "Thirty First"
        elif todaydate == '2':
            dateno = "Second"
        elif todaydate == '3':
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
