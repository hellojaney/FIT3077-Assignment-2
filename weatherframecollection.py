from weatherframe import WeatherFrame

class WeatherFrameCollection:
    def __init__(self):
        self.wFrameList = []

    def addFrame(self, newFrame):
        self.wFrameList.append(newFrame)

    def clearAllFrames(self):
        for wFrame in self.wFrameList:
            wFrame.closeFrame(wFrame.frame)
        self.wFrameList = []