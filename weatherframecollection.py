"""
Holds a list of all WeatherFrame instances.
"""

class WeatherFrameCollection:
    def __init__(self):
        self.wFrameList = []

    """
    Add a frame to the Weather Frame Collection list given a new frame.
    """
    def addFrame(self, newFrame):
        self.wFrameList.append(newFrame)


    """
    Closes frame from the window and remove all frames from the Weather Frame Collection.
    """
    def clearAllFrames(self):
        for wFrame in self.wFrameList:
            wFrame.closeFrame(wFrame.frame)
        self.wFrameList = []