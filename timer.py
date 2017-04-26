from activemonitors import ActiveMonitors
import time

class Timer:

    def __init__(self):
        # refreshing monitors: not too sure if there is a more efficient way to do this???\
        self.time = time.localtime(time.time())


    def checkTimer(self, currentTime):
        if currentTime%self.time == 300:
            return True
        else:
            return False
