"""Problem 2:
  Describe a function that would accept 7 values from the function call and determine 
the minimum and maximum of those 7 values. Design this function without using the idea of 
arrays or lists.  Send back to the function call the minimum and maximum value.  (Hint
, you 
should use no more than 7 comparisons to find the maximum and no more than 7 comparisons to 
find the minimum.)
"""

def main():
    num1 = int(input("Please enter a value for num1. "))
    num2 = int(input("Please enter a value for num2. "))
    num3 = int(input("Please enter a value for num3. "))
    num4 = int(input("Please enter a value for num4. "))
    num5 = int(input("Please enter a value for num5. "))
    num6 = int(input("Please enter a value for num6. "))
    num7 = int(input("Please enter a value for num7. "))

    min_, max_ = min_max(x1,x2,x3,x4,x5,x6,x7)

    print(min_, max_)
    
def min_max(y1,y2,y3,y4,y5,y6,y7):
    if y1 > y2:
        maximum = y1
        minimum = y2
    else:
        maximum = y2
        minimum = y1
    if y3 > maximum:
        maximum = y3
    elif y3 < minimum:
            minimum = y3
    if y4 > maximum:
        maximum = y4
    elif y4 < minimum:
            minimum = y4
    if y5 > maximum:
        maximum = y5
    elif y5 < minimum:
            minimum = y5
    if y6 > maximum:
        maximum = y6
    elif y6 < minimum:
            minimum = y6
    if y7 > maximum:
        maximum = y7
    elif y7 < minimum:
            minimum = y7

    return minimum, maximum

main()
