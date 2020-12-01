"""
This module defines the maze.

"""


import random

from items import Items
# from file import Element(s)
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
        self.set_grid()
        self.position_items()
        self.move_on_destination((2, 12))
        self.directional_keys("l")
        self.macgyver(2, 11)

    def set_grid(self):
        """set_grid defined the maze."""
        with open('maze.txt') as maze:
            datas = maze.read()
        # je parcours toutes mes lettres
        # le retour a la ligne est le caractère "\n"
        x = 0
        y = 0
        for letter in datas:
            print(x, y)
            if letter == "M":
                self.grid[(x, y)] = "wall"
                x = x + 1
                self.wall.append((x, y))
            if letter == "A":
                self.grid[(x, y)] = "start"
                x = x + 1
                self.macgyver = self.macgyver(self.macgyver.coo_x, self.macgyver.coo_y)
            if letter == "C":
                self.grid[(x, y)] = "chemin"
                self.chemin.append((x, y))
                x = x + 1
            if letter == "S":
                self.grid[(x, y)] = "exit"
                x = x + 1
            if letter == "\n":
                print("line break")
                x = 0
                y = y + 1

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
        """directional_keys manages the movements according to the directional keys."""
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
        """move_on_destination move the player according to what he is on the destination."""
        if new_coo in self.wall:
            pass
        if new_coo in self.chemin:
            # remettre la case où était macgyver en "chemin"
            self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "chemin"
            # changer les coo de macgyver
            self.macgyver.coo_x = new_coo[0]
            self.macgyver.coo_y = new_coo[1]
        for obj in ["plastic_tube", "needle", "ether"]:
            if new_coo in obj:
                self.is_picked_up = True
                self.backpack_space.append(obj)
                self.macgyver.coo_x = new_coo[0]
                self.macgyver.coo_y = new_coo[1]
                self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "chemin"
            if new_coo in self.guardian():
                if self.macgyver.full_backpack is True:
                    self.macgyver.coo_x = new_coo[0]
                    self.macgyver.coo_y = new_coo[1]
                    print("Bravo! Tu as gagné!")
                elif self.macgyver.full_backpack is False:
                    print("game over! Tu as perdu")


if __name__ == "__main__":

    maze = Maze()
    # tester directional_keys en bas
    print(maze.directional_keys("d"))
    # tester directional_keys en haut
    print(maze.directional_keys("u"))
    # tester directional_keys à droite
    print(maze.directional_keys("r"))
    # tester directional_keys à gauche
    print(maze.directional_keys("l"))
