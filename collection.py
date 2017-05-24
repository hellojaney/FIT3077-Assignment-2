class Collection:
    def __init__(self, caller):
        self.collectionList = []
        self.caller = caller

    def add(self, item):
        self.collectionList.append(item)

    def exists(self, item):
        pass

    def removeFromCollection(self, item):
        pass