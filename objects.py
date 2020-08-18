class Items():

	def __init__(self, items):
		self.items= {}
		items = ["needle()", "syringue()", "plastic_tube()", "ether()"]
		
	def set_items(self):
		with open('maze.txt') as maze:
        	datas = maze.read()
		B = 1
		D = 1 
		E = 1
		F = 1
		backpack_macgyver = 0
		for letter in datas:
			if letter == "B":
				self.items[] = needle()
			if letter == "D":
				self.items[] = syringue()
			if letter == "E":
				self.items[] = plastic_tube()
			if letter == "F":
				self.items[] = ether()

	def needle():
		image_of_needle = needle.png
		place_in_the_backpack = 1

	def syringue():
		image_of_syringue = syringue.png
		place_in_the_backpack = 1

	def plastic_tube():
		image_of_plastic_tube = plastic_tube.png
		place_in_the_backpack = 1

	def ether():
		image_of_ether = ether.png
		place_in_the_backpack = 1
		

	def backpack_MacGyver():
	    items_inventory = []
	#Ajoutez un compteur qui les listera.

	if __name__ == "__main__":
    # ici tu test ton code
		items.needle()
		items.syringue()
		items.plastic_tube()
		items.ether()
		items.backpack_MacGyver()
