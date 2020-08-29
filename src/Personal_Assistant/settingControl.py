import os

from src.Personal_Assistant.Speaking import Speaking


class settingControl:
    speaking = Speaking()
    speaking.speak("Do you want to shutdown the computer")
    input_choice = speaking.takeCommand()

    # input_choice=input("Shutdown the computer ( yes or not) ")
    if input_choice == "yes" or input_choice == 'y' or input_choice == 'Y':
        print("shutting down the os")
        os.system("Shutdown /s /t 30")
    elif input_choice == "no":
        print("Thank you Sir")
