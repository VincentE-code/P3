from items import Items
# from file import Element(s)
from macgyver import Macgyver

from guardian import Guardian

import random


class Maze:

    def __init__(self):
        # print("object created")
        self.grid = {}
        self.chemin = []
        self.wall = []
        self.backpack_space = []
        self.set_grid()
        self.position_items()
        self.can_move(6, 2)
        self.macgyver_move("u")

    def set_grid(self):
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
                self.macgyver = macgyver(x, y)
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

    def position_items(self):  # Positionner les objets sur les chemins
        # pour chacun des 3 objets
        for obj in ["plastic_tube", "needle", "ether"]:
            # on commence par mélanger les chemins
            random.shuffle(self.chemin)
            # print(self.chemin[0])
            # on prend la première case, et on y colle un objet
            self.grid[self.chemin[0]] = obj
            # on vire la case déjà utilisée du self.chemin
            self.chemin.remove(self.chemin[0])

    def macgyver_move(self, move):
        if move == "u":  # "u" = up
            new_y = macgyver(y) - 1
            new_x = macgyver(x)
        if move == "d":  # "d" = down
            new_y = macgyver(y) + 1
            new_x = macgyver(x)
        if move == "r":  # "r" = right
            new_x = macgyver(x) + 1
            new_y = macgyver(y)
        if move == "l":  # "l" = left
            new_x = macgyver(x) - 1
            new_y = macgyver(y)
        # tu connais les nouvelles coordonnées (new_x, new_y)
        # tu dois vérifier ce qu'il y a sur les nouvelles coordonnées
        # si tu peux déplacer macgyver ou non
        # et savoir si tu dois ramasser un objet ou non
        # et savoir si tu es sur le gardien ou non

    def can_move(self, full_backpack, macgyver_move):
        # vérifier que la destination n'est pas un mur
        if macgyver(x, y) in self.wall:
            pass
        if macgyver(x, y) in self.chemin:
            # changer les coo de macgyver
            macgyver(x) = self.macgyver_move.new_x
            macgyver(y) = self.macgyver_move.new_y
            return macgyver(x, y)
            # remettre la case où était macgyver en "chemin"
        for obj in ["plastic_tube", "needle", "ether"]:
            if macgyver(x, y) in obj:
                self.is_picked_up = True
                self.backpack_space.append(obj)
                self.macgyver.coo_x = self.macgyver_move.new_x
                self.macgyver.coo_y = self.macgyver_move.new_y
                self.grid[self.macgyver.coo_x, self.macgyver.coo_y] = "chemin"
            if macgyver(x, y) in Guardian():
                if self.full_backpack is True:
                    self.macgyver.coo_x = self.macgyver_move.new_x
                    self.macgyver.coo_y = self.macgyver_move.new_y
                    print("Bravo! Tu as gagné!")
                elif self.full_backpack is False:
                    print("game over! Tu as perdu")


if __name__ == "__main__":

    maze = Maze()
    print(maze.grid)
    print(maze.can_move)
