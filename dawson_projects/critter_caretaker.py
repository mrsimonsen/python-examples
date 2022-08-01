# Critter Caretaker
# A virtual pet to care for

class Critter(object):
	"""A virtual pet"""
	def __init__(self, name, hunger = 0, boredom = 0):
		self.name = name
		self.hunger = hunger
		self.boredom = boredom

	def __pass_time(self):
		self.hunger += 1
		self.boredom += 1

	@property
	def mood(self):
		unhappiness = self.hunger + self.boredom
		if unhappiness < 5:
			m = "happy"
		elif 5 <= unhappiness <= 10:
			m = "okay"
		elif 11 <= unhappiness <= 15:
			m = "frustrated"
		else:
			m = "mad"
		return m
	
	def talk(self):
		print(f"I'm {self.name} and I feel {self.mood} now.\n")
		self.__pass_time()
	
	def eat(self, food = 4):
		print("Brruppp. Thank you.")
		self.hunger -= food
		if self.hunger < 0:
			self.hunger = 0
		self.__pass_time()

	def play(self, fun = 4):
		print("Wheee!")
		self.boredom -= fun
		if self.boredom < 0:
			self.boredom = 0
		self.__pass_time()


def main():
	crit_name = input("What do you want to name your critter?:\n")
	crit = Critter(crit_name)

	choice = None  
	while choice != "0":
		print \
		("""
		Critter Caretaker

		0 - Quit
		1 - Listen to your critter
		2 - Feed your critter
		3 - Play with your critter
		""")
	
		choice = input("Choice:\n")
		print()

		# exit
		if choice == "0":
			print("Good-bye.")

		# listen to your critter
		elif choice == "1":
			crit.talk()
		
		# feed your critter
		elif choice == "2":
			crit.eat()
			
		# play with your critter
		elif choice == "3":
			crit.play()

		# some unknown choice
		else:
			print(f"\nSorry, but {choice} isn't a valid choice.")

if __name__ == "__main__":
	main()

