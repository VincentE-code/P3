"""
This module defines the character macgyver

"""


class Macgyver:

    """ We find in this class the coordinates of macgyver and its backpack."""

    def __init__(self, x, y):
        self.coo_x = x
        self.coo_y = y
        self.backpack_space = []
        self.full_backpack = False

    def backpack(self, backpack_space):
        """full_backpack counts the number of items that macgyver picks up."""
        if backpack_space == 3:
            self.full_backpack = True
        if backpack_space < 3:
            self.full_backpack = False
