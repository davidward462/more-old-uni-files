#process list

def main():

	a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	b = []

	#loop through list and check if even
	for i in range(len(a)):
		if a[i] % 2 == 0:
			b.append(a[i])
			
	print(b)

main()