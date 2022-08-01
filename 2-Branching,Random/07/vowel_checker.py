message = input("Enter a message:\n").lower()

if 'a' not in message and 'e' not in message and 'i' not in message and 'o' not in message and 'u' not in message:
	print("Your message doesn't have any vowels.")
else:
	print("Your message has at least 1 vowel in it.")

