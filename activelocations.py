"""
A list that contains all of the displayed locations.
The locations are stored as instances of Location
"""
import threading
from weatherframe import WeatherFrame
from weatherframecollection import WeatherFrameCollection

class ActiveLocations:
    def __init__(self, gui):
        self.gui = gui
        self.activeList = []
        #self.startRefresh()
        #self.timer = perpetualTimer(5, self.refreshLocations()).start()


    def refreshLocations(self, wFrameCollection):
        wFrameCollection.clearAllFrames()


    def add(self, newLocation):
        self.activeList.append(newLocation)


    def addMulti(self, locationsList):
        for monitor in locationsList:
            self.activeList.append(monitor)