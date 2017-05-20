from gui import GUI
from clients import MelbClient
from location import Location
from monitor import Monitor
from activelocations import ActiveLocations
from monitorcollection import MonitorCollection
from controllertimer import ControllerTimer
from locationlist import LocationList
from dropdownlist import DropDownList
from viewselection import ViewSelection

"""
Controller manages the program functions including:
- tracking timer to refresh location data on screen
- creating instances of GUI, WebClient, ActiveLocations, WeatherFrameCollection
"""

class Controller:
    def __init__(self):
        self.gui = GUI("Weather Monitor")
        self.melbWeather2 = MelbClient()
        self.active = ActiveLocations()
        self.allLocations = LocationList()
        self.monitorCollection = MonitorCollection()
        self.viewOption = None


    """
    Update location data and display on the screen through the Weather Frame.
    """
    def updateLocationInfo(self):
        print("Updating Weather Data...")

        # obtain new data through web client
        for location in self.active.activeList:
            tempData = self.melbWeather2.getWeatherData(location.getName())
            #update timestamp first to correct values in temperatureHistory and rainfallHistory
            location.setTimestamp(tempData[2])
            location.setDatestamp(tempData[3])
            location.setTemperature(tempData[0])
            location.setRainfall(tempData[1])

        print("Update Complete.")

        self.refreshMonitors()

    """
    Clears all monitors from window and re-adds them with the new information
    """
    def refreshMonitors(self):
        self.monitorCollection.clearAllMonitors()
        # display new data to the weather frame
        for location in self.active.activeList:
            monitor = Monitor(self.gui.frame, self.active, location.getName())
            monitor.addData(location, self.viewOption)
            self.monitorCollection.addMonitor(monitor)


    """
    Obtains data of selected location information and displays to the Weather Frame.
    """
    def makeLocationActive(self, locationName):
        if self.viewOption == None:
            print("Select Viewing Option")
            return

        # check if location exists
        if self.active.exists(locationName):
            print(locationName + " is already active")
            return

        # retrieve data from web client
        locInfo = self.melbWeather2.getWeatherData(locationName)
        location = Location(locationName, locInfo[0], locInfo[1], locInfo[2], locInfo[3])
        self.active.add(location)

        # display data to weather frame
        wFrame = Monitor(self.gui.frame, self.active, locationName)
        wFrame.addData(location, self.viewOption)
        self.monitorCollection.addMonitor(wFrame)


    """
    Sets the view option to either: temperature, rainfall or both.
    """
    def setViewingOption(self, option):
        self.viewOption = option
        self.refreshMonitors()


    """
    Initialise Program
    """
    def begin(self):
        # initialising GUI and Web Client
        locList = self.melbWeather2.getLocationNames()

        # passing list of locations and creating optionMenu
        self.allLocations.addMulti(locList)
        DropDownList(self.gui.canvas, self.allLocations.getAll(), self)

        # initialise view selection: location, rainfall or both
        ViewSelection(self.gui.canvas, self)

        # initialise timer and start GUI
        newTimer = ControllerTimer(300, self.updateLocationInfo)
        newTimer.start()
        self.gui.startLoop()
        newTimer.cancel()


"""
create controller and start the program
"""
app = Controller()
app.begin()