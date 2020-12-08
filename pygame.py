from maze import Maze

import pygame


pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Macgyver maze")
screen = pygame.display.set_mode((500, 500))

# importer l'arrière plan du jeu
background = pygame.image.load("floor_image.png")

game = Maze()

running = True

maze = [
MMMMMMMMMMMMMMM
SCCCCCCCCCBCCCM
MMMMMMMCMMMMMCM
MCCCCCMCMCCCMCM 
MCMCCCMCMCCCCCM
MCMCMMMCMMMMMCM 
MCMCMCCCCCCCMCM
MCMCMCCCCCCCMCM
MCMCMMMMMMMMMCM
MCMCCCCCCCCCCCM
MCMMMMMMMMMMMCM
MCMCCCCCCCCCCCM
MCMMMMMMMMMMMCM
MCCCACCCCCCCCCM
MMMMMMMMMMMMMMM]

# boucle tant que cette condition est vrai
while running:


    # que l'évenement est la fermeture de fenêtre
    if event.type == pygame.QUIT:
        running = False
        pygame.quit()

    # appliquer l'arrière plan du jeu
    # blit va ajouter l'image de mon choix
    screen.blit(background, (0, 0))

    # déssiner la grille
    x = 0
    y = 0
    for letter in datas:
            if letter == "M":
                screen.blit(wall_image.png, (0, 0))
            if letter == "A":
                screen.blit(macgyver.png, (0, 0))
            if letter == "B":
                screen.blit((guardian.png, (0, 0))
            if letter == "S":
                
    for event in pygame.event.get():
    	if event.type == pygame.KEYDOWN:
        	if event.key == pygame.K_RIGHT:
        		self.maze.directional_keys = "r"
        		print("déplacement vers la droite")

        	if event.key == pygame.K_LEFT:
        		self.maze.directional_keys = "l"
        		print("déplacement vers la gauche")

        	if event.key == pygame.K_UP:
        		self.maze.directional_keys = "u"
        		print("déplacement vers le haut")

        	if event.key == pygame.K_DOWN:
        		self.maze.directional_keys = "d"
        		print("déplacement vers le bas")

        # que l'évenement est la fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

if __name__ == "__main__":
