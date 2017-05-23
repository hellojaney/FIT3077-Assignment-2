class Collection:
    def __init__(self, caller):
        self.collectionList = []
        self.caller = caller

    def add(self, item):
        self.collectionList.append(item)

    def exists(self):
        pass

    def remove(self):
        pass