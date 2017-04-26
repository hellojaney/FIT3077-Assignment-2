"""
Legit just a list. It will contain the montitors that are active in the GUI
Can decide later how we store the monitors in here
    - As an entire Monitor class?
    - Just the location name?
That will depend on how we will use this list
"""
import time
from timer import Timer

class ActiveMonitors:
    def __init__(self):
        self.list = []
        self.timer = Timer()
        #instantiate timer and update all active montiors every 5 minutes
        """
        while True:
            if self.list == []:
                pass
            else:
                currentTime = time.localtime(time.time())
                if self.timer.checkTimer(currentTime) == True:
                    for monitor in self.list:
                        monitor.createFrame()
        """

    def add(self, newMonitor):
        self.list.append(newMonitor)


    def addMulti(self, monitorList):
        for monitor in monitorList:
            self.list.append(monitor)

