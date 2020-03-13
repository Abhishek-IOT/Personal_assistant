import datetime

# for taking the time for wishMe method
import pyttsx3
# for taking the voice from the window and the laptop
import speech_recognition as sr

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
    speak('I am Jarvis   .Please tell how may I help u Sir')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')
            print("the query is printed='", Query, "'")
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"
        return Query


if __name__ == '__main__':
    pass
