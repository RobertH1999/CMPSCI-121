class Animal:
	number_of_legs = 0
	def__init__(self, name, age):
		self.name = name
		self.age = age
		if self.age == 0:
			self.__id = self.__createID()
		else:
			self.__id = self.__createID() * age
			
	def __createID(self):
		return random.randint(199, 999)
	
	def setID(self, idnum):
		self.__id = id nm
		
