#sum of numbers in a file

def getChoice():
	print()
	choice = input("Sum or average? (s/a): ")
	return choice

def SumAndCount(fileIn):
	sum = 0
	count = 0
	
	for line in fileIn:
		sum += float(line)
		count += 1
	return sum, count

#def calcAverage():

def main():
	
	try:
		fileIn = open(r"D:\nkfyn\Programming\Python\readWriteFiles\SepLineNumbers.txt", "r")
		
		choice = getChoice()
		sum, count= SumAndCount(fileIn)
		
		if choice == "s":
			print(sum)
		elif choice == "a":
			avg = sum/count
			print(avg)
		else:
			print("Invalid input")
	except:
		print("An error occured")
	
	
	fileIn.close()
	
	
	

main()