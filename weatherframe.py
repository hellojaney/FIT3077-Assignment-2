from Tkinter import *
from graphwindow import GraphWindow

"""
Creates a Frame() for the GUI
Takes a list of information from getAllInfo: location, timestamp, rainfall and temp
Packs the frame into the GUI
"""

class WeatherFrame:
    def __init__(self, root, activeLocations, locationName):
        self.id = locationName
        self.frame = Frame(root)
        self.frame.pack(side=TOP, anchor=NW)
        self.activeLocations = activeLocations
        self.windowOpen = False

    # packs data into frame
    def addData(self, location, viewOption):
        # blank label to create spacing
        Label(self.frame, text=" ").grid(row=0, column=0)

        # create the title and 'x' button, the first item in the list is the location name (title)
        Label(self.frame, text = location.getName(), font ="Helvetica 16 bold").grid(row=1, column=0, sticky = W)
        self.closeButton = Button(self.frame, text="x", command=lambda: self.killFrame(self.frame)).grid(row = 1, column = 5)
        Label(self.frame, text="Updated at: " + location.getDateStamp() + ", " + location.getTimeStamp(),
              font="Helvetica 14").grid(row=2, column=0, sticky=W)

        # view options
        if viewOption == "Temperature":
            Label(self.frame, text="Temperature: " + str(location.getTemperature()) + "C", font="Helvetica 14").grid(
                row=3, column=0, sticky=W)
        elif viewOption == "Rainfall":
            Label(self.frame, text="Rainfall: " + str(location.getRainfall()) + "mm", font="Helvetica 14").grid(row=3,
                                                                                                                column=0,
                                                                                                                sticky=W)
        else:
            Label(self.frame, text="Temperature: " + str(location.getTemperature()) + "C", font="Helvetica 14").grid(
                row=3, column=0, sticky=W)
            Label(self.frame, text="Rainfall: " + str(location.getRainfall()) + "mm", font="Helvetica 14").grid(row=4,
                                                                                                                column=0,
                                                                                                                sticky=W)
        Button(self.frame, text="Show Graph", command = self.createGraph).grid(row = 5, column = 0, sticky = W)


    # only removes the frame from the GUI, doesn't delete the location from active locations
    # this is called when the locations are refreshed
    def closeFrame(self, frame):
        frame.pack_forget()
        frame.destroy()


    # removes the frame from the GUI and delete's location
    # this is called when the X button is clicked
    def killFrame(self, frame):
        self.activeLocations.removeLocation(self.id)
        frame.pack_forget()
        frame.destroy()

    """
    opens a new window to display the temperature/rainfall graph
    """
    def createGraph(self):
        #test data to see if it goes through, change to actual data later
        self.windowOpen = True
        print "Rain and temperature graph opened"
        graphWindow = GraphWindow(self.id, [1, 2, 3, 4, 5], [11, 5, 3, 9, 2], [5, 8, 1, 1, 10])
        self.windowOpen = False