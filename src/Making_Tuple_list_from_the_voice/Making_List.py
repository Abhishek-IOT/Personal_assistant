import pandas as pd

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
        speaking.speak("Tell me the elements sir")
        i = 0
        list1 = []
        while (True):
            query = speaking.takeCommand()
            list1.append(i + 1)
            list1.append(query)
            speaking.speak((str)(i + 1) + "Element is " + query)
            speaking.speak("do you want to stop adding sir")
            query1 = speaking.takeCommand()
            i = i + 1
            print("the list=", list1)
            if (query1 == 'yes'):
                speaking.speak("the final list is sir" + str(list1))
                df = pd.DataFrame(list1)
                df.to_csv('filename.csv', index=False)
                speaking.speak(
                    "Thank you for making the list with help of me sir and I converting the list to csv file sir")

                speaking.speak("Do you want to know the number of elements in the list sir")
                take = speaking.takeCommand()
                if (take == 'yes'):
                    speaking.speak(list1[(list1.__len__()) - 2])
                    print(list1.__len__())

                else:
                    speaking.speak("thank you sir")
                break
            else:
                speaking.speak("The next element is sir")
                continue
