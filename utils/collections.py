class Queue:
    """
    Queue manager utility class
    ...
    Attributes
    ----------
    length : int
        Holds the length of the queue
    Methods
    -------
    enqueue(item)
        Adds the item list to self.__array 
    dequeue()
        Removes the first element of self.__array, if any
    get_queue()
        Returns self.__array
    clone()
        Returns a copy of self.__array
    """

    def __init__(self, items = None):
        """
        Parameters
        ----------
        __array : list
            A private list that holds N elements of any type
        length : int
            The count of all the elements inside __array
        """
        if items is None:
            self.__array = []
            self.length = 0
        else:
            self.__array = items
            self.length = len(items)
    
    def enqueue(self, item):
        """ Adds another element to the queue
        Parameters
        ----------
        self : Queue class
            The class instance
        item : any
            An element of any type
        """
        self.__array.append(item)
        self.length += 1
    
    def dequeue(self):
        """ Removes and returns the first item of the queue

        """
        if self.length == 0:
            raise Exception('The queue is empty')

        last = self._Queue__array.pop(-1)
        self.length -= 1
        return last
    
    def get_items(self):
        """ Returns self.__array
        Acts as a getter of the private attribute __array

        """
        return self._Queue__array

    def clone(self):
        """ Clones self.__array
        Returns a attribute __array as a copy without references 
        to the instance

        """
        return self._Queue__array


class Stack:
    """
    Stack manager utility class

    ...

    Attributes
    ----------
    length : int
        Holds the length of the queue

    Methods
    -------
    add()
        Adds an element to the stack
    remove()
        Remove and returns the last element of the stack of self.__array, if any
    seek()
        Returns the last element of the stack
    get_items()
        Returns all the stack elements
    clone()
        Returns a copy of the stack
    """
    def __init__(self, items=None):
        """
        Parameters
        ----------
        __array : list
            A private list that holds N elements of any type
        length : int
            The count of all the elements inside __array
        """
        if items is None:
            self.__array = []
            self.length = 0
        else:
            self.__array = items
            self.length = len(items)
    
    def add(self, item):
        """ Adds another element to the queue
        Parameters
        ----------
        self : Queue class
            The class instance
        item : any
            An element of any type
        """
        self.__array.append(item)
        self.length += 1
    
    def remove(self):
        """ Removes and returns the last item of the stack

        """
        if self.length == 0:
            raise Exception('The stack is empty')

        last = self.__array[-1]
        self.length -= 1
        return last

    def seek(self):
        """ Returns the last item of the stack

        """
        if self.length == 0:
            raise Exception('The queue is empty')

        return self.__array[-1]
    
    def get_items(self):
        """ Returns self.__array
        Acts as a getter of the private attribute __array

        """
        return self.__array

    def clone(self):
        """ Clones self.__array
        Returns a attribute __array as a copy without references 
        to the instance

        """
        return Stack(self.__array)
