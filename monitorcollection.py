from collection import Collection
from location import Location
from monitortext import MonitorText
from monitorgraph import MonitorGraph

"""
Monitor Collection holds all instances of individual monitors for each Location
"""

class MonitorCollection(Collection):
    def __init__(self):
        Collection.__init__(self)

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
        monitor.openGraph()

    """
    Checks to see if the monitor exists for the location
    """
    def exists(self, mon):
        monitorLocation = mon.getLocation()
        n = monitorLocation.name
        s = monitorLocation.serviceType
        v = monitorLocation.viewType
        d = monitorLocation.dataType

        for mon in self.collectionList:
            monLocation = mon.getLocation()
            if monLocation.name == n and monLocation.serviceType == s and monLocation.viewType == v and monLocation.dataType == d:
                return True
        return False

    """
    Removes specific monitor from the Monitor Collection
    """
    def removeFromCollection(self, monitor):
        if self.exists(monitor):
            self.collectionList.remove(monitor)
        else:
            print("Error: Couldn't delete monitor for " + monitor.location.name + ", was not found.")


    """
    Removes all monitors and all locations from the Monitor Collection
    """
    def removeAll(self):
        temporaryList = []
        for monitor in self.collectionList:
            temporaryList.append(monitor)

        for monitor in temporaryList:
            monitor.remove()

        if len(self.collectionList) != 0:
            print "Did not shut down all monitors"
