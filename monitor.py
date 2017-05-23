from observer import Observer

class Monitor(Observer):

    def __init__(self, location, caller):
        # 'declare' class variables
        self.temperature = None
        self.rainfall = None
        self.timestamp = None
        self.datestamp = None
        self.caller = caller

        # register the monitor (observer) to the location (subject)
        self.location = location
        self.location.register(self)


    def update(self, temperature, rainfall, datestamp, timestamp):
        pass