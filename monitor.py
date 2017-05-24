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

    """
    Stop the timer in the associated location so that no more updates from the webclient are made
    Removes the location and the monitor from their collectons
    """
    def remove(self):
        self.location.stopTimer()
        self.location.remove()
        self.caller.remove(self.location.name, self.location.serviceType, self.location.viewType,self.location.dataType)