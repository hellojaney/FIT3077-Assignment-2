from webclient import WebClient


class WebClientTimelapseAdapter(WebClient):
    def __init__(self, timelapseClient):
        WebClient.__init__(self)
        self.timelapseClient = timelapseClient
        self.currentWeatherData = []


    def getLocationNames(self):
        # get the list of locations by calling the function from the timelapse client
        return self.timelapseClient.getLocationNames()


    def getWeatherData(self, location):
        # the the weather data by calling the function from the timelapse client
        unconvertedWeatherData = self.timelapseClient.getWeatherData(location)

        # convert Kelvin to Celsius
        temperature = float(unconvertedWeatherData[0]) - 273.15

        # convert centimeters to millimeters
        rainfall = float(unconvertedWeatherData[1]) * 10
        rainfall = self.formatNoneData(rainfall)

        # date and time remains the same
        date, time = unconvertedWeatherData[2], unconvertedWeatherData[3]

        return temperature, rainfall, date, time