import Die
import SL_Board
import Player

def main():
	# Your code goes here
	board = SL_Board.SL_Board(6, 4, 5) 
			
#Add and document suitable functions

#This function can be called in your program. 	
def boardData():
	with open("boardConfig.txt","r") as fileHandle:
		size = int(fileHandle.readline().strip("\n"))
		snakeData = fileHandle.readline().split()
		for i in range(len(snakeData)):
			snakeData[i] = int(snakeData[i].strip("\n"))
		ladderData = fileHandle.readline().split()
		for i in range(len(ladderData)):
			ladderData[i] = int(ladderData[i].strip("\n"))
		
		# Convert snakes to a list of tuples
		snakes = []
		for i in range(0,len(snakeData)//2):
			snakes.append( (snakeData[2*i], snakeData[2*i+1]) )
		
		# Convert ladders to a list of tuples
		ladders = []
		for i in range(0,len(ladderData)//2):
			ladders.append( (ladderData[2*i], ladderData[2*i+1]) )
		newBoard = SL_Board.SL_Board(size,snakes,ladders)
		return newBoard

# Do not change anything below here. 		
if __name__ == "__main__":
	main()