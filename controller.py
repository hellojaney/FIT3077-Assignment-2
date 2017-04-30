from gui import GUI
from webclient import WebClient
from location import Location
from weatherframe import WeatherFrame
from activelocations import ActiveLocations
from weatherframecollection import WeatherFrameCollection
from controllertimer import ControllerTimer
from locationlist import LocationList
from dropdownlist import DropDownList

"""
Controller manages the program functions including:
- tracking timer to refresh location data on screen
- creating instances of GUI, WebClient, ActiveLocations, WeatherFrameCollection
"""
class Controller:
    def __init__(self):
        self.gui = GUI("Weather Monitor")
        self.webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')

        self.active = ActiveLocations()
        self.allLocations = LocationList()
        self.wFrameCollection = WeatherFrameCollection()

    # Update data and display new data on screen
    def refreshLocations(self):
        print("Refreshing Weather Data...")
        #update loop
        for location in self.active.activeList:
            tempData = self.webClient.getWeatherData(location.getName())
            location.setTemperature(tempData[0])
            location.setRainfall(tempData[1])
            location.setTimestamp(tempData[2])
            location.setDatestamp(tempData[3])

        self.wFrameCollection.clearAllFrames()

        #display loop
        for location in self.active.activeList:
            wFrame = WeatherFrame(self.gui.frame, self.active, location.getName())
            wFrame.addData(location)
            self.wFrameCollection.addFrame(wFrame)

        print("Refresh Complete.")

    def makeLocationActive(self, locationName):
        if self.active.exists(locationName):
            print(locationName + " is already active")
            return
        locInfo = self.webClient.getWeatherData(locationName)
        location = Location(locationName, locInfo[0], locInfo[1], locInfo[2], locInfo[3])
        self.active.add(location)

        wFrame = WeatherFrame(self.gui.frame, self.active, locationName)
        wFrame.addData(location)
        self.wFrameCollection.addFrame(wFrame)


    def begin(self):
        # initialising GUI and Web Client
        locList = self.webClient.getLocationNames()

        # passing list of locations to inactiveLocations and creating optionMenu
        self.allLocations.addMulti(locList)
        optionMenu = DropDownList(self.gui.canvas, self.allLocations.getAll(), self)

        # initialise timer and start GUI
        # NOTE YOU MIGHT NOT NEED THESE PARAMETERS THEY'RE ALL OBJECT VARIABLES NOW
        newTimer = ControllerTimer(5, self.refreshLocations)
        newTimer.start()

        self.gui.startLoop()
        newTimer.cancel()

cont = Controller()
cont.begin()