#phone book

def changeEntry(phonebook):
	#print("Change")
	key = input("Enter key: ")
	if key in phonebook:
		value = int(input("Enter value: "))
		phonebook[key] = value
		print(phonebook)
	else:
		print("Item not present.")
	
def addEntry(phonebook):
	#print("Add")
	key = input("Enter key: ")
	if key not in phonebook:
		value = int(input("Enter value: "))
		phonebook[key] = value
		print(phonebook)
	else:
		print("Item already present.")

def removeEntry(phonebook):
	#print("Remove")
	key = input("Enter key: ")
	if key in phonebook:
		del phonebook[key]
		print("%s has been removed." % key)
	else:
		print("Item not present.")

def search(phonebook):
	#print("Search")
	key = input("Enter key: ")
	if key in phonebook:
		print("%s has value %d." % (key, phonebook[key]))
	else:
		print("Item not present.")
	
def view(phonebook):
	print(phonebook)
	
def clear(phonebook):
	#print("Clears the phonebook.")
	yesNo = input("Are you sure you want to delete the entire phonebook? " )
	if yesNo == 'y':
		phonebook.clear()
		print("Phonebook has been cleared.")
	else: 
		print("That was close.")

def help():
	print("Commands:\n")
	print("add, remove, search, change, view, clear, exit, help.")
	
def main():

	print("PHONEBOOK")
	phonebook = {"Bob":492, "Carl":395, "Dylan":192, "Jenny":932}

	run = True
	while run:
		command = input("\nEnter command: ")
		if command == "exit":
			run = False
		elif command == "add":
			addEntry(phonebook)
		elif command == "remove":
			removeEntry(phonebook)
		elif command == "search":
			search(phonebook)
		elif command == "change":
			changeEntry(phonebook)
		elif command == "view":
			view(phonebook)
		elif command == "clear":
			clear(phonebook)
		elif command == "help":
			help()
		else:
			print("Unknown command. Type 'help' for list of commands.")
		


main()