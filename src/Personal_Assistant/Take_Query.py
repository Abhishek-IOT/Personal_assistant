import datetime
import webbrowser

import wikipedia

from src.Personal_Assistant.Date import Date
from src.Personal_Assistant.Speaking import Speaking
from src.Personal_Assistant.Time import Time


class Take_Query(Time, Date):

    def query(self):
        speaking = Speaking()
        #  speaking.WishMe()
        time = Time()
        while (True):
            query = speaking.takeCommand().lower()
            if 'wikipedia' in query:
                print(userhour)
                speaking.speak("Checking in the wikipedia Sir")
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=4)
                speaking.speak("According to wikipedia Sir")
                speaking.speak(result)
                continue
            elif 'set reminder' in query:
                speaking.speak("at which hour you want to set the reminder sir")
                # speak("tell us thea hour sir")
                query = speaking.takeCommand().lower()
                if query[0] == '1':
                    if query[1] == '2' or query[1] == '0' or query[1] == '1':
                        userhour = query[0:2]
                        usermin = query[3:5]
                        time_meridiem = query[6:9]
                        print(time_meridiem)
                        print(usermin)
                        time.get_Reminder(userhour, usermin, time_meridiem)
                else:
                    userhour = query[0]
                    usermin = query[2:4]
                    time_meridiem = query[5:8]
                    print(time_meridiem)
                speaking.speak("The Alarm is set at" + userhour + "hours" + usermin + "Minutes Sir")
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

                # print("the reminder hour" + userhour)
                # print("the reminder min" + usermin)

                continue

            elif 'open youtube' in query:
                speaking.speak("Opening the youtube sir")
                webbrowser.open("www.youtube.com")
                continue
            elif 'open google' in query:
                speaking.speak("Opening the google sir")
                webbrowser.open("google.com")
                continue
            elif 'open facebook' in query:
                speaking.speak("Opening facebook sir")
                webbrowser.open("facebook.com")
                continue
            elif 'open geeksforgeeks' in query:
                speaking.speak("Opening geeks for geeks sir")
                webbrowser.open("geeksforgeeks.com")
                continue
            elif 'open the news' in query:
                speaking.speak("Telling about the news sir")
                webbrowser.open("https://www.indiatvnews.com/")
                continue  # speak(webbrowser.open("https://www.indiatvnews.com/"))
            elif 'open online classes' in query:
                speaking.speak("Opening the cousresite.com sir")
                webbrowser.open("https://blackboard.coursesites.com/")
                speaking.speak("Goodluck sir for studies")
                continue
            elif 'time' in query:
                time.tellTime()
                continue
            elif "jarvis bye" in query:
                speaking.speak("Bye sir  Have a very good day sir.Take care")
                exit()


            elif 'date' in query:
                date = Date()
                date.telldate()
                continue

    def query2(self, userhour, usermin, time_merdiem):
        speaking = Speaking()
        #  speaking.WishMe()
        time = Time()

        timereal = str(datetime.datetime.now())
        if time_merdiem == 'p.m':
            userhour = int(userhour) + 12
            userhour = str(userhour)

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
                if 'wikipedia' in query:
                    print(userhour)
                    speaking.speak("Checking in the wikipedia Sir")
                    query = query.replace("wikipedia", "")
                    result = wikipedia.summary(query, sentences=4)
                    speaking.speak("According to wikipedia Sir")
                    speaking.speak(result)
                    continue
                elif 'set reminder' in query:
                    speaking.speak("at which hour you want to set the reminder sir")
                    # speak("tell us thea hour sir")
                    query = speaking.takeCommand().lower()
                    if query[0] == '1':
                        if query[1] == '2' or query[1] == '0' or query[1] == '1':
                            userhour = query[0:2]
                            usermin = query[3:5]
                            time_meridiem = query[6:9]
                            print(time_meridiem)
                            print(usermin)
                            time.get_Reminder(userhour, usermin, time_meridiem)
                    else:
                        userhour = query[0]
                        usermin = query[2:4]
                        time_meridiem = query[5:8]
                        print(time_meridiem)
                        speaking.speak("The Alarm is set at" + userhour + "hours" + usermin + "Minutes Sir")
                        print("The Alarm is set at     " + userhour + "    hours     " + usermin + "       Minutes Sir")
                        list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
                        if userhour in list:
                            userhour = "0" + userhour
                        while (True):
                            if (time.get_Reminder(userhour, usermin, time_meridiem) == True):
                                break
                            else:
                                self.query(userhour, usermin)
                                continue
            else:
                print("this is alarm time sir")
                speaking.speak("Alarm time sir")
                b = False
