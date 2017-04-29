"""
A list that contains all of the displayed locations.
The locations are stored as instances of Location
"""
from weatherframe import WeatherFrame
from weatherframecollection import WeatherFrameCollection

class ActiveLocations:
    def __init__(self):
        self.activeList = []


    def removeLocation(self, locationName):
        index = 0
        while index < len(self.activeList):
            if self.activeList[index].getName() == locationName:
                del self.activeList[index]
                return
            index += 1

        print("Error: Couldn't delete location from active locations, location not found.")


    def add(self, newLocation):
        self.activeList.append(newLocation)


    def addMulti(self, locationsList):
        for monitor in locationsList:
            self.activeList.append(monitor)