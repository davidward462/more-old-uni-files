#string operations

def search(string):
	search = input("Search for: ")
	for character in string:
		if character == search:
			print(character)
			
def split(string):
	words = string.split(" ")
	return words
	

def main():

	string1 = "hello"
	string2 = "the quick fox jumped over the lazy brown dog"

	words = split(string2)
	print(words)
	#search(string2)

main()