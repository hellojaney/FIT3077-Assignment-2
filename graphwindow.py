from timelapseclient import TimeLapseClient
from controllertimer import ControllerTimer

from Tkinter import *
from datetime import datetime

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

class GraphWindow:

    def __init__(self, locationName):

        self.locationName = locationName
        self.client = TimeLapseClient()
        self.timer = ControllerTimer(2, self.updateData)

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
        self.axis.set_color_cycle(['blue', 'orange'])
        self.axis.legend(['Rainfall', 'Temperature'], loc='upper left')
        self.axis.set_xlabel('t')
        self.axis.set_ylabel('C / mm')


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
        self.timer.start()
        self.graphRoot.mainloop()
        self.timer.cancel()

    """
    Retrieves new data from the TimeLapse Web Client and updates the temperature and rainfall data lists
    """
    def updateData(self):
        newData = self.client.getWeatherTimeLapse(self.locationName)

        # convert Kelvin to Celsius, then add to temperature data
        temperature = float(newData[0])
        temperature -= 273.15
        self.tempData.append(temperature)

        # convert centimeters to millimeters asnd add to rainfall data
        rainfall = float(newData[1])
        rainfall = rainfall * 10
        self.rainData.append(rainfall)

        # add new time data
        formattedTime = newData[2] + " " + newData[3]
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