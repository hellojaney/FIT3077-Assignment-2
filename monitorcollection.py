"""
Holds a list of all WeatherFrame instances.
"""

class MonitorCollection:
    def __init__(self):
        self.monitorList = []

    """
    Add a frame to the Weather Frame Collection list given a new frame.
    """
    def addMonitor(self, newFrame):
        self.monitorList.append(newFrame)


    """
    Closes frame from the window and remove all frames from the Weather Frame Collection.
    """
    def clearAllMonitors(self):
        for monitor in self.monitorList:
            monitor.closeMonitor(monitor.frame)
        self.monitorList = []