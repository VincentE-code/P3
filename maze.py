from Items import Items
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
        self.set_grid()
        self.position_items()
        self.macgyver_move()
        self.can_move()


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
                self.wall.append((x, y)) # récupère les coordonnées des chemins dans la liste "wall"
            if letter == "A":
                self.grid[(x, y)] = "start"
                x = x + 1
                self.macgyver = (x, y)
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
        # pour chacun des 3 objets
        for obj in ["plastic_tube", "needle", "ether"]:
            # on commence par mélanger les chemins
            random.shuffle(self.chemin)
            # print(self.chemin[0])
            # on prend la première case, et on y colle un objet
            self.grid[self.chemin[0]] = obj
            # on vire la case déjà utilisée du self.chemin
            self.chemin.remove(self.chemin[0])

    def macgyver_move(self, move): # gérer les déplacements de Macgyver
        if move == "u": # "u" = up
            new_y = self.macgyver.coo_y - 1
            new_x = self.macgyver.coo_x
        if move == "d": # "d" = down
            new_y = self.macgyver.coo_y + 1
            new_x = self.macgyver.coo_x
        if move == "r": # "r" = right
            new_x = self.macgyver.coo_x + 1
            new_y = self.macgyver.coo_y
        if move == "l": # "l" = left
            new_x = self.macgyver.coo_x - 1
            new_y = self.macgyver.coo_y
        # tu connais les nouvelles coordonnées (new_x, new_y)
        # tu dois vérifier ce qu'il y a sur les nouvelles coordonnées pour savoir
        # si tu peux déplacer macgyver ou non
        # et savoir si tu dois ramasser un objet ou non
        # et savoir si tu es sur le gardien ou non

    def can_move(self, coo_x, coo_y):
        #vérifier que la destination n'est pas un mur
        if (self.coo_x, self.coo_y) in self.wall:
            pass
        if (self.coo_x, self.coo_y) in self.chemin:
            # changer les coo de macgyver
            self.macgyver.coo_x = coo_x
            self.macgyver.coo_y = coo_y
            # changer l'emplacement de macgayver dans la grille
            # remettre la case où était macgyver en "chemin"


if __name__== "__main__":
    # ici tu test ton code
    maze = Maze()
    print(maze.grid)