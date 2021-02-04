#check if prime 

def isPrime(value):
	for i in range(2, value): #does not work all the time
		if value % i == 0:
			return False
		elif value % i != 0: #maybe just use "else: return true"
			return True


def main():
	value = int(input("Enter an integer: "))
	TrueFalse = isPrime(value)
	print(TrueFalse)

main()