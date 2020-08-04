class Maze:

    def __init__(self):
        print("object created")

    def set_grid(self):
        with open('maze.txt') as maze:
            datas = maze.read()
            # je parcours toutes mes lettres
            # le retour a la ligne est le caractère "\n"
            for letter in datas:
                if letter == "M":
                    print("wall")
                    x = x + 1
                if letter == "A":
                    print("start")
                    x = x + 1
                if letter == "C":
                    print("path")
                    x = x + 1
                if letter == "S":
                    print("exit")
                    x = x + 1
                if letter == "\n":
                    print("Line break")
                    x = 0
                    y = y + 1
    

if _name_ == "__main__":
    # ici tu test ton code
    maze = Maze()
    maze.set_grid()


