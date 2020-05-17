from src.Personal_Assistant.Speaking import Speaking


class Making_list(Speaking):
    def List_Making(self):
        speaking = Speaking()
        speaking.speak("how many elements do you want in the list sir")
        query = speaking.takeCommand()
        query = (int)(query)
        list = []
        speaking.speak("Tell me the elements in the list sir")
        for i in range(query):
            item = speaking.takeCommand()
            list.append(item)
            speaking.speak("the" + item + "is added in the list sir")
        print(list)

    def List_Making_Do_not_have_No(self):
        speaking = Speaking()
        i = 0
        while (True):
            query = speaking.takeCommand()
            speaking.speak(i + "Element is " + query)
            speaking.speak("do you want to stop adding sir")
            query1 = speaking.takeCommand()
            if (query1 == 'yes'):
                break
            else:
                continue
