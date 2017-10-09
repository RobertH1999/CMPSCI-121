## Program that will calculate distance that an object falls from given
## and the kinetic energy of an object in motion given the mass and the velocity.

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

## function to calculate kinetic of a moving object given its mass and velocity.
## input: mass and velocity will be passed to the function from the function call.
## output: the kinetic energy will be returned to the fucntion call.
## processing: KE is 0.mv^2

def KE(mass, velocity):
    kineng= 0.5 * mass * velocity **2
    return kineng

## function to check user's input and prompt user to re-enter when less than or equal to 0.
## input: value to be checked description of the value(time, mass, velocity)
## output: a value greater than 0 will returned to the call.
## processing: use a while loop that will keep asking the user to re-enter as long an invalid value is entered. 

def checkinput(value, what):
    while value < 0:
        print("The", what, "cannot be less than or equal to zero.")
        value = float(input("Enter a new value for " + what + " "))
    return value    

    
def main():
    choice = input(" Enter 'd' to calculate the distance an object fell or 'KE'  to calculate the kinetic energy. ")
    if choice == 'd':
        seconds = float(input('Enter the seconds the object fell. '))
        seconds = checkinput(seconds, "time")
        d = distance(seconds)      # function call
        print("The object fell", d," meter in", seconds, "seconds.")
    else:
        m = float(input("Enter the mass of the object. "))
        m = checkinput(m, "mass")
        v = float(input("Enter the velocity of the object." ))
        v = checkinput(v, "velocity")
        ke = KE(m, v) 
        print("The kinetic energy of an object whose mass ", m, "and velocity is", v, "is", ke, ".")
        
main()

