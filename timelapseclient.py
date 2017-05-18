from webclient import WebClient
from suds.client import Client

class TimeLapseClient(WebClient):
    def __init__(self):
        WebClient.__init__(self)
        self.client = Client('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeatherTimeLapse?wsdl')

    def getWeatherTimeLapse(self, location):
        return self.client.service.getWeather(location)