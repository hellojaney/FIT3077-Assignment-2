from gui import GUI
from locationcollection import LocationCollection
from monitorcollection import MonitorCollection
from webclientmelb import WebClientMelb
from selector import Selector
from applybutton import ApplyButton
import sys

"""
INSERT 
"""
class Controller:
    def __init__(self):
        self.gui = GUI("Weather Monitor")
        self.melbWeather2 = WebClientMelb()
        self.monitorCollection = MonitorCollection(self)
        self.locationCollection = LocationCollection(self)

        self.locationSelection = None
        self.serviceSelection = None
        self.viewSelection = None
        self.dataSelection = None

    """
    
    """
    def createMonitor(self):
        location = self.locationCollection.createLocation(self.locationSelection, self.serviceSelection, self.viewSelection, self.dataSelection)

        if location is None:
            print "A monitor for " + self.locationSelection + " using " + self.serviceSelection + " to view its " + self.dataSelection + " as a " + self.viewSelection +  " is already active."
            return

        if self.viewSelection == "Text":
            self.monitorCollection.createTextMonitor(location, self.gui.frame)

        elif self.viewSelection == "Graph":
            self.monitorCollection.createGraphMonitor(location)

        else:
            print "Error Creating Monitor: selected data view (temperature/rainfall/both) was not found."

    """
    Sets the selector values when an option is selected from a selector list
    """
    def setSelectorValues(self, option, selectorType):
        if selectorType == "Service":
            self.serviceSelection = option
        elif selectorType == "View":
            self.viewSelection = option
        elif selectorType == "Data":
            self.dataSelection = option
        elif selectorType == "Location":
            self.locationSelection = option
        else:
            print "Selector Error: could not set selector value for " + str(selectorType)


    """
    Check that all other selector values have been set to something when location is selected, 
        - returns True if all have been selected, false otherwise.
    """
    def allValuesSelected(self):
        allSelected = True

        if self.serviceSelection is None:
            print "Selection Error: select which web service to use (1st list)"
            allSelected = False

        if self.viewSelection is None:
            print "Selection Error: select how the data should be represented (2nd list)"
            allSelected = False

        if self.dataSelection is None:
            print "Selection Error: select which data should represented (3rd list)"
            allSelected = False

        if self.locationSelection is None:
            print "Selection Error: select which location to be viewed (4th list)"
            allSelected = False

        return allSelected


    def applyOptions(self):
        if self.allValuesSelected():
            self.createMonitor()



    """
    Set up elements and start the GUI/program
    """
    def begin(self):
        # create lists of options for each drop down selector
        serviceOptions = ["---- Select a Service ----", "MelbWeather2", "WeatherTimeLapse"]
        locationOptions = ["---- Select a Location ----"] + self.melbWeather2.getLocationNames()
        viewOptions = ["---- Select a View ----", "Text", "Graph"]
        dataOptions = ["---- Select Data ----", "Temperature", "Rainfall", "Temperature and Rainfall"]

        # set up the drop down selectors by creating their objects
        Selector(self.gui.canvas, serviceOptions, self, "Service", 0)
        Selector(self.gui.canvas, viewOptions, self, "View", 1)
        Selector(self.gui.canvas, dataOptions, self, "Data", 2)
        Selector(self.gui.canvas, locationOptions, self, "Location", 3)
        ApplyButton(self.gui.canvas, self, 4)

        #open the gui
        self.gui.startLoop()

"""
create controller and start the program
"""
app = Controller()
app.begin()
sys.exit(0)