from PyDictionary import PyDictionary

from src.Personal_Assistant.Speaking import Speaking


class Meaning:
    dic = PyDictionary()
    speak = Speaking()
    speak.speak("Which word do u want to find the meaning sir")
    query = speak.takeCommand()
    word = dic.meaning(query)
    print(len(word))
    for states in word:
        print(word[states])
        speak.speak("the meaning  is" + str(word[states]))
