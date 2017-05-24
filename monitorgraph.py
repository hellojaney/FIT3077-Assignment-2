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

        # create data lists
        self.rainData = []
        self.tempData = []
        self.timeData = []

        # set up window and main plot
        self.graphRoot = Tk()
        self.graphRoot.title('Rainfall and Temperature Graph for ' + self.location.getName())
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.fig.suptitle('Rainfall and Temperature Graph for ' + self.location.getName())

        # create axis
        self.axis = self.fig.add_subplot(111)


        # add plot lines to the axis
        self.tempLine = self.axis.plot(self.timeData, self.tempData)
        self.rainLine = self.axis.plot(self.timeData, self.rainData)

        # create canvas object
        self.canvas = FigureCanvasTkAgg(self.fig, self.graphRoot)

        self.formatAxis()
        self.showCanvas()

    """
    Adds the legend, x axis and y axis to the plot
    Restricts the line colours to orange and bluegr
    """
    def formatAxis(self):
        legendItems = []
        colourItems = []
        if self.location.dataType != 'Rainfall':
            legendItems.append('Temperature')
            colourItems.append('red')

        if self.location.dataType != 'Temperature':
            legendItems.append('Rainfall')
            colourItems.append('blue')

        self.axis.set_prop_cycle('color', colourItems)
        self.axis.legend(legendItems, loc='upper left')
        self.setLegendColours()

        self.axis.set_xlabel('Time (date hour:minute)')
        if self.location.dataType == 'Temperature':
            self.axis.set_ylabel('Temperature (C)')
        elif self.location.dataType == 'Rainfall':
            self.axis.set_ylabel('Rainfall (mm)')
        else:
            self.axis.set_ylabel('Temperature / Rainfall (C / mm)')

    """
    Fixes the colours for the legend (Temperature = red, Rainfall = blue)
    """
    def setLegendColours(self):
        legend = self.axis.get_legend()
        if self.location.dataType == 'Temperature':
            legend.legendHandles[0].set_color('red')
        elif self.location.dataType == 'Rainfall':
            legend.legendHandles[0].set_color('blue')
        else:
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
        self.graphRoot.protocol("WM_DELETE_WINDOW", self.shutDownMonitor)
        self.graphRoot.mainloop()


    """
    Calls the remove function for the monitor (which deletes the monitor and the associated location from their collection.
    Then destroys (closes) the window.
    """
    def shutDownMonitor(self):
        self.remove()
        self.graphRoot.destroy()

    """
    Retrieves new data from the TimeLapse Web Client and updates the temperature and rainfall data lists
    """
    def update(self, temperature, rainfall, datestamp, timestamp):
        # update the parent class' variables
        self.temperature = temperature
        self.rainfall = rainfall
        self.datestamp = datestamp
        self.timestamp = timestamp

        # update the temperature and rainfall data lists for the graph
        self.tempData.append(self.temperature)
        self.rainData.append(self.rainfall)

        # get date and time data and convert it to datetime format, then store in data list
        formattedTime = self.datestamp + " " + self.timestamp
        formattedTime = datetime.strptime(formattedTime, '%d/%m/%Y %H:%M:%S')
        self.timeData.append(formattedTime)

        # clear the graph and plot the lines with the new data
        self.clearGraph()
        self.plotLines()

    """
    Removes both temperature and rainfall lines from the graph
    """
    def clearGraph(self):
        if self.location.dataType != 'Rainfall':
            l = self.tempLine.pop(0)
            l.remove()
        if self.location.dataType != 'Temperature':
            l = self.rainLine.pop(0)
            l.remove()


    """
    Adds temperature and rainfall lines to the graph
    """
    def plotLines(self):
        # update lines with new data
        if self.location.dataType != 'Rainfall':
            self.tempLine = self.axis.plot(self.timeData, self.tempData)
        if self.location.dataType != 'Temperature':
            self.rainLine = self.axis.plot(self.timeData, self.rainData)
        self.canvas.show()