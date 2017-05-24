from suds.client import Client

"""
Web Client TimeLapse creates an instance of Web Client TimeLapse
"""
class WebClientTimeLapse():
    def __init__(self):
        self.client = Client('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeatherTimeLapse?wsdl')

    """
    Obtains all location names from the webclient
    """
    def getLocationNames(self):
        locations = self.client.service.getLocations()
        return locations

    """
    Obtains all timelapse data from the webclient for a specific location
    """
    def getWeatherData(self, location):
        weatherData = self.client.service.getWeather(location)
        temperature = weatherData[1]
        rainfall = weatherData[2]

        date, time = weatherData[0].split(' ')

        return temperature, rainfall, date, time