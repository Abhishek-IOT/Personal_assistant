import pyttsx3

engine=pyttsx3.init('Sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)