"""
A list that contains all of the displayed locations.
The locations are stored as instances of Location class.
"""

class ActiveLocations:
    def __init__(self):
        self.activeList = []


    """
    Remove location from ActiveLocations list given a location name.
    """
    def removeLocation(self, locationName):
        index = 0
        while index < len(self.activeList):
            if self.activeList[index].getName() == locationName:
                del self.activeList[index]
                return
            index += 1
        print("Error: Couldn't delete location from active locations, location not found.")


    """
    Add a location to ActiveLocations list given a new location.
    """
    def add(self, newLocation):
        self.activeList.append(newLocation)
