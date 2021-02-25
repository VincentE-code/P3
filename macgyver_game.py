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
        self.images = {
            "wall": pygame.image.load("ressource/wall.png"),
            "macgyver": pygame.image.load("ressource/macgyver.png"),
            "floor": pygame.image.load("ressource/floor.png"),
            "exit": pygame.image.load("ressource/exit.png"),
            "guardian": pygame.image.load("ressource/guardian_image.png"),
            "plastic_tube": pygame.image.load("ressource/plastic_tube.png"),
            "ether": pygame.image.load("ressource/ether.png"),
            "needle": pygame.image.load("ressource/needle.png"),
        }
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
            self.screen.blit(self.images[value], (coo_x, coo_y))

        pygame.display.flip()

    def game_loop(self):
        """position_items positions the objects on the paths."""
        while self.running:
            taille_carre = 20
            new_x = self.maze.macgyver.coo_x
            new_y = self.maze.macgyver.coo_y
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

                    if self.maze.move_on_destination(way_to_go):
                        new_x = way_to_go[1][0] * taille_carre
                        new_y = way_to_go[1][1] * taille_carre
                        self.screen.blit(self.images["macgyver"], (new_x, new_y))
                        old_coo_x = way_to_go[0][0] * taille_carre
                        old_coo_y = way_to_go[0][1] * taille_carre
                        self.screen.blit(self.images["floor"], (old_coo_x, old_coo_y))

            pygame.display.flip()

            # que l'évenement est la fermeture de fenêtre
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()


if __name__ == "__main__":

    MACGYVER_GAME = Macgyvergame()
