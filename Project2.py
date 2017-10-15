## Robert Hsu
## CMPSCI 121 - Fall 2017

"""
"""
totalInterest = 0
currentBalance = 0
yearlyInterestRate = float(input("What is the yearly interest rate for the credit card entered as a percent? "))
while yearlyInterestRate < 1 or yearlyInterestRate > 30:
    yearlyInterestRate = float(input("Error: The yearly interest rate must be between 1 and 30. "))
print("\n")

print("The balance from the previous month was ${:,.2f}.".format(currentBalance))

monthlyInterestRate = yearlyInterestRate / 12
monthlyInterest = monthlyInterestRate * 0.01 * currentBalance
totalinterest += monthlyInterest
print("There was ${:,.2f}.".format(monthlyInterest), "applied to your account last month.")

totalCharges = float(input("What were the total charges for this month? "))
currentBalance = currentBalance + monthlyInterest + totalCharges

print("Your current balance is ${:,.2f}.".format(currentBalance))

if currentBalance >= 10:
    if 0.075 * currentBalance > 10:
        minimumPayment = 0.075 * currentBalance
    else:
        minimumPayment = 10
else:
    minimumPayment = currentBalance
print("The minimum payment for this month is ${:,.2f}.".format(minimumPayment))

youPay = float(input("How much would you like to pay this month? "))
print("\n")
currentBalance -= youPay
print("The balance from the previous month was ${:,.2f}.".format(currentBalance))


while currentBalance > 0:
    monthlyInterestRate = yearlyInterestRate / 12
    monthlyInterest = monthlyInterestRate * 0.01 * currentBalance
    totalInterest += monthlyInterest
    print("There was ${:,.2f}.".format(monthlyInterest), "applied to your account last month.")

    totalCharges = float(input("What were the total charges for this month? "))
    currentBalance = currentBalance + monthlyInterest + totalCharges

    print("Your current balance is ${:,.2f}.".format(currentBalance))

    if currentBalance >= 10:
        if 0.075 * currentBalance > 10:
            minimumPayment = 0.075 * currentBalance
        else:
            minimumPayment = 10
    else:
        minimumPayment = currentBalance
    print("The minimum payment for this month is ${:,.2f}.".format(minimumPayment))

    youPay = float(input("How much would you like to pay this month? "))
    print("\n")
    currentBalance -= youPay
    print("The balance from the previous month was ${:,.2f}.".format(currentBalance))

print("Your account has been paid off!")
print("You paid a total of ${:,.2f}.".format(totalInterest))
if currentBalance < 0:
    print("You currently have a credit of ${:,.2f}.".format(currentBalance))
print("Press any key to continue.  .  .  ") 
