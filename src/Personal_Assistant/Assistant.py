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

# engine=pyttsx3.init('dummy')
# if sapi5 is giving any error you can first try with the dummy parameter and then with the sapi5 parameter and also remember the case used in it
# engine = pyttsx3.init('sapi5')
# sapi 5 voice is the default voice for windows
# voices = engine.getProperty('voices')
# getter method for the pyttsx3
# engine.setProperty('voice', voices[0].id)


# setter method for the pyttsx3


# def speak(audio):
#   engine.say(audio)  # Method for the speaking of the the assistant
#  engine.runAndWait()


# def WishMe():
#   hour = int(datetime.datetime.now().hour)
#   if hour >= 0 and hour < 12:  # Method for Wishing the master
#      speak('Good morning sir')
# elif hour >= 12 and hour < 18:
#    speak("Good afternoon sir")
# else:
#   speak('Good evening sir')
# speak('I am Jarvis   .Please tell how may I help u Sir')
from src.Personal_Assistant.Speaking import Speaking

"""
def takeCommand():
# this method is for taking the commands and recognizing the command
    r = sr.Recognizer()
# from the speech_Recognition module we will use the recongizer method for recognizing
    with sr.Microphone() as source:
        #from the speech_Recognition module we will use the Microphone module for listening the command
        print('Listening')
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            # for listening the command in indian english
            print("the query is printed='", Query, "'")
            # for printing the query or the command that we give
        except Exception as e:
            print(
                e)  # this method is for handling the exception and so that assistant can ask for telling again the command
            print("Say that again sir")
            return "None"
        return Query



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


def telltime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    sec = time[18:19]
    print(hour + min + sec)
    speak(hour + "Hours" + min + "Minutes" + sec + "Seconds sir")




"""
if __name__ == '__main__':  # main method for executing the functions
     speaking = Speaking()

"""
    WishMe()
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak("Checking in the wikipedia Sir")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=4)
        speak("According to wikipedia Sir")
        speak(result)
    elif 'open youtube' in query:
        speak("Opening the youtube sir")
        webbrowser.open("www.youtube.com")
    elif 'open google' in query:
        speak("Opening the google sir")
        webbrowser.open("google.com")
    elif 'open facebook' in query:
        speak("Opening facebook sir")
        webbrowser.open("facebook.com")
    elif 'open geeksforgeeks' in query:
        speak("Opening geeks for geeks sir")
        webbrowser.open("geeksforgeeks.com")
    elif 'open the news' in query:
        speak("Telling about the news sir")
        webbrowser.open("https://www.indiatvnews.com/")
    # speak(webbrowser.open("https://www.indiatvnews.com/"))
    elif 'open online classes' in query:
        speak("Opening the cousresite.com sir")
        webbrowser.open("https://blackboard.coursesites.com/")
        speak("Goodluck sir for studies")
    elif 'time' in query:
        telltime()
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
