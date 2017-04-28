"""
Legit just a list. It will contain the montitors that are active in the GUI
Can decide later how we store the monitors in here
    - As an entire Monitor class?
    - Just the location name?
That will depend on how we will use this list
"""
import threading
from webclient import WebClient

class ActiveMonitors:
    def __init__(self):
        self.list = []


    def startRefresh(self):
        threading.Timer(300, self.refreshMonitors).start()


    def refreshMonitors(self):
        for monitor in self.list:
            print(monitor.getAllInfo())


    def add(self, newMonitor):
        self.list.append(newMonitor)


    def addMulti(self, monitorList):
        for monitor in monitorList:
            self.list.append(monitor)

