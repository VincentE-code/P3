from maze import Maze

import pygame


pygame.init()

# Générer la fenêtre du jeu
pygame.display.set_caption("Macgyver maze")
screen = pygame.display.set_mode((300, 300))

# importer l'arrière plan du jeu
background = pygame.image.load("floor_image.png")

game = Maze()

running = True

taille_carre = 20

maze = Maze()

for key, value in maze.grid.items():
	# key = (x, y)
	# value = M / A / C / S ....
	coo_x = key[0] * taille_carre
	coo_y = key[1] * taille_carre
	image = ""
	if value == "M":
		image = "mur.jpg"
	elif value == "A":
		image = "macgyver.png"
	elif value == "C":
		image = "floor_image.png"
	elif value == "S":
		image = "tile-crusader-logo.png"
	elif value == "B":
		image == "guardian.png"

self.maze.position_items()

	# afficher la case
	screen.blit(image, (coo_x, coo_y))

# boucle tant que cette condition est vrai
while running:

	# appliquer l'arrière plan du jeu
	# blit va ajouter l'image de mon choix
	screen.blit(background, (0, 0))

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
			running = False
			pygame.quit()

if __name__ == "__main__":

	MACGYVER_GAME = pygame()
