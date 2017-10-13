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
    print(num_quarters)
    change1 = money % quarters
    print(change1)
    num_dimes = change1 // dimes
    print(num_dimes)
    change2 = change1 % dimes
    print(change2)
    num_nickels = change2 // nickels
    print(num_nickels)
    change3 = change2 % nickels
    print(change3)
    num_pennies = change3 // pennies
    print(num_pennies)

    return num_quarters, num_dimes, num_nickels, num_pennies
   
    
def main():
    money_incoins = float(input("Please enter the amount of change needed. "))
    while money_incoins <= 0:
        money_incoins = float(input("ERROR: The amount of change needs to be nonnegative."))
    numq, numd, numn, nump = exchange(money_incoins)	
    print("The change can be converted to", numq, "quarters", numd, "dimes", numn, "nickels", nump, "pennies. ")    
    print(exchange(money_incoins))
    
main()

	
	
