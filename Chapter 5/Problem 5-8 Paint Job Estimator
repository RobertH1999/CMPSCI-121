"""
Purpose: Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data:

1. The number of gallons of paint required.
2. The hours of labor required.
3. The cost of the paint.
4. The labor charges.
5. The total cost of the paint job. 

Input needed: 
"""

def main():
    wall_space = float(input("Please input the square feet of wall space to be painted. "))
    gallon_price = float(input("Please input the price of the paint per gallon. "))
    estimate(wall_space, gallon_price)

# This is where all the estimation takes place. 
def estimate(wall_space, gallon_price):
    num_gallon = wall_space / 112
    labor_hours = num_gallon * 8 
    totalpaintcost = gallon_price * num_gallon 
    laborcharge = 35 * labor_hours
    totalcost = laborcharge + totalpaintcost

    print("The number of gallons of paint required: ", num_gallon, ".")
    print("The hours of labor required is: ", labor_hours, ".")
    print("The cost of the paint is: ", totalpaintcost, ".")
    print("The labor charges: ",laborcharge, ".") 
    print ("The total price for this paint job is $", totalcost, ".")

main()
