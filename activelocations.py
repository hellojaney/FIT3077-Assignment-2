"""
A list that contains all of the displayed locations.
The locations are stored as instances of Location.
"""

class ActiveLocations:
    def __init__(self):
        self.activeList = []

    # removes location from the ActiveLocations list
    def removeLocation(self, locationName):
        index = 0
        while index < len(self.activeList):
            if self.activeList[index].getName() == locationName:
                del self.activeList[index]
                return
            index += 1
        print("Error: Couldn't delete location from active locations, location not found.")

    # add location to ActiveLocations list
    def add(self, newLocation):
        self.activeList.append(newLocation)

    def exists(self, newLocation):
        for location in self.activeList:
            if location.getName() == newLocation:
                return True
        return False

    # add multiple locations to ActiveLocations list (temp??)
    def addMulti(self, locationsList):
        for monitor in locationsList:
            self.activeList.append(monitor)