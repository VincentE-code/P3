from maze import Maze

import pygame


pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Macgyver maze")
screen = pygame.display.set_mode((800, 500))

# importer l'arrière plan du jeu
background = pygame.image.load("floor_image.png")

game = Maze()

running = True

# boucle tant que cette condition est vrai
while running:

    # appliquer l'arrière plan du jeu
    # blit va ajouter l'image de mon choix
    screen.blit(background, (0, 0))

    #définir la grille


    # si le joueur ferme cette fenêtre
    for event in pygame.event.get():
        # que l'évenement est la fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
