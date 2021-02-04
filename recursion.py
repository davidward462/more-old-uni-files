#recursion

def message(times):
	if times > 0:
		print("Message")
		message(times - 1)

def main():

	message(5)

main()