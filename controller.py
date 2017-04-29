from gui import GUI
from webclient import WebClient
from location import Location
from weatherframe import WeatherFrame
from activelocations import ActiveLocations
from weatherframecollection import WeatherFrameCollection
from timer import ControllerTimer

def refreshLocations(active, wFrameCollection, webClient):
    tempData = []
    #update loop
    for location in active.activeList:
        tempData = webClient.getWeatherData(location.getName())
        location.setCelcius(tempData[0])
        location.setRainfall(tempData[1])
        location.setTimestamp(tempData[2])
        location.setDatestamp(tempData[3])

    wFrameCollection.clearAllFrames()

    #display loop
    for location in active.activeList:
        wFrame = WeatherFrame(gui.root, active, location.getName())
        wFrame.addData(location)
        wFrameCollection.addFrame(wFrame)



#set up GUI and Web Client
gui = GUI("Weather Monitor")
webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')

######## START TEST DATA ########

active = ActiveLocations(gui)
wFrameCollection =  WeatherFrameCollection()

locList = webClient.getLocationNames()
locInfo = []
print "Loading weather information..."
for loc in locList:
    locInfo = webClient.getWeatherData(loc)
    location = Location(loc, locInfo[0], locInfo[1], locInfo[2], locInfo[3])
    active.add(location)
    wFrame = WeatherFrame(gui.root, active, loc)
    wFrame.addData(location)
    wFrameCollection.addFrame(wFrame)
print "Loaded."

######## END TEST DATA ########


newTimer = ControllerTimer(3, lambda: refreshLocations(active, wFrameCollection, webClient))
newTimer.start()

gui.startLoop()

newTimer.cancel()