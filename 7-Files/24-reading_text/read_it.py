# Read It
# Demonstrates reading from a text file

print("\nReading characters from the file.")
with open open("read_it.txt", "r") as file:
	print(file.read(1))
	print(file.read(5))

print("\nReading the entire file at once.")
with open("read_it.txt", "r") as file:
	whole_thing = file.read()
print(whole_thing)


print("\nReading characters from a line.")
with open("read_it.txt", "r") as file:
	print(file.readline(1))
	print(file.readline(5))

print("\nReading one line at a time.")
with open("read_it.txt", "r") as file:
	print(file.readline())
	print(file.readline())
	print(file.readline())

print("\nLooping through the file, line by line.")
with open("read_it.txt", "r") as file:
	for line in file:
		print(line)

print("\nReading the entire file into a list.")
with open("read_it.txt", "r") as file:
	lines = file.readlines()
print(lines) 
print(len(lines))
for line in lines:
	print(line)


