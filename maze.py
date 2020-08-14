class Maze:

    def __init__(self):
        print("object created")
        self.grid = {}

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
                self.grid[(x, y)] = "path"
                x = x + 1
            if letter == "S":
                self.grid[(x, y)] = "exit"
                x = x + 1
            if letter == "\n":
                print("line break")
                x = 0
                y = y + 1



if __name__ == "__main__":
    # ici tu test ton code
    maze = Maze()
    maze.set_grid()
    print(maze.grid)