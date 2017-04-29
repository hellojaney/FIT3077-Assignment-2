from gui import GUI
from webclient import WebClient
from location import Location
from weatherframe import WeatherFrame
from activelocations import ActiveLocations


#set up GUI and Web Client
gui = GUI("Weather Monitor")
webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')

#test
active = ActiveLocations()
loc = Location("Springvale", 10, 0.1, "now", "now")
active.add(loc)
wFrame = WeatherFrame(gui.root)
wFrame.addData(loc)

gui.startLoop()