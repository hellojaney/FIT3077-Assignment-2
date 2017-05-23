from suds.client import Client


class WebClientTimeLapse():
    def __init__(self):
        self.client = Client('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeatherTimeLapse?wsdl')


    def getLocationNames(self):
        locations = self.client.service.getLocations()
        return locations


    def getWeatherData(self, location):
        weatherData = self.client.service.getWeather(location)
        temperature = weatherData[1]
        rainfall = weatherData[2]

        date, time = weatherData[0].split(' ')

        return temperature, rainfall, date, time