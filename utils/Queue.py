class Queue():

    def __init__(self, items=[]):
        self.__array = items
        self.length = len(items)
    
    def enqueue(self, item):
        self.__array.append(item)
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            raise Exception('The queue is empty')

        last = self.__array.pop()
        self.length -= 1
        return last
    
    def get_queue(self):
        return self.__array

    def clone(self):
        return Queue(self.__array)
