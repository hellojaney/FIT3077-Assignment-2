from monitor import Monitor
from suds.client import Client


class WebClient:
    def __init__(self, url):
        self.client = Client(url)

    #NOT IN USE AT THE MOMENT
    def getLocationNames(self):
        locations = []
        locations = self.client.service.getLocations()
        return locations

    # Mostly written by David Lei from forum example
    # Need to change this function so that it does not display all location frames
    def getMonitors(self, locations):
        collection = []
        for loc in locations:
            date_time, rainfall = self.client.service.getRainfall(loc)
            date, time = date_time.split(' ')
            temp = self.client.service.getTemperature(loc)[-1]
            collection.append(Monitor(loc, temp, rainfall, time, date))
        return collection


