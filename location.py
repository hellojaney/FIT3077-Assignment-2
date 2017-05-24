from subject import Subject
from updatetimer import UpdateTimer
from webclientmelb import WebClientMelb
from webclienttimelapseadapter import WebClientTimelapseAdapter
from webclienttimelapse import WebClientTimeLapse
from temperature import Temperature
from rainfall import Rainfall

"""
Location Class holds information relevant to the location.
    Takes in the location name, temperature, rainfall and timestamp obtained from the Web Client.
    Creates and holds a temperature and rainfall instance.
    Keeps location name, timestamp and datestamp as an attribute.
"""

class Location(Subject):
    def __init__(self, name, service, view, data, caller):
        Subject.__init__(self)

        self.observers = []
        self.name = name
        self.caller = caller
        self.temperature = Temperature(None)
        self.rainfall = Rainfall(None)
        self.timestamp = None
        self.datestamp = None

        self.serviceType = service
        self.viewType = view
        self.dataType = data

        self.client = None
        self.timer = None
        self.setupClient()


    def register(self, newObserver):
        self.observers.append(newObserver)


    def unregister(self, deleteObserver):
        self.observers.remove(deleteObserver)


    def notifyObservers(self):
        for observer in self.observers:
            observer.update(self.temperature.getTemperature(), self.rainfall.getAmount(), self.datestamp, self.timestamp)


    def setupClient(self):
        if self.serviceType == "MelbWeather2":
            # set up client and timer
            self.client = WebClientMelb()
            self.timer = UpdateTimer(300, self.updateData)

            # update data for the first time, then start the timer
            self.updateData()
            self.timer.start()
        elif self.serviceType == "WeatherTimeLapse":
            # set up client and timer
            incompatibleClient = WebClientTimeLapse()
            self.client = WebClientTimelapseAdapter(incompatibleClient)
            self.timer = UpdateTimer(2, self.updateData)

            # update data for the first time, then start the timer
            self.updateData()
            self.timer.start()
        else:
            print "Web Client Setup Error: web client name not found"


    """
    Updates data of the location's attributes from the WebClient
    """
    def updateData(self):
        locInfo = self.client.getWeatherData(self.name)
        self.setTemperature(locInfo[0])
        self.setRainfall(locInfo[1])
        self.setDatestamp(locInfo[2])
        self.setTimestamp(locInfo[3])
        self.notifyObservers()

    """
    Removes the location object from the location collection when a monitor is shut down
    """
    def removeLocation(self):
        self.caller.removeFromCollection(self)

    """
    Stops the timer by calling cancel()
    """
    def stopTimer(self):
        self.timer.cancel()

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