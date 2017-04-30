from weatherframecontroller import WeatherFrameController
from guicontroller import GUIController
from timer import ControllerTimer

class Controller():
    def __init__(self):
        self.guiController = GUIController()
        self.weatherFrameController = WeatherFrameController(self.guiController.guiFrame)
        self.timer = ControllerTimer(3, lambda: self.weatherFrameController.refreshLocations(self.guiController.active,
            self.weatherFrameController.wFrameCollection, self.guiController.webClient))

    def run(self):
        self.guiController.start()

    def quit(self):
        print("Quitting Program.")
        self.timer.cancel()


if __name__ == '__main__':
    controller = Controller()
    controller.run()
    controller.quit()

