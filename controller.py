from gui import GUI
from webclient import WebClient
from location import Location
from weatherframe import WeatherFrame
from activelocations import ActiveLocations
from weatherframecollection import WeatherFrameCollection
from timer import ControllerTimer
from inactivelocations import InactiveLocations
from dropdownlist import DropDownList

"""
Controller manages the program functions including:
- tracking timer to refresh location data on screen
- creating instances of GUI, WebClient, ActiveLocations, WeatherFrameCollection
"""

# Update data and display new data on screen
def refreshLocations(active, wFrameCollection, webClient):
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
        wFrame = WeatherFrame(gui.frame, active, location.getName())
        wFrame.addData(location)
        wFrameCollection.addFrame(wFrame)


# initialising GUI and Web Client
gui = GUI("Weather Monitor")
webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')


######## START TEST DATA ########

active = ActiveLocations()
inactive = InactiveLocations()
wFrameCollection =  WeatherFrameCollection()

locList = webClient.getLocationNames()
locInfo = []
print("Loading weather information...")

# passing list of locations to inactiveLocations and creating optionMenu
inactive.addMulti(locList)
optionMenu = DropDownList(inactive.getAll())


"""
for loc in locList:
    locInfo = webClient.getWeatherData(loc)
    location = Location(loc, locInfo[0], locInfo[1], locInfo[2], locInfo[3])
    active.add(location)
    wFrame = WeatherFrame(gui.frame, active, loc)
    wFrame.addData(location)
    wFrameCollection.addFrame(wFrame)
    """
print("Loaded.")



######## END TEST DATA ########


# initialise timer and start GUI
newTimer = ControllerTimer(3, lambda: refreshLocations(active, wFrameCollection, webClient))
newTimer.start()
gui.startLoop()
newTimer.cancel()