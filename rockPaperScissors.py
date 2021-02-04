#rock, paper, scissors
import random 

def generateChoice():
	cpuChoice = random.randint(1, 3)
	# 1 is rock, 2 is paper, 3 is scissors
	return cpuChoice

def main():
	print("\nITS ROCK PAPER SCISSORS, BITCH!\n")
	
	play = True
	
	while play:
	
		cpuChoice = generateChoice()
	
		userChoice = input("Rock, paper, or scissors? (r/p/s) ")
	
		#cpu chooses rock
		if cpuChoice == 1:
			if userChoice == "r":
				print("  Tie")
			if userChoice == "p":
				print("  You win")
			elif userChoice == "s":
				print("  You lose")
				
		#cpu chooses paper
		if cpuChoice == 2:
			if userChoice == "p":
				print("  Tie")
			if userChoice == "s":
				print("  You win")
			elif userChoice == "r":
				print("You lose")
				
		#cpu chooses scissors
		if cpuChoice == 3:
			if userChoice == "s":
				print("  Tie")
			if userChoice == "r":
				print("  You win")
			elif userChoice == "p":
				print("  You lose")
		
		yesNo = input("  Play again? (y/n)")
		print()
		if yesNo != "y":
			play = False
		
		

main()


