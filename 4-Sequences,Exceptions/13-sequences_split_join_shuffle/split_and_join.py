#Demonstrates the string methods .split() and .join()
message = input("Enter a message:\n")
char = input("What character or string do you want to split your message at:\n")
split = message.split(char)
print(f"Split message:\n{split}")
char = input("What character or string do you want to join your message with:\n")
join = char.join(split)
print(f"Joined message:\n{join}")
