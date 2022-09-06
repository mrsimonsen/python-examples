# Classy Critter
# Demonstrates class attributes and static methods

class Critter(object):
	"""A virtual pet"""
	total = 0

	@staticmethod   
	def status():
		print(f"\nThe total number of critters is {Critter.total}")
        
	def __init__(self, name):
		print("A critter has been born!")
		self.name = name
		Critter.total += 1

#main
print(f"Accessing the class attribute Critter.total: {Critter.total}")

print("\nCreating critters.")
crit1 = Critter("critter 1")
crit2 = Critter("critter 2")
crit3 = Critter("critter 3")

Critter.status()

print(f"\nAccessing the class attribute through an object: {crit1.total}")

