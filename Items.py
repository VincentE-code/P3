"""
This module defines the items

"""


class Items:

    """We find in this class the details of the items."""

    def __init__(self, name):
        self.name = name
        self.is_picked_up = False
        self.backpack_space = 1
