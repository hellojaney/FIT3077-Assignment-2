"""
Holds Rainfall Information for a Location
"""

class Rainfall:
    def __init__(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setAmount(self, newAmount):
        self.amount = newAmount