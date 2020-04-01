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
