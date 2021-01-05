"""
This module defines the game.

"""


import pygame

from maze import Maze

class Macgyvergame:

    """We find in this class the game of the project."""

    def __init__(self):
        self.running = True
        self.maze = Maze()
        pygame.init()
        pygame.display.set_caption("Macgyver maze")
        self.screen = pygame.display.set_mode((300, 300))
        self.wall_img = pygame.image.load("ressource/wall.png")
        self.macgyver_img = pygame.image.load("ressource/macgyver.png")
        self.floor_img = pygame.image.load("ressource/floor_image.png")
        self.exit_img = pygame.image.load("ressource/exit.png")
        self.guardian_img = pygame.image.load("ressource/guardian.png")
        self.tube_img = pygame.image.load("ressource/plastic_tube.png")
        self.ether_img = pygame.image.load("ressource/ether.png")
        self.needle_img = pygame.image.load("ressource/needle.png")
        self.game_settings()
        self.game_loop()

    def game_settings(self):
        """game_settings defined the settings of the game."""

        taille_carre = 20

        for key, value in self.maze.grid.items():
            # key = (x, y)
            # value = M / A / C / S ....
            coo_x = key[0] * taille_carre
            coo_y = key[1] * taille_carre
            image = ""
            print("value : ", value)
            if value == "wall":
                image = self.wall_img
            elif value == "start":
                image = self.macgyver_img
            elif value == "chemin":
                image = self.floor_img
            elif value == "exit":
                image = self.exit_img
            elif value == "B":
                image = self.guardian_img
            elif value == "plastic_tube":
                image = self.tube_img
            elif value == "needle":
                image = self.needle_img
            elif value == "ether":
                image = self.ether_img
                
            self.screen.blit(image, (coo_x, coo_y))

            pygame.display.flip()


    def game_loop(self):
        """position_items positions the objects on the paths."""
        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        way_to_go = self.maze.directional_keys("r")
                    if event.key == pygame.K_LEFT:
                        way_to_go = self.maze.directional_keys("l")
                    if event.key == pygame.K_UP:
                        way_to_go = self.maze.directional_keys("u")
                    if event.key == pygame.K_DOWN:
                        way_to_go = self.maze.directional_keys("d")

                    self.maze.move_on_destination(way_to_go)

            # que l'évenement est la fermeture de fenêtre
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()


if __name__ == "__main__":

    MACGYVER_GAME = Macgyvergame()