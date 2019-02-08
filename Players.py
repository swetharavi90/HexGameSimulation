# Players.py
"""
The base player class
"""
from random import choice, shuffle

class Player(object):
    """
    Base player class
    """
    def __init__(self, name=None):
        """
        Constructor to initialize the base class.
        @param name - the name of the player
        """
        self.name = name
        self.side = None
        self.game = None
        self.wins = 0
        self.losses = 0

    def setSide(self, side):
        """
        Sets the side of the player
        @param side - side to be set.
        """
        self.side = side

    def otherSide(self, side):
        """
        Changes the side of the player
        @param side - side to be set.
        """
        return -1*side

    def won(self):
        """
        Increments the win counter of the player
        """
        self.wins += 1

    def lost(self):
        """
        Increments the loss counter of the player
        """
        self.losses += 1


    def getMove(self, board):
        """
        Returns the current move for the board
        @param board - the board to be considered
        """
        raise NotImplementedError()