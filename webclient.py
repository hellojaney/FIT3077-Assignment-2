"""
Add class description here (tbd right now)
"""

class WebClient:
    def __init__(self):
        pass

    """
    Retrieves a list of all location names.
    """
    def getLocationNames(self):
        locations = self.client.service.getLocations()
        return locations

    """
    Retrieves data associated to a given location from MelbourneWeatherData.
    """
    def getWeatherData(self, location):
        pass


    """
    Retrieves data associated to a given location from MelbourneWeatherTimeLapse.
    """
    def getWeatherTimeLapse(self, location):
        pass


