import datetime

# for taking the time for wishMe method
import pyttsx3

# for taking the voice from the window and the laptop

engine = pyttsx3.init('Sapi5')
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
