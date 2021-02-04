#Player class for 110 assignment 6
import random
import string

class Player():
	def __init__ (self):
		self.__name = ""
		self.__symbol = ""
		self.__position = 1
	
	def set_name (self, name):
		self.__name = name
		
	def set_symbol (self):
		string.ascii_letters
		choice = random.choice(string.ascii_letters)
		self.__symbol = choice #add symbol generation code
		
	def set_position (self, position):
		self.__position = position
	
	def get_name (self):
		return self.__name
		
	def get_symbol (self):
		return self.__symbol
		
	def get_position (self):
		return self.__position
		
	def __str__ (self):	
		return self.__name + "("+ self.__symbol + "):" + self.__position
		
	
	
	