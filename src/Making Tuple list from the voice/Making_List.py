from src.Personal_Assistant.Speaking import Speaking


class Making_list:
    speaking = Speaking()

    def List(self):
        speaking = Speaking()
        speaking.speak("how many elements do you want in the list sir")
        query = (int)(speaking.takeCommand())
        list = []
        for i in range(query):
            item = speaking.takeCommand()
            list.append(item)
        print(list)
