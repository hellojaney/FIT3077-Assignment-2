from gui import GUI
from webclientmelb import WebClientMelb
from monitor import Monitor
from monitorcollection import MonitorCollection
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
        self.melbWeather2 = WebClientMelb()
        self.allLocations = LocationList()
        self.monitorCollection = MonitorCollection()
        self.viewOption = None

    """
    Creates a text monitor given a location name
    """
    def createMonitor(self, locationName):
        if self.viewOption == None:
            print("Select Viewing Option")
            return

        # check if location exists
        if self.monitorCollection.exists(locationName, self.viewOption):
            print("Monitor looking at " + locationName + "'s " + self.viewOption + " is already active")
            return

        # display data to weather frame
        monitor = Monitor(self.gui.frame, self.monitorCollection, locationName, self.viewOption)
        self.monitorCollection.addMonitor(monitor)

    """
    Sets the view option to either: temperature, rainfall or both.
    """
    def setViewingOption(self, option):
        self.viewOption = option


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

        self.gui.startLoop()


"""
create controller and start the program
"""
app = Controller()
app.begin()