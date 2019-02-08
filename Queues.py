# Queues.py
"""
Queues for handling the First in first out nodes and priorities
"""
from collections import deque
from heapq import heappush, heappop

class _Queue(object):
    """
    Abstract base class for FIFO_Queue, LIFO_QUEUE, and Priority_Queue
    """
    def __init__(self):
        """
        Constructor to initialize the base queue.
        """
        self.contents = deque()

    def add(self, item):
        """
        Stores item in the queue
        @:param item - the item to be added
        """
        self.contents.append(item)

    def get(self):
        """
        Removes some item from the queue and returns it.
        @:returns - the item
        """
        raise NotImplementedError("Child classes must implement get.")

    def __len__(self):
        """ 
        Returns the length of the queue.
        @:returns - the length of the queue
        """
        return len(self.contents)

    def __repr__(self):
        """ 
        string representation of the grid.
        @:returns - the string representation of the string
        """
        return repr(self.contents)

    def __contains__(self, item):
        """ 
        Checks if the elements is already present in the queue.
        @:returns - boolean to indicate that the item in the queue
        """
        return item in self.contents

class FIFO_Queue(_Queue):
    """
    Returns the first element added to the queue
    """
    def get(self):
        """
        Removes the oldest item from the queue and returns it.
        @:returns - the item
        """        
        return self.contents.popleft()

class LIFO_Queue(_Queue):
    """
    Returns the last element in the queue.
    """
    def get(self):
        """
        Removes the newest item from the queue and returns it.
        @:returns - the item
        """
        return self.contents.pop()

class Priority_Queue(_Queue):
    """
    Returns elements based on priority
    """
    def __init__(self):
        """
        Initializes the queue
        """
        self.contents = []

    def add(self, item, priority):
        """
        Adds the element to the heap.
        """
        heappush(self.contents, (priority, item))

    def get(self):
        """
        Removes the lowest-priority item from the queue and returns it.
         @:returns - the item
        """
        return heappop(self.contents)[1]