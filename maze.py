import Items

import Macgyver

class Maze:

    def __init__(self):
        print("object created")
        self.grid = {}
        self.chemin = []
        self.items = [needle, syringue, plastic_tube, ether]
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
        items = [needle, syringue, plastic_tube, ether]
        for chemin in grid.values():

    def macgyver_move(self): #Gérer les déplacements ! (haut, bas, droite, gauche)
        for chemin in grid.values():
            if 

    #vérifier que la destination n'est pas un mur
    #vérifier que la destination n'est pas en dehors de la grille du labyrinthe
    #vérifier s'il y a un objet ou non sur la case de destination
    #"ramasser" cet objet. redéfinir la valeur de la clé dans la grille à "chemin"
    #ajouter l'objet ramassé dans le sac a dos de MacGyver
    #vérifier s'il y a le gardien ou non sur la case de destination
    #Creation d'une classe qui va représenter Le gardien        

    def backpack_macgyver(self):
        if i == 4 and macgyver() == guardian()
        print("Bravo! Tu as gagné!")
        elif i < 4 and macgyver() == guardian()
        print("game over! Tu as perdu")
        continue

        if macgyver() == "exit" and i == 4
        print("Bravo! Tu as gagné!")    
        continue
        


if __name__ == "__main__":
    # ici tu test ton code
    maze = Maze()
    maze.set_grid()
    print(maze.grid)
    print(maze.chemin)
    print(maze.items)