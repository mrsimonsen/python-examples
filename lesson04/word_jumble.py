# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word

import random

# create a sequence of words to choose from
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
# pick one word randomly from the sequence
word = random.choice(WORDS)
# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble =""
while word:#while there are letters left in the word
	position = random.randrange(len(word))#get a random index position
	jumble += word[position]#add that letter to the jumble
	word = word[:position] + word[(position + 1):]#remove that letter from the word

# start the game
print(
"""
					Welcome to Word Jumble!
				
	Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""
)
print(f"The jumble is: {jumble}\n")

guess = input("Your guess:\n")
while guess != correct and guess != "":
	print("Sorry, that's not it.")
	guess = input("Your guess:\n")
		
if guess == correct:
	print("That's it!  You guessed it!\n")

print("Thanks for playing.")

