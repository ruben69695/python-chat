from utils import BaseCollection

class Stack(BaseCollection.BaseCollection):

    def __init__(self, items=[]):
        self.__array = items
        self.length = len(items)
    
    def remove(self):
        if self.length == 0:
            raise Exception('The stack is empty')

        last = self.__array.pop()
        self.length -= 1
        return last

    def clone(self):
        return Stack(self.__array)