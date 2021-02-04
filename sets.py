#sets

def main():

	commands = ["help", "write", "stop", "view", "run", "delete"]
	
	cmdSet = set(commands)
	
	print(cmdSet)
	
	for cmd in cmdSet:
		print(cmd)
	
	
	team1 = [1, 3, 5, 7, 9]
	team2 = [2, 4, 6, 7, 8, 10]
	
	team1Set = set(team1)
	team2Set = set(team2)
	
	print(team1Set.intersection(team2Set))
	
	

main()