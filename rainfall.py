"""
Holds Rainfall Information for a Location
"""

class Rainfall:
    def __init__(self, amount):
        self.amountMm = amount


    def getAmount(self):
        return self.amountMm


    def setAmount(self, newAmount):
        self.amountMm = newAmount