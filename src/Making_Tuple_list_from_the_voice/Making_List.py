from src.Personal_Assistant.Speaking import Speaking


class Making_list(Speaking):
    def List_Making(self):
        speaking = Speaking()
        speaking.speak("how many elements do you want in the list sir")
        query = speaking.takeCommand()
        query = (int)(query)
        list = []
        for i in range(query):
            item = speaking.takeCommand()
            list.append(item)
        print(list)
