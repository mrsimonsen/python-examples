#Demonstrates inheritance and polymorphism

class Critter(object):
	pets = []
	def __init__(self, name):
		self.name = name
		self.type = 'Critter'
		Critter.pets.append(self)
	
	def talk(self):
		print(f"Hi, I'm {self.name} and I'm a {self.type}.")

class Dog(Critter):
	def __init__(self, name):
		super().__init__(name)
		self.type = 'Dog'

	def talk(self):
		super().talk()
		print("Woof!")

class Cat(Critter):
	def __init__(self, name):
		super().__init__(name)
		self.type = 'Cat'

	def talk(self):
		super().talk()
		print("Meow!")

#main()
crit = Critter('Francis')
dog = Dog('Doug')
cat = Cat("Thomas")

for pet in Critter.pets:
	pet.talk()
