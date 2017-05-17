"""
Holds a list of locations (locations not displayed) for the scrollbar
"""

class LocationList:
    def __init__(self):
        self.allLocations = []


    """
    Add multiple locations to list of all locations given a list of locations.
    """
    def addMulti(self, locationList):
        for locationName in locationList:
            self.allLocations.append(locationName)


    """
    Return all locations from the list.
    """
    def getAll(self):
        return self.allLocations