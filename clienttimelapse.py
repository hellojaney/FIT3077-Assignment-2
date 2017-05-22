from webclient import WebClient
from suds.client import Client


class ClientTimeLapse(WebClient):
    def __init__(self):
        WebClient.__init__(self)
        self.client = Client('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeatherTimeLapse?wsdl')


    def getLocationNames(self):
        locations = self.client.service.getLocations()
        return locations


    def getWeatherData(self, location):
        locationData = []

        #get weather from timelapseclient; example of how it looks: [27/04/2017 7:02:56, 280.9, 0.2]
        tempData = self.client.service.getWeather(location)

        #obtain temperature data
        locationData.append(tempData[1])

        # obtain rainfall data
        locationData.append(tempData[2])

        # obtain timestamp data
        date, time = tempData[0].split(' ')
        locationData.append(date)
        locationData.append(time)

        return locationData