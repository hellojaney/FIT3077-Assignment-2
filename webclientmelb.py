from webclient import WebClient
from suds.client import Client

"""
WebClientMelb creates an instance of the Web Client
"""
class WebClientMelb(WebClient):
    def __init__(self):
        WebClient.__init__(self)
        self.client = Client('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')

    """
    Obtains all location names from the web client
    """
    def getLocationNames(self):
        locations = self.client.service.getLocations()
        return locations

    """
    Obtains weather data from the web client for a specific location
    """
    def getWeatherData(self, location):
        temperatureData = self.client.service.getTemperature(location)
        temperature = temperatureData[1]

        rainfallData = self.client.service.getRainfall(location)
        rainfall = self.formatNoneData(rainfallData[1])

        date, time = rainfallData[0].split(' ')

        return temperature, rainfall, date, time