class InactiveLocations:
    def __init__(self):
        self.list = []

    def add(self, newLocation):
        self.list.append(newLocation)

    def addMulti(self, locationList):
        for locationName in locationList:
            self.list.append(locationName)

    def remove(self, locationName):
        for loc in self.list:
            if loc == locationName:
                self.list.remove(loc)
                return
        print("Error: could not remove " + str(locationName) + " from list of locations")

    def getAll(self):
        return self.list