from monitor import Monitor
from suds.client import Client


class WebClient:
    def __init__(self, url):
        self.client = Client(url)

    def getLocationNames(self):
        locations = []
        locations = self.client.service.getLocations()
        return locations

    # Mostly written by David Lei from forum example
    # Need to change this function so that it does not display all location frames
    def getAllMonitors(self):
        locations = self.getLocationNames()
        collection = []
        for loc in locations:
            date_time, rainfall = self.client.service.getRainfall(loc)
            date, time = date_time.split(' ')
            temp = self.client.service.getTemperature(loc)[-1]
            collection.append(Monitor(loc, temp, rainfall, time))
        return collection

