def main():
    salsa = []
    sales = []
    for i in range(5):
        jar = input("Please enter the types of salsas. " )
        salsa.append(jar)
        sale = float(input("Please enter the sales from the corresponding salsa"))
        sales.append(sale)
        
    if sales[0] > sales[1]:
        maximum = sales[0]
        minimum = sales[1]
        max_name = salsa[0]
        min_name = salsa[1]
    else:
        maximum = sales[1]
        minimum = sales[0]
        max_name = salsa[1]
        min_name = sales[0]
    for i in range(2,5):
        if sales[i] > maximum:
            maximum = sales[i]
            max_name = salsa[i]
        elif sales[i] < minimum:
            minimum = sales[i]
            min_name = salsa[i]

    print("The salsa with the highest sale is ", max_name)
    print("The salsa with the lowest sale is ", min_name)
   
main()
