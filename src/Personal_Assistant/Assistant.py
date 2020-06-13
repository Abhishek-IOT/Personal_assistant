""""
User=Abhishek Srivastav
Github UserName=Abhishek-IOT
Personal Assistant project

"""
# there is reformating of code trying the OOPs Approach so that can use the concept of OOPS
# importing the webbrowser module for opening the webbrowser

# for taking the time for wishMe method
# import pyttsx3
# for taking the voice from the window and the laptop
# importing the wikipedia module for having a search from wikipedia

from src.Personal_Assistant.Take_Query import Take_Query
from src.Personal_Assistant.Take_brake import Take_brake


class Assistant:
    if __name__ == '__main__':  # main method for executing the functions
        take = Take_brake()
        takequery = Take_Query()
        takequery.query()

