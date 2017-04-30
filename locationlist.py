"""
Holds a list of inactive locations (locations not displayed) for the scrollbar
"""

class LocationList:
    def __init__(self):
        self.allLocations = []

    def addMulti(self, locationList):
        for locationName in locationList:
            self.allLocations.append(locationName)

    def getAll(self):
        return self.allLocations