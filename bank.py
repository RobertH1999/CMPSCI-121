import datetime
   

class SavingsAccount(Customer):
    def __init__(self, name, account_num, int_rate, balance):
        Customer.__init__(self, name, balance)
        self.__account_num = account_num
        self.__interest_rate = int_rate

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance

class CD(Customer):
    def __init__ (self, name, account_num, int_rate, balance, mat_date):
        Customer.__init__(self, name, balance)
        self.__account_num = account_num
        self.__interest_rate = int_rate
        self.__maturity_date = mat_date

    def set_account_num(self, account_num):
        self.__account_num = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    def get_account_num(self):
        return self.__account_num

    def get_interest_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance

    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    def get_maturity_date(self):
        return self.__maturity_date

    def get_interest(self, time, int_rate):
        if time == 3:
            int_rate = 0.015
            self.__balance *= (1 + int_rate*time)
        elif time == 6:
            int_rate = 0.0175
            self.__balance *= (1 + int_rate*time)
        elif time == 12:
            int_rate = 0.0225
            self.__balance *= (1 + int_rate*time)
        elif time == 18:
            int_rate == 0.025
            self.__balance *= (1 + int_rate*time)
        elif time == 24:
            int_rate == 0.03
            self.__balance *= (1 + int_rate*time)
        else:
            int_rate == 0.035
            self.__balance *= (1 + int_rate*time)

class Checking(Customer):
    def __init__(self, name, account_num
            
            
class Customer:
    def __init__(self,name,birthdate,phone,balance=0.0):
        self.name= name
        self.birthdate = birthdate
        self.phone = phone
        self.balance = balance

    def age(self):
        today=datetime.date.today()
        month, day, year = self.birthdate.split("/")
        age = today.year - int(year)

        if (today.month, today.day) < (int(month),int(day)):
            age-=1
        return age

    def withdraw(self, amount):
        if amount>self.balance:
            return "You don't have enough money"
        else:
            self.balance-=amount
            return self.balance

    def deposit(self, amount):
        self.balance+=amount
        return self.balance

    def check_balance(self):
        return self.balance 

    

