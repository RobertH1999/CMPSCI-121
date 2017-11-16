"""
Purpose: Find the following things:
         Average annual change in population
         The year with the greatest increase
         The year with the smallest increase in population
Input: Read lines from text file
Output: The average annual change in population during the period, greatest and lowest increase in population. 
Algorithm:
        1. Initialize a total and count variable to 0.
        2. Create two empty lists called pop and change.
        1. Read file into the program
        4. Read data into pop list
        5. Each time a line is read, increase count by 1. 
        6. Insert the number in to the list.
        7. To find the change, subtract the current number by previous number.
           Do this for each number in the list starting with second number.
           Add each change to the change list
        8. Sum all the values in the change list
        9. To find the average, divide the total by the count - 1.
        10. Find the minimum change and maximum change using the min and max function
        11. Find the corresponding index for the minimum and maximum change and add 1951.
        12. Print average change, year with smallest change, and year with greatest change
"""
#Initialize a total and count variable to 0.
total = 0
count = 0

#Create two empty lists called pop and change.
pop = []
change = []

#Read file into the program
infile = open(r"E:\CMPSC121\USPopulation.txt", "r")

#Read data into pop list
#Each time a line is read, increase count by 1. 
for line in infile:
    population = float(line)
    pop.append(population)
    count += 1
    
#To find the change, subtract the current number by previous number.
#Do this for each number in the list starting with second number.
#Add each change to the change list
for i in range(count-1):
    annualchange = pop[i+1] - pop[i]
    change.append(annualchange)

#Sum all the values in the change list
total = sum(change)

#To find the average, divide the total by the count - 1. 
average = total / (count - 1)

#Find the minimum change and maximum change using the min and max function
maxPopulation = max(change)
minPopulation = min(change)

#Find the corresponding index and add 1951.
for j in range(count - 1):
    if change[j] == maxPopulation:
        maxyear = j + 1951
    if change[j] == minPopulation:
        minyear = j + 1951
#Print average change, year with smallest change, and year with greatest change
print ("The average annual change in population during the time period is {:.1f}. ".format(average))
print("The smallest annual change in population during the time period is in {0:3.0f}. ".format(minyear))
print("The greatest annual change in population during the time period is in {0:3.0f}. ".format(maxyear))              

