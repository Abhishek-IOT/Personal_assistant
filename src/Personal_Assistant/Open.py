import os

from src.Personal_Assistant.Speaking import Speaking


class Open:
    speaking = Speaking()
    speaking.speak("Which drive do you want to open sir")
    take = speaking.takeCommand()
    if "C" in take or "c" in take:
        speaking.speak("Opening the C drive Sir")
        os.startfile("C:")
    if "D" in take or "d" in take:
        speaking.speak("Opening the D drive Sir")
        os.startfile("D:")
    if "E" in take or "e" in take:
        speaking.speak("Opening the E drive Sir")
        os.startfile("E:")
