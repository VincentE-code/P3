"""
This module defines the character guardians

"""


class Guardian:

    """ We find in this class the coordinates of the guardian."""

    def __init__(self, image_guardian, x, y):
        self.coo_x = x
        self.coo_y = y
        self.image_guardian = image_guardian.png
