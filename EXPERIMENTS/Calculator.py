"""This is a multi purpose calculator that can add, subtract, multiply, divide and all of the other basic functions. This calculator can also calculate your GPA and your grades. 

In the works:
1. GPA_Calculator():
2. Grade_Converter():
3. Statistics_Calculator():
4. Graphing function
5. A visual calculator
6. button()

Multiple input calculations. 
"""

print("""Menu:
	1. Addition
	2. Subtraction
	3. Multiplication
	4. Division
	5. Division w/o remainder
	6. GPA Calculator
	7. Grade Converter
	8. Statistics Calculator""")
	
calc_function = int(input("Please enter what calculator function you would like to have. "))
while calc_function < 1 or calc_function > 8:
	try:
		calc_function = int(input("ERROR: The integer must be between 1 and 8, inclusively. "))
	except ValueError: 
		print("The number you entered is not an integer.")
if calc_function == 1:
	try:
	except:	
elif calc_function == 2:
	try:
	except:	
elif calc_function == 3:
	try:
	except:	
elif calc_function == 4:
	try:
	except:	
elif calc_function == 5:
	try:
	exception:	
elif calc_function == 6:
	try:
	except:	
elif calc_function == 7:
	try:
	except:	
else: 
	try:
	except:	
Addition(x1, x2):
	x1 = float(input("Please enter a value for x1 " ))
	x2 = float(input("Please enter a value for x2. "))
	total = x1 + x2
	print(total)
	
Subtraction(x1, x2):
	x1 = float(input("Please enter a value for x1 " ))
	x2 = float(input("Please enter a value for x2. "))
	total = x1 - x2
	print(total)
	
Multiplication(x1, x2):
	x1 = int(input("Please enter a value for x1 " ))
	x2 = int(input("Please enter a value for x2. "))
	total = x1 * x2
	print(total)
	
Division_No_Remainder(x1, x2):
	x1 = int(input("Please enter a value for x1 " ))
	x2 = int(input("Please enter a value for x2. "))
	total = x1//x2
	print(total)
	
GPA_Calculator(grade1, grade2, grade3, grade4, grade5):
	try:
		grade1 = float(input("Please enter your grade for class 1. "))
	exception:
	try:
		grade2 = float(input("Please enter your grade for class 2. "))
	try:
		grade3 = 
	try:
		grade4 =
	exception:
	try:
		grade5 =
	exception:
	
Grade_Converter():
Statistics_Calculator():
