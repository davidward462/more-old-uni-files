#student class

class student():
	def __init__ (self, name = "null", id = "null"):
		self.__name = name
		self.__id = id
		self.__courses = []
		self.__major = "undeclared"
	'''	
	def __str__ (self):
		return self.__name + " " + self.__id + " " + self.__courses + " " + self.__major
	'''	
	def setName(self, name):
		self.__name = name
		
	def setId(self, id):
		self.__id = id
		
	def getName(self):
		return self.__name
		
	def getId(self):
		return self.__id
		
	def declareMajor(major):
		self.__major = major
		
	def addCourse(course):
		self.__courses.append(course)
		
	def dropCourse(course):
		self.__courses.remove(course)
		
	def getMajor(self):
		return self.__major

	def getCourses(self):
		return self.__courses
		
		
		
def main():

	bob = student()
	alice = student()
	print(bob)
	print(alice)


main()
	
	
		
		