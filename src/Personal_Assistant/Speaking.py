import datetime
from tkinter import *
from tkinter import ttk
import pyttsx3
import speech_recognition as sr


class Speaking():
    def __int__(self):
        pass

        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
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
        pyttsx3.speak('I am Yeeeear .Please tell how may I help u Sir')

    def takeCommand(self):
        # this method is for taking the commands and recognizing the command
        r = sr.Recognizer()
        # from the speech_Recognition module we will use the recongizer method for recognizing
        with sr.Microphone() as source:
            # from the speech_Recognition module we will use the Microphone module for listening the command
            print('Listening')
            r.pause_threshold = 0.7  # seconds of non-speaking audio before a phrase is considered complete
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

    def takeCommandHindi(self):
        # this method is for taking the commands and recognizing the command
        r = sr.Recognizer()
        # from the speech_Recognition module we will use the recongizer method for recognizing
        with sr.Microphone() as source:
            # from the speech_Recognition module we will use the Microphone module for listening the command
            print('Listening')
            r.pause_threshold = 0.7  # seconds of non-speaking audio before a phrase is considered complete
            audio = r.listen(source)
            try:
                print("Recognizing")
                Query = r.recognize_google(audio, language='hi-In')
                # for listening the command in indian english
                print("the query is printed='", Query, "'")
                # for printing the query or the command that we give
            except Exception as e:
                print(
                    e)  # this method is for handling the exception and so that assistant can ask for telling again the command
                print("Say that again sir")
                return "None"
            return Query
