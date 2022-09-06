# Write It
# Demonstrates writing to a text file

print("Creating a text file with the write() method.")
with open("write_it.txt", "w") as file:
	file.write("Line 1\n")
	file.write("This is line 2\n")
	file.write("That makes this line 3\n")

print("\nReading the newly created file.")
with open("write_it.txt", "r") as file:
	print(file.read())

print("\nCreating a text file with the writelines() method.")
	lines = ["Line 1\n",
			"This is line 2\n",
			"That makes this line 3\n"]
with open("write_it.txt", "w") as file:
	file.writelines(lines)

print("\nReading the newly created file.")
with open("write_it.txt", "r") as file:
	print(file.read())

print("\nAppending data to the existing file.")
with open("write_it.txt", "a") as file:
	file.write("Appending line 4\n")

print("\nReading the existing file.")
with open("write_it.txt", "r") as file:
	print(file.read())