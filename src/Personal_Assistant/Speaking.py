import datetime

import pyttsx3
from pyttsx3 import engine


class Speaking():
    def __int__(self):
        pass

    def eng(self):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

    def speak(audio):
        engine.say(audio)  # Method for the speaking of the the assistant
        engine.runAndWait()

    def WishMe(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:  # Method for Wishing the master
            pyttsx3.speak('Good morning sir')
        elif hour >= 12 and hour < 18:
            pyttsx3.speak("Good afternoon sir")
        else:
            pyttsx3.speak('Good evening sir')
        pyttsx3.speak('I am Jarvis   .Please tell how may I help u Sir')
