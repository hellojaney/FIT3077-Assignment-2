"""
Holds a list of all WeatherFrame instances.
"""

class MonitorCollection:
    def __init__(self):
        self.monitorList = []

    """
    Add a frame to the Monitor Collection list given a new frame.
    """
    def addMonitor(self, newMonitor):
        self.monitorList.append(newMonitor)


    """
    Checks to see if a Monitor exists for a particular location
    """
    def exists(self, locationName, viewOption):
        for monitor in self.monitorList:
            if monitor.location.getName() == locationName and monitor.viewOption == viewOption:
                return True
        return False


    """
    Remove monitor from list of active monitors
    """
    def remove(self, locationName):
        index = 0
        while index < len(self.monitorList):
            if self.monitorList[index].getLocation().getName() == locationName:
                del self.monitorList[index]
                return
            index += 1
        print("Error: Couldn't delete location from active locations, location not found.")