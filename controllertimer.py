from threading import Timer

"""
Code inspired by http://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
Timer class keeps track of time for refreshing the weather locations
"""

class ControllerTimer():
    def __init__(self, time, action):
        self.time = time
        self.action = action
        self.thread = Timer(self.time, self.handler)

    def handler(self):
        self.action()
        self.thread = Timer(self.time, self.handler)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()