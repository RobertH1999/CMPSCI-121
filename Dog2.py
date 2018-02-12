class Dog:
	number_of_legs= 0
	count = 0
	def __init__(self, name, breed, size, age):
		self.name = name
		self.breed = breed
		self.size = size
		self.age = age
		Dog.count +=1
		
	def howMany(self):
		return Dog.count
	def eat(self):
		print(self.name + " is eating")
	def sleep(self):
		print(self.name + " is sleeping")
	def sit(self):
		print(self.name + " is sitting")
	def roll_over(self):
		print(self.name + " is rolling over")
	def run(self):
		print(self.name + " is running")
	def __str__(self):
		return "{} is a {} year old {}!".format(self.name, 
		self.age, self.breed)
__repr__=__str__
