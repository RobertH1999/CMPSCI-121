"""Program 3:
  Describe a function that will prompt the user to enter 50 whole numbers
 and count 
how many even and odd numbers were entered (
0 should be considered an even number).  The 
function should employ a print statement to output the results.  
"""
def main():
    for i in range(50):
	number = int(input("Please enter a whole number. "))
	while number < 0:
	    number = int(input("ERROR: Please enter a whole number. "))
	    
    even, odd = even_or_odd(number)
    print(even_or_odd(number))
		
def even_or_odd(num):
	 "))
			
		even_number = 0
		odd_number = 0
		if number % 2 == 0:
			even_number +=1
		else:
			odd_number +=1
		return even_number, odd_number	
	
main()
