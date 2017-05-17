from suds.client import Client

"""
Web Client relies in Suds Jurko Client class
Obtains location data from the web server.
"""

class WebClient:
    def __init__(self, url):
        self.client = Client(url)

    """
    Retrieves a list of all location names.
    """
    def getLocationNames(self):
        locations = self.client.service.getLocations()
        return locations

    """
    Retrieves data associated to a given location.
    """
    def getWeatherData(self, location):
        locationData = []

        # obtain temperature data
        temperature = self.client.service.getTemperature(location)[-1]
        locationData.append(temperature)

        # obtain rainfall data
        date_time, rainfall = self.client.service.getRainfall(location)
        locationData.append(rainfall)

        # obtain timestamp data
        date, time = date_time.split(' ')
        locationData.append(date)
        locationData.append(time)

        return locationData