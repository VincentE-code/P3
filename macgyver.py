class Macgyver:

    def __init__(self, x, y, full_backpack):
        self.coo_x = x
        self.coo_y = y
        self.backpack_space = []
        self.full_backpack(False)

    def full_backpack(self, backpack_space):
        if backpack_space == 3:
            full_backpack = True
        if backpack_space < 3:
            full_backpack = False
