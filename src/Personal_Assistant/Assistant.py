""""
User=Abhishek Srivastav
Github UserName=Abhishek-IOT
Personal Assistant project

"""
# there is reformating of code trying the OOPs Approach so that can use the concept of OOPS
# importing the webbrowser module for opening the webbrowser

# for taking the time for wishMe method
# import pyttsx3
# for taking the voice from the window and the laptop
# importing the wikipedia module for having a search from wikipedia

import webbrowser

import wikipedia

from src.Personal_Assistant.Date import Date
from src.Personal_Assistant.Speaking import Speaking
from src.Personal_Assistant.Time import Time

"""




def set_Reminder(userhour):
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    if userhour == hour:
        speak("Sir your reminder")



"""
if __name__ == '__main__':  # main method for executing the functions
    speaking = Speaking()
    speaking.WishMe()
    time = Time()
    query = speaking.takeCommand().lower()
    if 'wikipedia' in query:
        speaking.speak("Checking in the wikipedia Sir")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=4)
        speaking.speak("According to wikipedia Sir")
        speaking.speak(result)
    elif 'open youtube' in query:
        speaking.speak("Opening the youtube sir")
        webbrowser.open("www.youtube.com")
    elif 'open google' in query:
        speaking.speak("Opening the google sir")
        webbrowser.open("google.com")
    elif 'open facebook' in query:
        speaking.speak("Opening facebook sir")
        webbrowser.open("facebook.com")
    elif 'open geeksforgeeks' in query:
        speaking.speak("Opening geeks for geeks sir")
        webbrowser.open("geeksforgeeks.com")
    elif 'open the news' in query:
        speaking.speak("Telling about the news sir")
        webbrowser.open("https://www.indiatvnews.com/")
    # speak(webbrowser.open("https://www.indiatvnews.com/"))
    elif 'open online classes' in query:
        speaking.speak("Opening the cousresite.com sir")
        webbrowser.open("https://blackboard.coursesites.com/")
        speaking.speak("Goodluck sir for studies")

    elif 'time' in query:
        time.tellTime()
    elif "jarvis bye" in query:
        speaking.speak("Bye sir  Have a very good day sir.Take care")
        exit()


    elif 'date' in query:
        date = Date()
        date.telldate()

    elif 'set reminder' in query:
        speaking.speak("at which hour you want to set the reminder sir")
        # speak("tell us the hour sir")
        c = 0
        query = speaking.takeCommand().lower()
        if query[0] == '1':
            if query[1] == '2' or query[1] == '0' or query[1] == '1':
                userhour = query[0:2]
                usermin = query[3:5]
        else:
            userhour = query[0]
            usermin = query[2:4]
        speaking.speak("Setting the reminder at" + userhour + "hour" + usermin + "Minuetes sir")
        list = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        if userhour in list:
            userhour = "0" + userhour

        time.set_Reminder(userhour, usermin)
        print("the reminder hour" + userhour)
        print("the reminder min" + usermin)


        for i in range(query.__len__()):
            print(query[i],c)
            c=c+1

