from threading import Timer,Thread,Event

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
"""

class ControllerTimer():
    def __init__(self, time, action):
        self.time = time
        self.action = action
        self.thread = Timer(self.time, self.handler)

    def handler(self):
        self.action()
        self.thread = Timer(self.time, self.handler).start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()