from gui import GUI
from activelocations import ActiveLocations
from inactivelocations import InactiveLocations
from webclient import WebClient


class GUIController():
    def __init__(self):
        self.inactive = InactiveLocations()
        self.active = ActiveLocations()
        self.webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')
        self.gui = GUI("Weather Monitor", self.inactive.getAll())
        self.guiFrame = self.gui.frame


    def start(self):
        locationList = self.webClient.getLocationNames()
        self.inactive.addMulti(locationList)
        self.gui.startLoop()