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

    def No_of_odd_days_in_year(self, UserYear):
        year2 = UserYear[2:4]
        year1 = UserYear[0:2] + '00'
        # year2=year[3:5]
        print("Year1=", year1)
        print("Year2=", year2)
        deduced_year = int(year1)
        while (True):
            deduced_year = deduced_year - 400
            #  print(deduced_year)
            if deduced_year == 100:
                no_of_odd_days_inyear = 5
                break
            if deduced_year == 200:
                no_of_odd_days_inyear = 3
                break
            if deduced_year == 300:
                no_of_odd_days_inyear = 1
                break
            if deduced_year == 400:
                no_of_odd_days_inyear = 0
                break
            if deduced_year != 400 or deduced_year != 300 or deduced_year != 200 or deduced_year != 100:
                continue
        if UserYear == '2000':
            no_of_odd_days_inyear = no_of_odd_days_inyear + 1
        yearspassed = int(year2) - 1
        if year2 == '00':
            yearspassed = int(UserYear) - 1
            print("the yearspass22222===", yearspassed)
            print(type(yearspassed))
            yearspassed2 = str(yearspassed)
            yearspassed2 = yearspassed2[2:4]
            print("Yearsassdskjshdsajsadsdajasdkjasdkljasdkjsd", yearspassed2)
            divisor = int(yearspassed2) // 4
            print(divisor, "divisor")
            divisor2 = divisor * 2
            print(divisor2, "tota;divisor")
            reminder = int(yearspassed2) - divisor
            print(reminder)
        else:
            print(yearspassed)
            divisor = yearspassed // 4
            divisor2 = divisor * 2
            print("The years passed", divisor)
            reminder = yearspassed - divisor
            print("the reminder years=", reminder)
        total_odd_days = (divisor2 + reminder) % 7
        print("The total no of odd days =", total_odd_days)
        return no_of_odd_days_inyear + total_odd_days

    def No_of_Odd_Days_inMonths(self, month, year, date):
        days = int(date)
        if month == 'january':
            no_of_odd_days_inmonths = days
        if month == 'february':
            no_of_odd_days_inmonths = days + 31
        if month == 'march':
            no_of_odd_days_inmonths = days + 59
        if month == 'april':
            no_of_odd_days_inmonths = days + 90
        if month == 'may':
            no_of_odd_days_inmonths = days + 120
        if month == 'june':
            no_of_odd_days_inmonths = days + 151
        if month == 'july':
            no_of_odd_days_inmonths = days + 181
        if month == 'august':
            no_of_odd_days_inmonths = days + 212
        if month == 'september':
            no_of_odd_days_inmonths = days + 242
        if month == 'october':
            no_of_odd_days_inmonths = days + 273
        if month == 'november':
            no_of_odd_days_inmonths = days + 303
        if month == 'december':
            no_of_odd_days_inmonths = days + 334
        if int(year) % 400 == 0 or int(year) % 4 == 0:
            if month != 'january' and month != 'february':
                print(type(month))
                print("Yes it is not Jan , Feb")
                no_of_odd_days_inmonths = no_of_odd_days_inmonths + 1

            else:
                pass

        no_of_odd_days_inmonths = no_of_odd_days_inmonths % 7
        return no_of_odd_days_inmonths
