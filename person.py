import datetime

class Person:
	def __init__(self, name, birthdate, phone):
		self.name = name
		self.birthdate = birthdate
		self.phone = phone
	def age(self):
		today = datetime.date.today()
		month, day, year = self.birthdate.split("/")
		age = today.year - int(year)
		
		if today < daytime.date(int(year),int(month),int(day)):
			age-=1
		return age
	
