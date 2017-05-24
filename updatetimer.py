from threading import Timer

"""
Code derived from http://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds
Timer class keeps track of time for refreshing the weather locations
"""

class UpdateTimer():
    def __init__(self, time, action):
        self.time = time
        self.action = action
        self.thread = Timer(self.time, self.handler)


    """
    Reinstantiate Timer
    """
    def handler(self):
        self.action()
        self.thread = Timer(self.time, self.handler)
        self.thread.start()


    """
    Start Timer
    """
    def start(self):
        self.thread.start()


    """
    Cancel Timer (when program is quit)
    """
    def cancel(self):
        self.thread.cancel()