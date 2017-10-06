"""
Purpose: 
Write a function named falling_distance that accepts an object's falling time (in seconds) as an argument. The function should return the distance, in meters, that the object has fallen during that time interval. Write a program that calls the function in a loop that passes the values 1 through 10 as arguments and displays the return value.
"""
g = 9.8

falling_distance():
	d = 1/2*g*t**2
t = 1
while t < 11: 
	print(d)
	t+=1
