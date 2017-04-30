"""
Holds Temperature Information for a Location
"""

class Temperature:
    def __init__(self, celcius):
        self.temperature = celcius


    def getTemperature(self):
        return self.temperature


    def setTemperature(self, newTemperature):
        self.temperature = newTemperature
