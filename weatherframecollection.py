from weatherframe import WeatherFrame

"""
Holds a list of all WeatherFrame instances.
"""

class WeatherFrameCollection:
    def __init__(self):
        self.wFrameList = []

    def addFrame(self, newFrame):
        self.wFrameList.append(newFrame)

    def clearAllFrames(self):
        for wFrame in self.wFrameList:
            wFrame.closeFrame(wFrame.frame)
        self.wFrameList = []