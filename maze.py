from Items.py import Items
# from file import Element(s)
from macgyver.py import Macgyver

from guardian.py import Guardian

import random

class Maze:

    def __init__(self):
        print("object created")
        self.grid = {}
        self.chemin = []
        self.set_grid
        self.position_items
        self.needle
        self.syringue
        self.plastic_tube
        self.ether

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
            if letter == "A":
                self.grid[(x, y)] = "start"
                x = x + 1
            if letter == "C":
                self.grid[(x, y)] = "chemin"
                self.chemin.append((x, y)) # récupère les coordonnées des chemins dans la liste "chemin"
                x = x + 1
            if letter == "S":
                self.grid[(x, y)] = "exit"
                x = x + 1
            if letter == "\n":
                print("line break")
                x = 0
                y = y + 1

    def position_items(self): # Positionner les objets sur les chemins 
        self.chemin.append(self.needle)
        self.chemin.append(self.syringue)
        self.chemin.append(self.plastic_tube)
        self.chemin.append(self.ether)
        random.shuffle(self.chemin)


if __name__ == "__main__":
    # ici tu test ton code
    maze = Maze()
    maze.set_grid()
    maze.position_items()