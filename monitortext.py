from Tkinter import *

from location import Location
from monitor import Monitor

"""
Creates a Frame() for the GUI
Takes a list of information from getAllInfo: location, timestamp, rainfall and temp
Packs the frame into the GUI
"""

class MonitorText(Monitor):
    def __init__(self, location, root, caller):
        Monitor.__init__(self, location, caller)

        self.frame = Frame(root)
        self.frame.pack(side=TOP, anchor=NW)

        # 'declare' all text information (labels)
        self.temperatureLabel = None
        self.rainfallLabel = None
        self.datetimestampLabel = None

        self.packData()

    def update(self, temperature, rainfall, datestamp, timestamp):
        self.temperature = temperature
        self.rainfall = rainfall
        self.datestamp = datestamp
        self.timestamp = timestamp

        self.refreshMonitorData()


    """
    Packs data into the frame, this includes the text and the buttons
    """
    def packData(self):
        # blank label to create spacing
        Label(self.frame, text=" ").grid(row=0, column=0)

        Label(self.frame, text = self.location.getName(), font ="Helvetica 16 bold").grid(row=1, column=0, sticky = W)

        self.closeButton = Button(self.frame, text="x", command=lambda: self.closeMonitor(self.frame))
        self.closeButton.grid(row=1, column=5)

        Label(self.frame, text = "Viewing " + self.location.dataType + " from " + self.location.serviceType, font="Helvetic 14 italic").grid(row=2, column=0, sticky = W)

        self.datetimestampLabel = Label(self.frame, text="Updated at: " + self.location.getDateStamp() + ", " + self.location.getTimeStamp(),
                                        font="Helvetica 14")
        self.datetimestampLabel.grid(row=3, column=0, sticky=W)
        print (self.location.dataType)
        if self.location.viewType != "Rainfall":
            self.temperatureLabel = Label(self.frame, text="Temperature: " + str(self.location.getTemperature()) + "C", font="Helvetica 14")
            self.temperatureLabel.grid(row=4, column=0, sticky=W)
        if self.location.dataType != "Temperature":
            self.rainfallLabel = Label(self.frame, text="Rainfall: " + str(self.location.getRainfall()) + "mm", font="Helvetica 14")
            self.rainfallLabel.grid(row=5, column=0, sticky=W)


    """
    Updates the information on the GUI
    """
    def refreshMonitorData(self):
        self.datetimestampLabel.config(
            text="Updated at: " + str(self.location.timestamp) + ", " + str(self.datestamp))
        if self.location.dataType != "Rainfall":
            self.temperatureLabel.config(text="Temperature: " + str(self.temperature) + "C")

        if self.location.dataType != "Temperature":
            self.rainfallLabel.config(text="Rainfall: " + str(self.rainfall) + "mm")


    """
    Removes the frame from the GUI, called when the 'x' button is clicked
    """
    def closeMonitor(self, frame):
        self.remove()
        frame.pack_forget()
        frame.destroy()
