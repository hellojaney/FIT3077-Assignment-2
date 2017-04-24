from Tkinter import *
from weatherframe import WeatherFrame

class GUI:
    def __init__(self, title):
        self.root = Tk()
        self.root.title(title)

    def addMonitor(self, infoList):
        WeatherFrame(self.root, infoList)

    def startLoop(self):
        self.root.mainloop()