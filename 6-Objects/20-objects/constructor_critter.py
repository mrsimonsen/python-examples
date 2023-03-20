# Constructor Critter
# Demonstrates constructors

class Critter():
	"""A virtual pet""" 
	def __init__(self):
		print("A new critter has been born!")

	def talk(self):
		print("\nHi.  I'm an instance of class Critter.")

# main
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

