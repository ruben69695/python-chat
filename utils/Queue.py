from utils import BaseCollection

class Queue(BaseCollection.BaseCollection):

    def __init__(self, items=[]):
        self.__array = items
        self.length = len(items)
    
    def remove(self):
        if self.length == 0:
            raise Exception('The queue is empty')

        last = self.__array.pop(0)
        self.length -= 1
        return last
    
    def get_queue(self):
        return self.__array

    def clone(self):
        return Queue(self.__array)
