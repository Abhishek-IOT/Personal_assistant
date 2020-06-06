from src.Personal_Assistant.Speaking import Speaking
from src.Personal_Assistant.Take_Query import Take_Query
from src.Personal_Assistant.Time import Time


class Take_break:
    speaking = Speaking()
    take_query = Take_Query()
    time = Time()
    speaking.WishMe()
    query = time.tellTime(1)

    min_later = (int)(query[1]) + 45

    if min_later >= 60:
        min_later = min_later - 45

    time_query = Take_Query()
    while (True):
        query = time.tellTime(counter=0)
        hour = (int)(query[0])
        min = (int)(query[1])
        print(min_later)
        print(min)
        if min_later == min:
            print("Break Time sir")
            speaking.speak("Break Time sir")

            break
        else:
            query = speaking.takeCommand()
            take_query.all_the_queries(query)
            continue


