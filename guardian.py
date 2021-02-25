"""
This module defines the character guardians

"""


class Guardian:

    """ We find in this class the coordinates of the guardian."""

    def __init__(self, x, y):
        self.coo_x = x
        self.coo_y = y

    def get_tuple(self):
        return (self.coo_x, self.coo_y)

