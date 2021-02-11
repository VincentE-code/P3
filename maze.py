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
        self.floor = []
        self.wall = []
        self.backpack_space = []
        self.macgyver = None
        self.guardian = None
        self.set_grid()
        self.position_items()
        # self.directional_keys()
        # self.move_on_destination()

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
                self.floor.append((count_x, count_y))
                count_x = count_x + 1
            if letter == "S":
                self.grid[(count_x, count_y)] = "exit"
                count_x = count_x + 1
            if letter == "\n":
                print("line break")
                count_x = 0
                count_y = count_y + 1

    def position_items(self):
        """position_items positions the objects on the paths."""
        for obj in ["plastic_tube", "needle", "ether"]:
            # on commence par mélanger les chemins
            random.shuffle(self.floor)
            # print(self.floor[0])
            # on prend la première case, et on y colle un objet
            self.grid[self.floor[0]] = obj
            # on vire la case déjà utilisée du self.floor
            self.floor.remove(self.floor[0])

    def directional_keys(self, move):
        """directional_keys manages the movements
        according to the directional keys."""
        self.old_coo = (self.macgyver.coo_x, self.macgyver.coo_y)
        print(self.macgyver.coo_x, self.macgyver.coo_y)
        if move == "u":  # "u" = up
            self.macgyver.coo_y -= 1
        if move == "d":  # "d" = down
            self.macgyver.coo_y += 1
        if move == "r":  # "r" = right
            self.macgyver.coo_x += 1
        if move == "l":  # "l" = left
            self.macgyver.coo_x -= 1
        return [self.old_coo, (self.macgyver.coo_x, self.macgyver.coo_y)]

    def move_on_destination(self, new_coo):
        """move_on_destination move the player
        according to what he is on the destination."""
        print("new_coo : ", new_coo)
        if self.grid[new_coo[1]] in self.wall:
            print("Impossible move")
        if self.grid[new_coo[1]] in self.floor:
            # remettre la case où était macgyver en "floor"
            self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "floor"
            # changer les coo de macgyver
            self.macgyver.coo_x = new_coo[1][0]
            self.macgyver.coo_y = new_coo[1][1]
            self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "floor"
        for obj in ["plastic_tube", "needle", "ether"]:
            if self.grid[new_coo[1]] in obj:
                self.backpack_space.append(obj)
                self.macgyver.coo_x = new_coo[1][0]
                self.macgyver.coo_y = new_coo[1][1]
                self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "floor"
                print("my objects : ", self.backpack_space)
            if self.grid[new_coo[1]] in [self.guardian.coo_x, self.guardian.coo_y]:
                if self.backpack_space == ["plastic_tube", "needle", "ether"]:
                    self.macgyver.coo_x = new_coo[1][0]
                    self.macgyver.coo_y = new_coo[1][1]
                    self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "floor"
                    print("Bravo! Tu as gagné!")
                else: 
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
