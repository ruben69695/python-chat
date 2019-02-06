class Queue():
    """
    Queue manager utility class

    ...

    Attributes
    ----------
    length : int
        Holds the length of the queue

    Methods
    -------
    enqueue(item=[])
        Adds the item list to self.__array 
    dequeue()
        Removes the last element of self.__array, if any
    get_queue()
        Returns self.__array
    clone()
        Returns a copy of self.__array
    """


    def __init__(self, items=[]):
        """
        Parameters
        ----------
        __array : list
            A private list that holds N elements of any type
        length : int
            The count of all the elements inside __array
        """
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
        """ Removes the last item of the queue

        Parameters
        ----------
        None
        """"
        if self.length == 0:
            raise Exception('The queue is empty')

        last = self.__array[-1]
        self.__array.pop()
        self.length -= 1
        return last
    
    def get_queue(self):
        """ Returns self.__array

        Acts as a getter of the private attribute __array

        Parameters
        ----------
        None
        """
        return self.__array

    def clone(self):
        """ Clones self.__array

        Returns a attribute __array as a copy without references 
        to the instance

        Parameters
        ----------
        None
        """
        return Queue(self.__array)
