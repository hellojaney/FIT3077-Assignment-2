from weatherframecollection import WeatherFrameCollection
from weatherframe import WeatherFrame

class WeatherFrameController:

    def __init__(self, guiFrame):
        self.wFrameCollection = WeatherFrameCollection()
        self.guiFrame = guiFrame

    def refreshLocations(self, active, wFrameCollection, webClient):
        # update loop
        for location in active.activeList:
            tempData = webClient.getWeatherData(location.getName())
            location.setCelcius(tempData[0])
            location.setRainfall(tempData[1])
            location.setTimestamp(tempData[2])
            location.setDatestamp(tempData[3])

        self.wFrameCollection.clearAllFrames()

        # display loop
        for location in active.activeList:
            wFrame = WeatherFrame(self.guiFrame, active, location.getName())
            wFrame.addData(location)
            wFrameCollection.addFrame(wFrame)