"""
Holds Temperature Information for a Location
"""

class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius


    def getTemperature(self):
        return self.celcius


    def setTemperature(self, newTemperature):
        self.celcius = newTemperature
