from collection import Collection
from location import Location
from monitortext import MonitorText
from monitorgraph import MonitorGraph

"""
Holds a list of all WeatherFrame instances.
"""

class MonitorCollection(Collection):
    def __init__(self, caller):
        Collection.__init__(self, caller)


    """
    Creates a text monitor and stores it in the collection
    """
    def createTextMonitor(self, location, root):
        monitor = MonitorText(location, root, self)
        self.add(monitor)


    """
    Creates a graph monitor and stores it in the collection
    """
    def createGraphMonitor(self, location):
        monitor = MonitorGraph(location, self)
        self.add(monitor)


    """
    Checks to see if a Monitor exists by checking the details of the location that it holds
    """
    def exists(self, locationName, serviceType, viewType, dataType):
        for monitor in self.collectionList:
            if monitor.location.name == locationName and monitor.location.serviceType == serviceType and monitor.location.viewType == viewType and monitor.location.dataType == dataType:
                return True
        return False


    """
    Remove monitor from list of active monitors
    """
    def remove(self, locationName, serviceType, viewType, dataType):
        index = 0
        for monitor in self.collectionList:
            if monitor.location.name == locationName and monitor.location.serviceType == serviceType and monitor.location.viewType == viewType and monitor.location.dataType == dataType:
                monitor.location.stopTimer()
                index  = self.collectionList.index(monitor)
                del self.collectionList[index]
                return
            index += 1
        print("Error: Couldn't delete from active monitors, monitor not found.")
        print "monitor removed."

    """
        Removes all monitors and all (attached) locations
        """

    def removeAll(self):
        for monitor in self.collectionList:
            monitor.remove()