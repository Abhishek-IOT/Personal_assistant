""""
User=Abhishek Srivastav
Github UserName=Abhishek-IOT
Personal Assistant project

"""
import datetime
import webbrowser

# for taking the time for wishMe method
import pyttsx3
# for taking the voice from the window and the laptop
import speech_recognition as sr
import wikipedia

# engine=pyttsx3.init('dummy')
# if sapi5 is giving any error you can first try with the dummy parameter and then with the sapi5 parameter and also remember the case used in it
engine = pyttsx3.init('sapi5')
# sapi 5 voice is the default voice for windows
voices = engine.getProperty('voices')
# getter method for the pyttsx3
engine.setProperty('voice', voices[0].id)


# setter method for the pyttsx3


def speak(audio):
    engine.say(audio)  # Method for the speaking of the the assistant
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:  # Method for Wishing the master
        speak('Good morning sir')
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    else:
        speak('Good evening sir')
    speak('I am Jarvis   .Please tell how may I help u Sir')


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
            #for listening the command in indian english
            print("the query is printed='", Query, "'")
            #for printing the query or the command that we give
        except Exception as e:
            print(
                e)  # this method is for handling the exception and so that assistant can ask for telling again the command
            print("Say that again sir")
            return "None"
        return Query


if __name__ == '__main__':  # main method for executing the functions
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
