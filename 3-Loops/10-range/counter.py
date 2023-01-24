# Counter
# Demonstrates the range() function

print("Counting:")
count = ''
for i in range(10):
	count += f"{i} "
print(count)

print("\n\nCounting by fives:")
count = ''
for i in range(0, 50, 5):
	count += f"{i} "
print(count)

print("\n\nCounting backwards:")
count = ''
for i in range(10, 0, -1):
	count += f"{i} "
print(count)
