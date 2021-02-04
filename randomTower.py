import random

def getHeight():
	height = int(input("Enter the height: "))
	return height

def generateTower(height):
	for line in range(0, height):
		for i in range(0, 6):
			print("0", end='')
		print()
	
def main():
	height = getHeight()
	generateTower(height)


main()