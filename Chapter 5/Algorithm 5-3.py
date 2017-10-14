"""Program 3:
  Describe a function that will prompt the user to enter 50 whole numbers
 and count
how many even and odd numbers were entered (
0 should be considered an even number).  The
function should employ a print statement to output the results.
"""
def main():
    even_number = 0
    odd_number = 0
    for i in range(5):
        number = int(input("Please enter a whole number. "))
        while number < 0:
            number = int(input("ERROR: Please enter a whole number. "))
        if number % 2 == 0:
            even_number +=1
        else:
            odd_number +=1
    print("Number of even values: ",even_number,"Number of odd values: ", odd_number)
main()


