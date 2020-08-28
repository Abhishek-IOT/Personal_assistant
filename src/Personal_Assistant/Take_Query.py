import datetime
import webbrowser

import wikipedia

from src.Calculations.Number_to_Hindi import Number_to_Hindi
# from src.Making_Tuple_list_from_the_voice.Making_List import Making_list
from src.Personal_Assistant import Setting_control
from src.Personal_Assistant.Date import Date
from src.Personal_Assistant.Open import Open
from src.Personal_Assistant.Speaking import Speaking
from src.Personal_Assistant.Time import Time


class Take_Query(Time, Date):

    def query(self):
        speaking = Speaking()
        speaking.WishMe()
        speaking.Graphics()
        time = Time()
        date = Date()

        while (True):
            query = speaking.takeCommand().lower()
            self.all_the_queries(query)
            continue



    def query2(self, userhour, usermin, time_merdiem):
        speaking = Speaking()
        time = Time()
        date = Date()
        timereal = str(datetime.datetime.now())
        if time_merdiem == 'p.m':
            if userhour == '12':
                userhour = '12'
            else:
                userhour = int(userhour) + 12
            userhour = str(userhour)
        if time_merdiem == 'a.m':
            if userhour == '12':
                userhour = '00'
            else:
                pass

        hour = timereal[11:13]
        min = timereal[14:16]
        b = True
        while (b):

            timereal = str(datetime.datetime.now())
            hour = timereal[11:13]
            min = timereal[14:16]

            # print("The userhour"+userhour)
            print("The alarm min     " + userhour + "       " + usermin)
            print("The current min  " + hour + "       " + min)
            if (hour != userhour or min != usermin):
                query = speaking.takeCommand().lower()
                self.all_the_queries(query)
            else:
                print("this is alarm time sir")
                speaking.speak("Alarm time sir")
                b = False

    def set_Reminder(self):
        Speaking.speak(self, "at which hour you want to set the reminder sir")
        time = Time()
        query = Speaking.takeCommand(self).lower()
        if query[0] == '1':
            if query[1] == '2' or query[1] == '0' or query[1] == '1':
                userhour = query[0:2]
                usermin = query[3:5]
                time_meridiem = query[6:9]
                print(time_meridiem)
                print(usermin)
                self.get_Reminder(userhour, usermin, time_meridiem)
        else:
            userhour = query[0]
            usermin = query[2:4]
            time_meridiem = query[5:8]
            print(time_meridiem)

        Speaking.speak(self, "The Alarm is set at" + userhour + "hours" + usermin + "Minutes Sir")
        # print("The Alarm is set at     "+userhour+"    hours     "+usermin+"       Minutes Sir")
        list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        if userhour in list:
            userhour = "0" + userhour
        while (True):

            if (time.get_Reminder(userhour, usermin, time_meridiem) == True):
                print("Hello")
                break
            else:
                print("HI")

                self.query2(userhour, usermin, time_meridiem)
                continue

    def check_Date_validity(self, date, Usermonth, year):
        speakig = Speaking()
        if int(date) < 0 or int(date) > 31:
            print("the date is invalid sir")
            speakig.speak("the date is invalid sir")
            return False
        if len(year) > 4:
            print(len(year))
            print("Invalid year sir")
            speakig.speak("Invalid year sir")
            return False
        list_Month = {'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                      'november', 'december'}
        if Usermonth not in list_Month:
            print("Invalid Month sir")
            speakig.speak("The month that you have given is invalid sir")
            return False
        if Usermonth == 'february':
            if int(year) % 4 == 0 and int(year) % 400 == 0 and int(date) > 29:
                return False
                speakig.speak("Invalid year Sir")
            elif int(date) > 28:
                speakig.speak("Invalid year Sir")
                return False
        else:
            return True

    def tell_days(self, days):
        dict_day = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'thursday', 5: 'friday', 6: 'saturday', 7: 'sunday',
                    0: 'sunday'}
        if days in dict_day.keys():
            days = dict_day[days]
            #  print(dict_day[days])
            Speaking.speak(self, "The days is " + days)

    def all_the_queries(self, query):
        speaking = Speaking()
        date = Date()
        time = Time()
        if "number to english" in query:
            speaking.speak("what is the number sir")
            ans = speaking.takeCommandHindi()
            speaking.speak("The number is " + ans)

        if "list" in query:
            speaking.speak("Do you know the number of elements to be added sir")
            query1 = speaking.takeCommand()
            if (query1 == 'yes'):
                making = Making_list()
                making.List_Making()
            else:
                making = Making_list()
                making.List_Making_Do_not_have_No()
        if 'number to hindi' in query:
            no = Number_to_Hindi()
            speaking.speak("tell me the number sir")
            number = (int)(speaking.takeCommand())

            no.Numbers(number)

        if 'wikipedia' in query:

            speaking.speak("Checking in the wikipedia Sir")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speaking.speak("According to wikipedia Sir")
            speaking.speak(result)


        elif 'set reminder' in query:
            self.set_Reminder()


        elif 'open youtube' in query:
            speaking.speak("Opening the youtube sir")
            webbrowser.open("www.youtube.com")

        elif 'open Google' in query:
            speaking.speak("Opening the google sir")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speaking.speak("Opening facebook sir")
            webbrowser.open("facebook.com")

        elif 'open geeksforgeeks' in query:
            speaking.speak("Opening geeks for geeks sir")
            print("Opening geeksforgeeks Sir")
            webbrowser.open("geeksforgeeks.org")

        elif 'open the news' in query:
            speaking.speak("Telling about the news sir")
            webbrowser.open("https://www.indiatvnews.com/")
            # speak(webbrowser.open("https://www.indiatvnews.com/"))
        elif 'open online classes' in query:
            speaking.speak("Opening the cousresite.com sir")
            webbrowser.open("https://blackboard.coursesites.com/")
            speaking.speak("Goodluck sir for studies")

        elif 'time' in query:
            time.tellTime(counter=1)
            # mywindow = tk.Tk()
            # clock = Digital_clock(mywindow)
            # mywindow.mainloop()
        elif "bye" in query:
            speaking.speak("Bye sir  Have a very good day sir.Take care")
            exit()
        elif "which day" in query:
            speaking.speak("Tell me the date sir")
            Date_of_the_user = speaking.takeCommand().strip()
            speaking.speak("Now tell me about the month sir")
            Month_of_User = speaking.takeCommand().lower().strip()

            speaking.speak("Now tell me about the year sir")
            Year_of_the_user = speaking.takeCommand().strip()
            Hello = date.No_of_odd_days_in_year(Year_of_the_user)
            Hello2 = date.No_of_Odd_Days_inMonths(Month_of_User, Year_of_the_user, Date_of_the_user)
            print(Hello2)
            days = (Hello2 + Hello) % 7

            if (self.check_Date_validity(Date_of_the_user, Month_of_User, Year_of_the_user)):
                speaking.speak(
                    "According to you th date is sir" + Date_of_the_user + Month_of_User + Year_of_the_user)
                print("According to you th date is sir" + Date_of_the_user + Month_of_User + Year_of_the_user)
                self.tell_days(days)
            else:
                print("Soryy")
        elif 'day' in query:
            date.tellDay()
        elif 'date' in query:
            date.telldate()
        elif 'shutdown the computer' in query:
            speaking.speak("Shutting down the computer Sir")
            Setting_control()
        # elif "battery update" in query:
        #     Battery()
        elif "Open drive" in query:
            Open()
