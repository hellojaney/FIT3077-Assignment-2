from Tkinter import *
from weatherframe import WeatherFrame
from activemonitors import ActiveMonitors


"""
Adds monitor by taking in an info list (from getAllInfo) and adds weatherframe to GUI.
"""

class GUI:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)
        self.weatherFrameList = []

        self.active = ActiveMonitors()


    def addMonitor(self, infoList):
        wFrame = WeatherFrame(self.root, infoList[0])
        wFrame.addData(infoList)
        self.weatherFrameList.append(wFrame)

    def clearMonitor(self, id):
        print(len(self.weatherFrameList))
        for wFrame in self.weatherFrameList:
            if wFrame.id == id:
                wFrame.removeData()
                self.weatherFrameList.remove(wFrame)
        print (len(self.weatherFrameList))


    def startLoop(self):
        self.root.mainloop()