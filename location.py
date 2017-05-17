from rainfall import Rainfall
from temperature import Temperature

"""
Takes in the location name, temperature, rainfall and timestamp.
Creates and holds a temperature and rainfall instance.
Keeps location name, timestamp and datestamp as an attribute.
"""

class Location:
    def __init__(self, locationName, tempAmount, rainAmount, timestamp, datestamp):
        self.name = locationName
        self.temperature = Temperature(tempAmount)
        self.rainfall = Rainfall(rainAmount)
        self.temperatureHistory = {}
        self.rainfallHistory = {}
        self.timestamp = timestamp
        self.datestamp = datestamp

    """
    Getters
    """
    def getName(self):
        return self.name

    def getTemperature(self):
        return self.temperature.getTemperature()

    def getRainfall(self):
        return self.rainfall.getAmount()

    def getTimeStamp(self):
        return self.timestamp

    def getDateStamp(self):
        return self.datestamp

    def getTemperatureHistory(self):
        return self.temperatureHistory

    def getRainfallHistory(self):
        return self.rainfallHistory


    """
    Setters
    """
    def setTemperature(self, newTemperature):
        self.temperature.setTemperature(newTemperature)

    def setRainfall(self, newAmount):
        self.rainfall.setAmount(newAmount)

    def setTimestamp(self, newTimestamp):
        self.timestamp = newTimestamp

    def setDatestamp(self, newDatestamp):
        self.datestamp = newDatestamp