from gui import GUI
from webclient import WebClient
from activemonitors import ActiveMonitors
import time

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

#refreshing monitors: not too sure if there is a more efficient way to do this???
while True:
    if active.list == []:
        break
    else:
        currentTime = time.localtime(time.time())
        if active.checkTimer(active.timer, currentTime) == True:
            for monitor in active.list:
                gui.addMonitor(monitor.getAllInfo())

