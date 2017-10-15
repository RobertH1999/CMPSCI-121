"""
"""
yearlyInterestRate = float(input("What is the yearly interest rate for the credit card entered as a percent? "))
while yearlyInterestRate < 1 or interest_rate > 30:
    yearlyInterestRate = float(input("Error: The yearly interest rate must be between 1 and 30. "))
previous_balance = 0
print("The balance from the previous month was ${:,.2f}.".format(previous_balance))

monthlyInterestRate = yearlyInterestRate / 12
totalInterest = montlyInterestRate * 0.01 * previous_balance
