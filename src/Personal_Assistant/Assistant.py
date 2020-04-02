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

"""




def set_Reminder(userhour):
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    if userhour == hour:
        speak("Sir your reminder")


def telldate():
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

    speak(dateno + month + this_year)
    print(todaydate)





"""
if __name__ == '__main__':  # main method for executing the functions
    speaking = Speaking()
    speaking.WishMe()
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
        Date.telltime()
        """
    elif 'date' in query:
        telldate()
    elif 'set reminder' in query:
        speak("at which hour you want to set the reminder sir")
        #speak("tell us the hour sir")
        query = takeCommand().lower()
        



    elif "jarvis bye" in query:
        speak("Bye sir  Have a very good day sir.Take care")
        exit()
    
    """
