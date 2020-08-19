from plyer import notification
import pyttsx3
import datetime
import time




class Year:
    def Speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    def Wishme(self):
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            pyttsx3.speak('Good morning Sir')
        elif hour >= 12 and hour < 18:
            pyttsx3.speak("Good afternoon Sir")
        else:
            pyttsx3.speak('Good evening Sir')
        pyttsx3.speak('I am Assistant ')

    def Take_break(self):
        while (True):
            pyttsx3.speak("We will start in 5 mins Sir")

            time.sleep(5 * 60)
            pyttsx3.speak("Let's Start Sir")
            notification.notify(
                title="Let's Start Sir ",
                message="Will Alert you after 45 minutes",
                timeout=10
            )
            time.sleep(45 * 60)
            pyttsx3.speak("Please take a break Sir")
            notification.notify(
                title="Take a Break Sir",
                message="Please do use your device after sometime as you have been continuously using it for 45 mins and it will affect your eyes",
                timeout=10
            )
if __name__ == '__main__':
    Maam=Year()
    Maam.Wishme()
    Maam.Take_break()

