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


    """
    Checks to see if a Location exists for a particular location
    Looks at the location name, what it is viewing (temp/rain/both) and its service type (kind of web client)
    """
    def exists(self, location):
        l = location.name
        s = location.serviceType
        v = location.viewType
        d = location.dataType

        for loc in self.collectionList:
            if loc.name == l and loc.serviceType == s and loc.viewType == v and loc.dataType == d:
                return True
        return False


    """
    Remove location from list of active locations
    Looks at the location name, what it is viewing (temp/rain/both) and its service type (kind of web client)
    """
    def remove(self, locationName, serviceType, viewType, dataType):
        index = 0
        for location in self.collectionList:
            if location.name == locationName and location.serviceType == serviceType and location.viewType == viewType and location.dataType == dataType:
                location.stopTimer()
                index  = self.collectionList.index(location)
                del self.collectionList[index]
                return
            index += 1
        print("Error: Couldn't delete from active monitors, monitor not found.")