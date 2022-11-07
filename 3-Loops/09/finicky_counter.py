# Finicky Counter
# Demonstrates the break and continue statements

count = 0
for i in '1234567890123456789':
	count = int(i)
	# end loop if count greater than 10
	if count < 1:
		break
	# skip 5
	if count == 5:
		continue
	print(count)
		
