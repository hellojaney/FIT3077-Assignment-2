from webclient import WebClient
from suds.client import Client

class MelbClient(WebClient):
    def __init__(self):
        WebClient.__init__(self)
        self.client = Client('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')

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