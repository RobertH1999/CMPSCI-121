## Program that will calculate distance that an object falls from given
## and the kinetic energy of an object in motino given the mass and the velocity.

## input: For the distance, input is time, for kinetic energy the input is mass and
## velocity

## Output: the distance or the kinetic energy
## Processing: d = 1/2gt^2 where g is 9.8, KE = 1/2mv^2
##             The program will employ 4 functions: one to calculate the distance,
##             one to calculate the kinetic energy, one to check input, and main.
##             The main function will prompt the user to choose which calculation
##             to employ, the prompt the user to enter the needed values, call the function
##             to check the values, call the appropriate function.
##             the calculation, and output the result.

## function to calculate the distance an object falls
## input: time of fall is passsed to the function from the function call
## output: distance object fell is returned to the function call
## processing: d = 0.5gt^2

def distance(time):
    g = 9.8
    dist = 0.5 * g * time**2
    return dist

def main():
    choice = input(" Enter 'd' to calculate the distance an object fell or 'KE'  to calculate the kinetic energy. ")
    if choice == 'd':
        seconds = float(input('Enter the seconds the object fell. '))
        d = distance(seconds)      # function call
        print("The object fell", d," meter in", seconds, ".")
main()
