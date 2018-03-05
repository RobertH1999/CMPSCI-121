import datetime
class Bank:
	def __init__(self, name, birthdate, phone, balance = 0.0):
		self.name = name
		self.birthdate = birthdate
		self.phone = phone
		self.balance = balance

	def get_age(self):
		today=datetime.date.today()
		month, day, year = self.birthdate.split("/")
		age = today.year - int(year)
		if (today.month, today.day) < (int(month),int(day)):
			age-=1
		return age
		
	
		
		
	
