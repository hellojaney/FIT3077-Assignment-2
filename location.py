
from rainfall import Rainfall
from temperature import Temperature

"""
Takes in the location name, temperature, rainfall and timestamp.
Creates and holds a location instance.
"""

class Location:
    def __init__(self, locationName, tempAmount, rainAmount, timestamp, datestamp):
        temperature = Temperature(tempAmount)
        rainfall = Rainfall(rainAmount)
        self.name = locationName
        self.temperature = Temperature(tempAmount)
        self.rainfall = Rainfall(rainAmount)
        self.timestamp = timestamp
        self.datestamp = datestamp


    def getName(self):
        return self.name

    def getTimeStamp(self):
        return self.timestamp

    def getDateStamp(self):
        return self.datestamp

    def getTemperature(self):
        return self.temperature.getCelcius()

    def getRainfall(self):
        return self.rainfall.getAmount()


    def setTemperature(self, newTemp):
        self.temperature = newTemp

    def setRainfall(self, newRain):
        self.rainfall = newRain

    def setTimestamp(self, newTimestamp):
        self.timestamp = newTimestamp