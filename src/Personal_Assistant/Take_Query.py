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
