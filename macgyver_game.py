"""
This module defines the game.

"""


import pygame

from maze import Maze


class Macgyver_game:

    """We find in this class the game of the project."""

    pygame.init()

    def __init__(self):
        self.game_settings()
        self.game_loop()
        self.running = True

    def game_settings(self):
        """game_settings defined the settings of the game."""
        pygame.display.set_caption("Macgyver maze")
        screen = pygame.display.set_mode((300, 300))

        taille_carre = 20

        maze = Maze()

        for key, value in maze.grid.items():
            # key = (x, y)
            # value = M / A / C / S ....
            coo_x = key[0] * taille_carre
            coo_y = key[1] * taille_carre
            image = ""
            if value == "M":
                image = "wall.png"
            elif value == "A":
                image = "macgyver.png"
            elif value == "C":
                image = "floor_image.png"
            elif value == "S":
                image = "exit.png"
            elif value == "B":
                image == "guardian.png"

        self.maze.position_items()

        # afficher la case
        screen.blit(image, (coo_x, coo_y))

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

    MACGYVER_GAME = Macgyver_game()
