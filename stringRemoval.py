list = ["a", "a", "a", "b", "c", "m"]

i = 0
for ch in list:
	if ch == 'c':
		del list[i]
	i += 1
		
print(list)