"""Program 3:
  Describe a function that will prompt the user to enter 50 whole numbers
 and count 
how many even and odd numbers were entered (
0 should be considered an even number).  The 
function should employ a print statement to output the results.  
"""
def main():
	num_decision = even_or_odd(num)
	print(num_decision)
		
def even_or_odd(number):
	for i in range(50):
		number = int(input("Please enter a whole number. "))
		while number < 0:
			number = int(input("ERROR: Please enter a whole number. "))
			
		even = 0
		odd = 0
		if number %2 == 0:
			even_number +=1
		else:
			oddnumber +=1
	
main()
