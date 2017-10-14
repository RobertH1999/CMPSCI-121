def main():
    number1 = float(input("Please input a value. "))
    number2 = float(input("Please input a value. "))
    number3 = float(input("Please input a value. "))
  
    number1, number2, number3 = order(number1, number2, number3)
    print(number1, number2, number3)
    
def order(num1, num2, num3):
    temp = 0
    if num1 > num2:
        temp = num2
        num2 = num1
        num1 = temp
    if num2 > num3:
        temp = num3
        num3 = num2
        num2 = temp
    if num1 > num2:
        temp = num2
        num2 = num1
        num1 = temp
    return num1, num2, num3

main()
