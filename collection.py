"""
The Collection abstract class represents a list with operations including adding an object, check if the object exists and remove the object.
"""
class Collection:
    def __init__(self):
        self.collectionList = []


    def add(self, item):
        self.collectionList.append(item)


    def exists(self, item):
        pass


    def removeFromCollection(self, item):
        pass