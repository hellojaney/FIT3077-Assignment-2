from Tkinter import *
from datetime import datetime
from monitor import Monitor

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

"""
A Tkinter window which holds the rainfall and temperature graph that will be  
updated every 2 seconds from the MelbourneWeatherTimelapse Web Service. 

Some of this code is based on:
https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/
"""

class MonitorGraph(Monitor):

    def __init__(self, location, caller):
        Monitor.__init__(self, location, caller)

        self.locationName = location.getName()

        # create data lists
        self.rainData = []
        self.tempData = []
        self.timeData = []

        # set up window and main plot
        self.graphRoot = Tk()
        self.graphRoot.title('Rainfall and Temperature Graph for ' + self.locationName)
        self.fig = Figure(figsize=(5, 5), dpi=100)

        # create axis
        self.axis = self.fig.add_subplot(111)


        # add plot lines to the axis
        self.tempLine = self.axis.plot(self.timeData, self.tempData)
        self.rainLine = self.axis.plot(self.timeData, self.rainData)

        # create canvas object
        self.canvas = FigureCanvasTkAgg(self.fig, self.graphRoot)

        self.formatAxis()
        self.showCanvas()
        self.openGraph()

    """
    Adds the legend, x axis and y axis to the plot
    Restricts the line colours to orange and bluegr
    """
    def formatAxis(self):
        #self.axis.set_color_cycle(['blue', 'orange'])
        self.axis.set_prop_cycle('color', ['red', 'blue'])
        self.axis.legend(['Temperature', 'Rainfall'], loc='upper left')
        self.setLegendColours()

        self.axis.set_xlabel('Time (date hour:minute)')
        self.axis.set_ylabel('Temperature / Rainfall (C / mm)')

    """
    Fixes the colours for the legend (Temperature = red, Rainfall = blue)
    """
    def setLegendColours(self):
        legend = self.axis.get_legend()
        legend.legendHandles[0].set_color('red')
        legend.legendHandles[1].set_color('blue')


    """
    Packs the plot to the window (graphRoot)
    """
    def showCanvas(self):
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)


    """
    Starts the timer that calls updateData, then starts the mainloop
    When the window (graphRoot) is closed, the timer is stopped
    """
    def openGraph(self):
        self.graphRoot.mainloop()

    """
    Stops the update function when the user clicks the exit button on the window.
    WILL MOST LIKELY HAVE TO DELETE THIS
    """
    def cancelUpdates(self):
        pass



    """
    Retrieves new data from the TimeLapse Web Client and updates the temperature and rainfall data lists
    """
    def update(self, temperature, rainfall, datestamp, timestamp):
        # update the parent class' variables
        self.temperature = temperature
        self.rainfall = rainfall
        self.datestamp = datestamp
        self.timestamp = timestamp

        # update the data list for the graph
        self.tempData.append(self.temperature)
        self.rainData.append(self.rainfall)

        # get date and time data and convert it to datetime format, then store in data list
        formattedTime = self.datestamp + " " + self.timestamp
        formattedTime = datetime.strptime(formattedTime, '%d/%m/%Y %H:%M:%S')
        self.timeData.append(formattedTime)

        self.clearGraph()
        self.plotLines()

    """
    Removes both temperature and rainfall lines from the graph
    """
    def clearGraph(self):
        l = self.tempLine.pop(0)
        l.remove()
        l = self.rainLine.pop(0)
        l.remove()

    """
    Adds temperature and rainfall lines to the graph
    """
    def plotLines(self):
        # update lines with new data
        self.tempLine = self.axis.plot(self.timeData, self.tempData)
        self.rainLine = self.axis.plot(self.timeData, self.rainData)
        self.canvas.show()