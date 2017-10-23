def main():
    totalRainfall = []
    for i in range(12):
        monthlyRainfall = float(input("Please enter the amount of the rainfall for this month. " ))
        while monthlyRainfall < 0:
            monthlyRainfall = float(input("Error: Amount of rainfall must be greater than 0. " ))
        totalRainfall.append(monthlyRainfall)

    print(totalRainfall)
    sumRainfall = sum(totalRainfall)
    print(sumRainfall)
    averageRainfall = sumRainfall / 12
    
    print("The average rainfall is" , averageRainfall)
    
    if totalRainfall[0] > totalRainfall[1]:
        maximum = totalRainfall[0]
        minimum = totalRainfall[1]
        
    else:
        maximum = totalRainfall[1]
        minimum = totalRainfall[0]
    for i in range(2,12):
        if totalRainfall[i] > maximum:
            maximum = totalRainfall[i]
        elif totalRainfall[i] < minimum:
            minimum = totalRainfall[i]
    print("The maximum rainfall is ", maximum)
    print("The minimum rainfall is ", minimum)
    
main()                 
