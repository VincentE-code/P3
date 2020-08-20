class Items():

	def __init__(self, items):
		self.items= {}

	def set_items(self):
		with open('maze.txt') as maze:
			datas = maze.read()
			# je parcours toutes mes lettres
		i = 0
		for letter in datas:
			if letter == "B":
				self.items[(x, y)] = needle()
				i = i + 1
				#Peut-être se créer une condition "si B = 1, alors B dans le backpack. Si B = 0 alors le contraire"
			if letter == "D":
				self.items[(x, y)] = syringue()
				i = i + 1
			if letter == "E":
				self.items[(x, y)] = plastic_tube()
				i = i + 1
			if letter == "F":
				self.items[(x, y)] = ether()
				i = i + 1

	def needle():
		image_of_needle = needle.png
		i = 1

	def syringue():
		image_of_syringue = syringue.png
		i = 1

	def plastic_tube():
		image_of_plastic_tube = plastic_tube.png
		i = 1

	def ether():
		image_of_ether = ether.png
		i = 1
		

	def backpack_MacGyver():
	    items_inventory = []
	#Ajoutez un compteur qui les listera.

	if __name__ == "__main__":
    # ici tu test ton code
    	items = Items()
		items.needle()
		items.syringue()
		items.plastic_tube()
		items.ether()
		items.backpack_MacGyver()
		print(maze.items)

