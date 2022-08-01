# Finicky Counter
# Demonstrates the break and continue statements

count = 0
for i in '1234567890':
	count += 1
	# end loop if count greater than 10
	if count > 10:
		break
	# skip 5
	if count == 5:
		continue
	print(count)
		
