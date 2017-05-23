"""
Add class description here (tbd right now)
"""

class WebClient:
    def __init__(self):
        # 'declare' the class variables
        self.client = None

    """
    Retrieves a list of all location names.
    """
    def getLocationNames(self):
        pass

    """
    Retrieves weather data associated to a given location from the web service.
    """
    def getWeatherData(self, location):
        pass

    """
    Takes input and if its datatype is None, then it returns a "-" string. 
    """
    def formatNoneData(self, input):
        if input is None:
            return "-"
        else:
            return input




