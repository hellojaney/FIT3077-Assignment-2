from collection import Collection
from location import Location

class LocationCollection(Collection):
    def __init__(self, caller):
        Collection.__init__(self, caller)


    """
    Creates a location object and adds it to the collection list
    """
    def createLocation(self, locationName, serviceType, viewOption, dataOption):
        location = Location(locationName, serviceType, viewOption, dataOption, self)
        if not self.exists(location):
            self.add(location)
            return location  #return location to the controller so that we can use it to make a monitor
        else:
            return None

    def exists(self, location):
        n = location.name
        s = location.serviceType
        v = location.viewType
        d = location.dataType

        for loc in self.collectionList:
            if loc.name == n and loc.serviceType == s and loc.viewType == v and loc.dataType == d:
                return True
        return False


    def removeFromCollection(self, location):
        if self.exists(location):
            self.collectionList.remove(location)
        else:
            print("Error: Couldn't delete " + location.name +", was not found.")
