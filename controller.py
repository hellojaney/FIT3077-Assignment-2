from gui import GUI
from webclient import WebClient
from activemonitors import ActiveMonitors

#set up GUI and Web Client
gui = GUI("Weather Monitor")
webClient = WebClient('http://viper.infotech.monash.edu.au:8180/axis2/services/MelbourneWeather2?wsdl')

#create list of active monitors, for now all monitors are loaded
active = ActiveMonitors()
active.addMulti(webClient.getAllMonitors())

#adding each monitor to the GUI
for monitor in active.list:
    gui.addMonitor(monitor.getAllInfo())

gui.startLoop()