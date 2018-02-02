# Will find the age of the person, withdraw, deposit money, and check balance of bank accountg
# Author: Rob
import datetime

class Person:
	def __init__(self, name, birthdate, phone, balance=0):
		self.name = name
		self.birthdate = birthdate
		self.phone = phone
		self.balance = balance
	def age(self):
		today = datetime.date.today()
		month, day, year = self.birthdate.split("/")
		age = today.year - int(year)
		
		if today < daytime.date(int(year),int(month),int(day)):
			age-=1
		return age
	
	def withdraw(self, amount):
		if amount > self.balance:
			return "You don't have enough money"
		self.balance -= amount
			
	def deposit(self, amount):
		return self.balance += amount
	
	def check_balance(self):
		return self.balance
	
