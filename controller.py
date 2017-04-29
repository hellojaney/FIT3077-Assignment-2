from gui import GUI
from webclient import WebClient
from location import Location
from weatherframe import WeatherFrame
from activelocations import ActiveLocations
from weatherframecollection import WeatherFrameCollection
from timer import ControllerTimer

def refreshLocations(active, wFrameCollection, webClient):
    wFrameCollection.clearAllFrames()
    tempData = []
    for location in active.activeList:
        tempData = webClient.getWeatherData(location.getName())
        location.setCelcius(tempData[0])
        location.setRainfall(tempData[1])
        location.setTimestamp(tempData[2])
        location.setDatestamp(tempData[3])
        wFrame = WeatherFrame(gui.root, active, location.getName())
        wFrame.addData(location)
        wFrameCollection.addFrame(wFrame)
        print("refresh's: " + str(active.activeList))


#set up GUI and Web Client
gui = GUI("Weather Monitor")
webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')
print webClient.getLocationNames()

######## START TEST DATA ########
active = ActiveLocations(gui)
wFrameCollection =  WeatherFrameCollection()


loc = Location("Laverton", 10, 0.1, "now", "now")
active.add(loc)

wFrame = WeatherFrame(gui.root, active, "Laverton")
wFrame.addData(loc)
wFrameCollection.addFrame(wFrame)


loc = Location("Cranbourne", 10, 0.1, "now", "now")
active.add(loc)

wFrame = WeatherFrame(gui.root, active, "Cranbourne")
wFrame.addData(loc)
wFrameCollection.addFrame(wFrame)

######## END TEST DATA ########


newTimer = ControllerTimer(3, lambda: refreshLocations(active, wFrameCollection, webClient))
newTimer.start()

gui.startLoop()

newTimer.cancel()