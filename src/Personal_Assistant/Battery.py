import time

import psutil
from plyer import notification

from src.Personal_Assistant.Speaking import Speaking


class Battery():
    battery = psutil.sensors_battery()

    speaking = Speaking()

    # from psutil we will import the sensors_battery class and with that we have the battery remaining
    while (True):
        percent = battery.percent
        #        print("the battery percentage is "+percent)
        speaking.speak("the battery percentage is " + str(percent))
        notification.notify(
            title="Battery Percentage",
            message=str(percent) + "% Battery remaining",
            timeout=10)
        break
    time.sleep(60 * 60)
    # after every 60 mins it will show the battery percentage
