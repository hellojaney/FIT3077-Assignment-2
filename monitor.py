from location import Location
from rainfall import Rainfall
from temperature import Temperature

class Monitor:
    def __init__(self, locationName, tempAmount, rainAmount, timestamp):
        temperature = Temperature(tempAmount)
        rainfall = Rainfall(rainAmount)
        self.location = Location(locationName, temperature, rainfall)
        self.timestamp = timestamp


    def getLocation(self):
        return self.location


    def getTimestamp(self):
        return self.timestamp


    def setTemp(self, newTemp):
        self.location.setTemp(newTemp)


    def setRainfall(self, newRain):
        self.location.setRain(newRain)


    def setTimestamp(self, newTimestamp):
        self.timestamp = newTimestamp

    def getAllInfo(self):
        list = []

        #LOCATION NAME AND TIMESTAMP
        list.append(self.location.getName())
        list.append("Updated at: " + str(self.timestamp))

        #FORMAT TEMPERATURE
        temp = str(self.getLocation().getTemp().getCelcius())
        if temp != "-":
            temp += "C"
        list.append("Temperature: " + temp)

        #FORMAT RAINFALL
        temp = str(self.getLocation().getRain().getAmount())
        if temp != "-":
            temp += "mm"
        list.append("Rainfall: " + temp)

        return list