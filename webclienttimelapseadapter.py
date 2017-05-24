from webclient import WebClient

"""
FILL THIS OUT YOU FUCKWIT

"""
class WebClientTimelapseAdapter(WebClient):
    def __init__(self, timelapseClient):
        WebClient.__init__(self)
        self.timelapseClient = timelapseClient
        self.currentWeatherData = []

    """
    Obtains all Location Names from the web client
    """
    def getLocationNames(self):
        # get the list of locations by calling the function from the timelapse client
        return self.timelapseClient.getLocationNames()

    """
    Obtains all Weather Data from the web client for a specfic location
    """
    def getWeatherData(self, location):
        # the the weather data by calling the function from the timelapse client
        unconvertedWeatherData = self.timelapseClient.getWeatherData(location)

        # convert Kelvin to Celsius
        temperature = float(unconvertedWeatherData[0]) - 273.15

        # convert centimeters to millimeters, but check that the information is valid first
        rainfall = unconvertedWeatherData[1]
        rainfall = self.formatNoneData(rainfall)
        if rainfall != "-":
            rainfall = float(unconvertedWeatherData[1]) * 10

        # date and time remains the same
        date, time = unconvertedWeatherData[2], unconvertedWeatherData[3]

        return temperature, rainfall, date, time