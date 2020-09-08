import Items

import Macgyver

import Guardian

class Maze:

    def __init__(self):
        print("object created")
        self.grid = {}
        self.chemin = []
        self.items = []
        self.backpack_macgyver = []

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
        #Trouver comment remplacer aléatoirement un élément dans une liste 
        items = []
        for chemin in chemin:

    def macgyver_move(self): #Gérer les déplacements ! (haut, bas, droite, gauche)
        macgyver = (x, y)
        for macgyver in grid.values():
            if direction == up:
                y = y + 1
            if direction == down:
                y = y - 1
            if direction == right:
                x = x + 1
            if direction == left:
                x = x - 1 

        for macgyver in grid.values():
            if macgyver == "wall": #vérifier que la destination n'est pas un mur
                                    #vérifier que la destination n'est pas en dehors de la grille du labyrinthe
                print("None")

            i = 0
            if macgyver == needle:              #vérifier s'il y a un objet ou non sur la case de destination
                backpack_macgyver.append(i + 1) #ajouter l'objet ramassé dans le sac a dos de MacGyver
            if macgyver == syringue:
                backpack_macgyver.append(i + 1)
            if macgyver == plastic_tube:
                backpack_macgyver.append(i + 1)
            if macgyver == ether:
                backpack_macgyver.append(i + 1)
    
    #"ramasser" cet objet. redéfinir la valeur de la clé dans la grille à "chemin"????????????????????????????

        if i == 4 and macgyver() == guardian(): #vérifier s'il y a le gardien ou non sur la case de destination
            print("Bravo! Tu as gagné!")
        elif i < 4 and macgyver() == guardian():
            print("game over! Tu as perdu")
        continue

        if macgyver() == "exit" and i == 4:
            print("Bravo! Tu as gagné!")    
        continue
        


if __name__ == "__main__":
    # ici tu test ton code
    maze = Maze()
    maze.set_grid()
    print(maze.grid)
    print(maze.chemin)
    print(maze.items)