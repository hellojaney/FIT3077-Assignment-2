from rainfall import Rainfall
from temperature import Temperature


class Location:
    def __init__(self, name, temperature, rainfall):
        self.name = name
        self.temperature = temperature
        self.rainfall = rainfall

    def getName(self):
        return self.name

    def getTemp(self):
        return self.temperature

    def getRain(self):
        return self.rainfall

    def setTemp(self, newTemp):
        self.temperature.setCelcius(newTemp)

    def setRain(self, newRain):
        self.rainfall.setAmount(newRain)