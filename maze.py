"""
This module defines the maze.

"""


import random

from macgyver import Macgyver

from guardian import Guardian


class Maze:

    """We find in this class the details of the maze."""

    def __init__(self):
        # print("object created")
        self.grid = {}
        self.chemin = []
        self.wall = []
        self.backpack_space = []
        self.macgyver = None
        self.guardian = None
        self.set_grid()
        self.position_items()
        # self.move_on_destination(2, 12)
        # self.directional_keys("l")

    def set_grid(self):
        """set_grid defined the maze."""
        with open('maze.txt') as maze:
            datas = maze.read()
        # je parcours toutes mes lettres
        # le retour a la ligne est le caractère "\n"
        count_x = 0
        count_y = 0
        for letter in datas:
            print(count_x, count_y)
            if letter == "M":
                self.grid[(count_x, count_y)] = "wall"
                count_x = count_x + 1
                self.wall.append((count_x, count_y))
            if letter == "A":
                self.grid[(count_x, count_y)] = "macgyver"
                count_x = count_x + 1
                self.macgyver = Macgyver(count_x, count_y)
            if letter == "B":
                self.grid[(count_x, count_y)] = "guardian"
                count_x = count_x + 1
                self.guardian = Guardian(count_x, count_y)
            if letter == "C":
                self.grid[(count_x, count_y)] = "floor"
                self.chemin.append((count_x, count_y))
                count_x = count_x + 1
            if letter == "S":
                self.grid[(count_x, count_y)] = "exit"
                count_x = count_x + 1
                self.guardian = Guardian(count_x, count_y)
            if letter == "\n":
                print("line break")
                count_x = 0
                count_y = count_y + 1

    def position_items(self):
        """position_items positions the objects on the paths."""
        for obj in ["plastic_tube", "needle", "ether"]:
            # on commence par mélanger les chemins
            random.shuffle(self.chemin)
            # print(self.chemin[0])
            # on prend la première case, et on y colle un objet
            self.grid[self.chemin[0]] = obj
            # on vire la case déjà utilisée du self.chemin
            self.chemin.remove(self.chemin[0])

    def directional_keys(self, move):
        """directional_keys manages the movements
        according to the directional keys."""
        print(self.macgyver.coo_x, self.macgyver.coo_y)
        if move == "u":  # "u" = up
            new_y = self.macgyver.coo_y - 1
            new_x = self.macgyver.coo_x
        if move == "d":  # "d" = down
            new_y = self.macgyver.coo_y + 1
            new_x = self.macgyver.coo_x
        if move == "r":  # "r" = right
            new_x = self.macgyver.coo_x + 1
            new_y = self.macgyver.coo_y
        if move == "l":  # "l" = left
            new_x = self.macgyver.coo_x - 1
            new_y = self.macgyver.coo_y
        return (new_x, new_y)

    def move_on_destination(self, new_coo):
        """move_on_destination move the player
        according to what he is on the destination."""
        if new_coo in self.wall:
            pass
        if new_coo in self.chemin:
            # remettre la case où était macgyver en "chemin"
            self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "chemin"
            # changer les coo de macgyver
            self.macgyver.coo_x = new_coo[0]
            self.macgyver.coo_y = new_coo[1]
        for obj in ["plastic_tube", "needle", "ether"]:
            if self.grid[new_coo] in obj:
                self.is_picked_up = True
                self.backpack_space.append(obj)
                self.macgyver.coo_x = new_coo[0]
                self.macgyver.coo_y = new_coo[1]
                self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "chemin"
            if new_coo == (self.guardian.coo_x, self.guardian.coo_y):
                if self.macgyver.full_backpack is True:
                    self.macgyver.coo_x = new_coo[0]
                    self.macgyver.coo_y = new_coo[1]
                    print("Bravo! Tu as gagné!")
                elif self.macgyver.full_backpack is False:
                    print("game over! Tu as perdu")


if __name__ == "__main__":

    MAZE_OBJECT = Maze()
    # tester directional_keys en bas
    print(MAZE_OBJECT.directional_keys("d"))
    # tester directional_keys en haut
    print(MAZE_OBJECT.directional_keys("u"))
    # tester directional_keys à droite
    print(MAZE_OBJECT.directional_keys("r"))
    # tester directional_keys à gauche
    print(MAZE_OBJECT.directional_keys("l"))
