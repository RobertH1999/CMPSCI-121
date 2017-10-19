## Robert Hsu
## CMPSCI 121 - Fall 2017

"""
Purpose: The program will help the user to estimate credit card payments and interest.
Input: User will enter the yearly interest rate as a percentage.
Output: The output will be the total interest paid. If the user paid
        more than the current balance, then a credit should be output.
Algorithm:
In the main function:
    1. Set both the total interest and current balance as zero.
    2. Ask user to enter the yearly interest rate. If the yearly interest rate is less than 1 or more than 30, display error message
       and tell user to input a valid value.
    3. Calculate the monthly interest rate by dividing the yearly interest rate by 12.
    4. Calculate the monthly interest by multiplying the monthly interest rate and current balance and 0.01 and round it to the nearest cent
    5. Calculate the total interest by adding monthly interest to total interest. 
    6. Print the monthly interest applied to the account last month.
    7. Ask the user to input the total charges for the month. If the total charges is less than 0, display error message
       and ask user to enter a valid input.
    8. To calculate the new current balance, add the current balance, monthly interest, and total charges together.
    9. Display the current balance.
    10. Calculate the minimum payment. Compare the current balance to 10. If the current balance is greater than or equal to 10
        then compare 0.075 * current balance to 10 dollars. If the 0.075 * current balance is greater than 10, then the minimum payment is 0.075 * current payment
        rounded to the nearest cent. If the 0.075 * current balance is less than 10, then the minimum payment is 10. If the current balance is less than 10 dollars
        then the minimum payment is the current balance. 
    11. Prompt the user to input the amount of he/she would like to pay.
        If the amount is less than zero or less than minimum payment, display error message.
In a function: 
    1. Create a rounding function that will round a value to the nearest cent. The function will receive a value, multiply the value by 100 and add 0.5
       Set the current value as an integer. 

Test Data:
I used the same test data as the examples in the problem. 
"""


def main():
    # Set total interest and current balance as zero. 
    totalInterest = 0
    currentBalance = 0
    yearlyInterestRate = float(input("What is the yearly interest rate for the credit card entered as a percent? "))
    while yearlyInterestRate < 1 or yearlyInterestRate > 30:
        print("Error: The yearly interest rate must be between 1 and 30 percent! ")
        yearlyInterestRate = float(input("What is the yearly interest rate for the credit card entered as a percent? "))
    print("\n")

    print("The balance from the previous month was ${:,.2f}.".format(currentBalance))
    # Calculate the monthly interest rate. 
    monthlyInterestRate = yearlyInterestRate / 12
    monthlyInterest = rounding(monthlyInterestRate * 0.01 * currentBalance)
    # Add the monthly interest to the total interest for every month. 
    totalInterest += monthlyInterest
    print("There was ${:,.2f}.".format(monthlyInterest), "applied to your account last month.")
    # Ask the user to input the total charges. If the input is invalid, display error message. 
    totalCharges = float(input("What were the total charges for this month? "))
    while totalCharges < 0:
        print("New charges must be greater than or equal to $0.00 ")
        totalCharges = float(input("What were the total charges for this month? "))
    currentBalance = currentBalance + monthlyInterest + totalCharges

    print("Your current balance is ${:,.2f}.".format(currentBalance))
    # Determine the minimum balance. 
    if currentBalance >= 10:
        if 0.075 * currentBalance > 10:
            minimumPayment = rounding(0.075 * currentBalance)
        else:
            minimumPayment = 10
    else:
        minimumPayment = currentBalance
    print("The minimum payment for this month is ${:,.2f}.".format(minimumPayment))
    # Ask the user to input the amount he/she would like to pay. 
    youPay = float(input("How much would you like to pay this month? "))
    while youPay < 0 or youPay < minimumPayment:
        print("You MUST make at least the minimum payment of ${:,.2f).".format(minimumPayment))
        youPay = float(input("How much would you like to pay this month? "))
    print("\n")
    currentBalance -= youPay
    print("The balance from the previous month was ${:,.2f}.".format(currentBalance))

    # Repeat once the current balance is greater than zero. 
    while currentBalance > 0:
        monthlyInterestRate = yearlyInterestRate / 12
        monthlyInterest = rounding(monthlyInterestRate * 0.01 * currentBalance)
        totalInterest += monthlyInterest
        print("There was ${:,.2f}.".format(monthlyInterest), "applied to your account last month.")
    
        totalCharges = float(input("What were the total charges for this month? "))
        while totalCharges < 0:
            print("New charges must be greater than or equal to $0.00 ")
            totalCharges = float(input("What were the total charges for this month? "))
        currentBalance = currentBalance + monthlyInterest + totalCharges

        print("Your current balance is ${:,.2f}.".format(currentBalance))

        if currentBalance >= 10:
            if 0.075 * currentBalance > 10:
                minimumPayment = rounding(0.075 * currentBalance)
            else:
                minimumPayment = 10
        else:
            minimumPayment = currentBalance
        print("The minimum payment for this month is ${:,.2f}.".format(minimumPayment))

        youPay = float(input("How much would you like to pay this month? "))
        while youPay < 0 or youPay < minimumPayment:
            print("You MUST make at least the minimum payment of ${:,.2f}.".format(minimumPayment))
            youPay = float(input("How much would you like to pay this month? "))
        print("\n")
        currentBalance -= youPay
        
    print("\n")
    print("Your account has been paid off!")
    print("You paid a total of ${:,.2f}.".format(totalInterest), "in interest.")
    if rounding(currentBalance) < 0:
        currentBalance = rounding(currentBalance) * -1
        print("You currently have a credit of ${:,.2f}.".format(currentBalance))
    print("Press any key to continue. . .  ") 

# This function will round a value to the nearest cent. 
def rounding(value):
    value = int(value * 100 + 0.5)
    return value * 0.01

# Execute the main function. 
main()

