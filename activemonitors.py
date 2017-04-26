"""
Legit just a list. It will contain the montitors that are active in the GUI
Can decide later how we store the monitors in here
    - As an entire Monitor class?
    - Just the location name?
That will depend on how we will use this list
"""
import time

class ActiveMonitors:
    def __init__(self):
        self.list = []
        self.timer = time.localtime(time.time())

    def add(self, newMonitor):
        self.list.append(newMonitor)

    def addMulti(self, monitorList):
        for monitor in monitorList:
            self.list.append(monitor)

    def checkTimer(self,timer, currentTime):
        if timer/currentTime == 5:
            return True
        else:
            return False

