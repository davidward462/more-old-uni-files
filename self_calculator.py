import random
import time

def add(num1, num2):
    """Returns num1 plus num2."""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2."""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 times num2."""
    return num1 * num2


def div(num1, num2):
    #Returns num1 divided by num2.
	try:
		return num1 / num2
	except ZeroDivisionError:
		print("Handled div by zero. Returning zero.")
		return 0

		
def runOperation(num1, num2, operation):
		#Determines operation to run based on random generation
		if (operation == 1):
			#print("Adding...")
			print(add(num1, num2))
		elif (operation == 2):
			#print("Subtracting...") 
			print(sub(num1, num2))
		elif (operation == 3):
			#print("Multiplying...")
			print(mul(num1, num2))
		elif (operation == 4):
			#print("Dividing...")
			print(div(num1, num2))
			
	
def main():
	loopNumber = int(input("How many times do you want to loop? "))
	delay = float(input("Delay: "))
	for i in range(loopNumber):
	# Generate input	
		num1 = random.randint(0, 10000)
		operation = random.randint(1, 3) #1) add 2) sub 3) mult 4) div
		num2 = random.randint(1, 10000) #Probably don't divide by zero
		runOperation(num1, num2, operation)
		time.sleep(delay)


main()