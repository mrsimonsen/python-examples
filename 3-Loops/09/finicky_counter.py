# Finicky Counter
# Demonstrates the break and continue statements

for i in '1234567890ABC':
	count = int(i)
	# end loop if count greater than 10
	if count < 1:
		break
	# skip 5
	if count == 5:
		continue
	print(count)
		
