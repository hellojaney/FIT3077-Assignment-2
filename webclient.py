from suds.client import Client

class WebClient:
    def __init__(self, url):
        self.client = Client(url)

    #NOT IN USE AT THE MOMENT
    def getLocationNames(self):
        locations = []
        locations = self.client.service.getLocations()
        return locations


    #retrieves data associated with location
    def getWeatherData(self, location):
        locationData = []

        temperature = self.client.service.getTemperature(location)[-1]
        locationData.append(temperature)

        date_time, rainfall = self.client.service.getRainfall(location)
        locationData.append(rainfall)

        date, time = date_time.split(' ')
        locationData.append(date)
        locationData.append(time)

        return locationData