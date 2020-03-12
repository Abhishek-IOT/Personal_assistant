import datetime

import pyttsx3

engine = pyttsx3.init('Sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning sir')
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir")
    else:
        speak('Good evening sir')
