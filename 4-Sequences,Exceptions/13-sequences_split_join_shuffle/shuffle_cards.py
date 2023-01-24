#Demonstrates the random.shuffle() method
import random
#create a deck of cards
deck = []
for suit in ('S','C','D','H'):
	#Spades, Clubs, Diamonds, Hearts
	for value in ('A','2','3','4','5','6','7','8','9','10','J','Q','K'):
		#Face values
		deck += [value+suit]
print(f"Original deck:\n{deck}")
random.shuffle(deck)
print(f"Shuffled deck:\n{deck}")