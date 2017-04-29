"""
A list that contains all of the displayed locations.
The locations are stored as instances of Location
"""
import threading
from weatherframe import WeatherFrame

class ActiveLocations:
    def __init__(self):
        self.list = []
        self.startRefresh()

    def startRefresh(self):
        threading.Timer(300, self.refreshLocations).start()


    def refreshLocations(self):
        pass


    def add(self, newLocation):
        self.list.append(newLocation)


    def addMulti(self, locationsList):
        for monitor in locationsList:
            self.list.append(monitor)