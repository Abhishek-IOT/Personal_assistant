import psutil
import time
from plyer import notification
battery=psutil.sensors_battery()
class Battery:
#from psutil we will import the sensors_battery class and with that we have the battery remaining
    while(True):
	    percent=battery.percent
	    notification.notify(
    	    title="Battery Percentage",
    	    message=str(percent)+"% Battery remaining",
    	    timeout=10
        )
        time.sleep(60*60)
    #after every 60 mins it will show the battery percentage
	    continue



