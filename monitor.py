from Tkinter import *
from graphwindow import GraphWindow
from webclientmelb import WebClientMelb
from location import Location

"""
Creates a Frame() for the GUI
Takes a list of information from getAllInfo: location, timestamp, rainfall and temp
Packs the frame into the GUI
"""

class Monitor:
    def __init__(self, root, activeMonitors, locationName, viewOption):
        self.location = None
        self.activeMonitors = activeMonitors
        self.viewOption = viewOption
        self.client = WebClientMelb()
        self.createLocation(locationName)
        self.frame = Frame(root)
        self.job = self.frame.after(3000000, self.updateLocationData)
        self.frame.pack(side=TOP, anchor=NW)

        # 'declare' all text information (labels)
        self.temperatureLabel = None
        self.rainfallLabel = None
        self.datetimestampLabel = None

        self.packData()

    """
    Creates the location instance after getting data from Web Client (called from initialisation) 
    """
    def createLocation(self, locationName):
        # retrieve data from web client and create location object
        locInfo = self.client.getWeatherData(locationName)
        self.location = Location(locationName, locInfo[0], locInfo[1], locInfo[2], locInfo[3])


    """
    Packs data into the frame, this includes the text and the buttons
    """
    def packData(self):
        # blank label to create spacing
        Label(self.frame, text=" ").grid(row=0, column=0)

        Label(self.frame, text = self.location.getName(), font ="Helvetica 16 bold").grid(row=1, column=0, sticky = W)

        self.closeButton = Button(self.frame, text="x", command=lambda: self.killMonitor(self.frame))
        self.closeButton.grid(row = 1, column = 5)

        self.datetimestampLabel = Label(self.frame, text="Updated at: " + self.location.getDateStamp() + ", " + self.location.getTimeStamp(),
                                        font="Helvetica 14")
        self.datetimestampLabel.grid(row=2, column=0, sticky=W)

        if self.viewOption != "Rainfall":
            self.temperatureLabel = Label(self.frame, text="Temperature: " + str(self.location.getTemperature()) + "C", font="Helvetica 14")
            self.temperatureLabel.grid(row=3, column=0, sticky=W)
        if self.viewOption != "Temperature":
            self.rainfallLabel = Label(self.frame, text="Rainfall: " + str(self.location.getRainfall()) + "mm", font="Helvetica 14")
            self.rainfallLabel.grid(row=4, column=0, sticky=W)

        Button(self.frame, text="Show Graph", command = self.createGraph).grid(row = 5, column = 0, sticky = W)

    """
    Updates the location data from the Web Client
    """

    def updateLocationData(self):
        locInfo = self.client.getWeatherData(self.location.getName())

        # set all of the values
        self.location.setTemperature(locInfo[0])
        self.location.setRainfall(locInfo[1])
        self.location.setDatestamp(locInfo[2])
        self.location.setTimestamp(locInfo[3])
        self.refreshMonitorData()
        # reset the timer
        self.job = self.frame.after(3000000, self.updateLocationData)

    """
    Updates the information on the GUI
    """
    def refreshMonitorData(self):
        self.datetimestampLabel.config(
            text="Updated at: " + str(self.location.getTimeStamp()) + ", " + str(self.location.getDateStamp()))
        if self.viewOption != "Rainfall":
            self.temperatureLabel.config(text="Temperature: " + str(self.location.getTemperature()) + "C")

        if self.viewOption != "Temperature":
            self.rainfallLabel.config(text="Rainfall: " + str(self.location.getRainfall()) + "mm")


    """
    Destroys the monitor (called by clearAllMonitors() in MonitorCollection) WILL PROBABLY DELETE
    """
    def closeMonitor(self, frame):
        frame.pack_forget()
        frame.destroy()

    """
    Removes the frame from the GUI, called when the 'x' button is clicked
    """
    def killMonitor(self, frame):
        self.cancelUpdates()
        self.activeMonitors.remove(self.location.getName())
        frame.pack_forget()
        frame.destroy()

    """
    opens a new window to display the temperature/rainfall graph
    """
    def createGraph(self):
        graphWindow = GraphWindow(self.location.getName())


    """
    Stops the update function when the user clicks the exit button on the window.
    """
    def cancelUpdates(self):
        if self.job is not None:
            self.frame.after_cancel(self.job)
            self.job = None