from Tkinter import *
from weatherframe import WeatherFrame


"""
Adds monitor by taking in an info list (from getAllInfo) and adds weatherframe to GUI.
"""

class GUI:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)

    def clearLocations(self):
        for wFrame in self.weatherFrameList:
            wFrame.removeData()
            self.weatherFrameList.remove(wFrame)

    def startLoop(self):
        self.root.mainloop()