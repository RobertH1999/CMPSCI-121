""" Describe a function that will accept change needed from a purchase and 
will determine  the number of quarters, number of dimes, number of nickels, and number of pennies 
needed to make the change if you want to minimize the total number of coins used.  The number 
of each coin needed should be sent back to the function call.

Input needed: The amount of change.
Expected output: The minimum amount of pennies nickels, dimes, and quarters required. 
Algorithm: """



pennies = 0.01
nickels = 0.05
dimes = 0.10
quarters = 0.25



def exchange(money):
    num_quarters = money // quarters
    change1 = money % quarters
    num_dimes = change1 // dimes
    change2 = change1 % dimes
    num_nickels = change2 // nickels
    change3 = change2 // pennies
    num_pennies = change3// pennies

    return num_quarters, num_dimes, num_nickels, num_pennies
    print("The change can be converted to", num_quarters, "quarters", num_dimes, "dimes", num_nickels, "nickels", num_pennies, "pennies. ")
    
def main():
    money = float(input("Please enter the amount of change needed. "))
    while money < 0:
        money = float(input("ERROR: The amount of change needs to be positive."))
    exchange(money_incoins)	
        
main()

	
	
