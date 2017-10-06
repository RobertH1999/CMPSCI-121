"""
Write a program that asks the user to enter the total sales for the month. From this figure, the application should calculate 
and display the following:
1. The amount of county sales tax
2. Amount of state sales tax
3. The total sales tax (county plus state)
"""

def main():
    total_sales = int(input("Enter the total sales for the month. "))
    while total_sales < 0:
    	total_sales = int(input("ERROR: The total sales for the month must be a nonnegative value."))
    display_taxes(total_sales)

def county_tax(total_sales):
    county_tax_rate = 0.025
    return total_sales * county_tax_rate
	
def state_tax(total_sales):
    state_tax_rate = 0.05
    return total_sales * state_tax_rate
	
def taxes(total_sales):
    total = county_tax + state_tax
	
def display_taxes(total_sales):
    countytax = county_tax(total_sales)
    statetax = state_tax(total_sales)
    print("The total sales is: ", total_sales, ".")
    print("The amount of county sales taxes is: ", countytax,".")
    print("The amount of state sales taxes is: ", statetax, ".")
    
main()
	
