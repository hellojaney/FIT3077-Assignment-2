from Tkinter import *

"""
Creates a Frame() for the GUI
Takes a list of information from getAllInfo: location, timestamp, rainfall and temp)
Packs the frame into the GUI
"""

def closeMonitor(frame):
    frame.pack_forget()
    frame.destroy()

class WeatherFrame:
    def __init__(self, root):
        self.frame = Frame(root)
        self.frame.pack(side=TOP, anchor=NW)

    def addData(self, list):
        index = 0
        Label(self.frame, text = list[0], font = "Helvetica 16 bold").grid(row=0, column=0)
        self.closeButton = Button(self.frame, text="x", command=lambda: closeMonitor(self.frame)).grid(row = 0, column = 5)
        index += 1
        while index < len(list):
            Label(self.frame, text = list[index], font = "Helvetica 14").grid(row=index, column=0)
            index += 1

