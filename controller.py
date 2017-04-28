from gui import GUI
from webclient import WebClient
from location import Location
from weatherframe import WeatherFrame


#set up GUI and Web Client
gui = GUI("Weather Monitor")
webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')

#test
loc = Location("Springvale", 10, 0.1, "now", "now")
wFrame = WeatherFrame(gui.root, "Spring")
wFrame.addData(loc)

gui.startLoop()