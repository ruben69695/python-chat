class BaseCollection():

    def __init__(self, items = []):
        self.__array = items
        self.length = len(items)

    def add(self, item):
        self.__array.append(item)
        self.length += 1

    def remove(self, item):
        self.__array.remove(item)

    def get_items(self):
        return self.__array

    def clone(self):
        return BaseCollection(self.__array)