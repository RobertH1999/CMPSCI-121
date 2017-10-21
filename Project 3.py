"""
Purpose: Estimate the volume of the cheese with holes in it. 
Input needed: The dimensions of the cheese, the radius of the holes,
              radius and height of cylinder.  
              the number of number of holes.  
Expected output: Volume of the cheese.
Algorithm:
Volume of cheese: length * width * height
Volume of spheres: 4/3 * pi * r^2
Volume of cylinder: pi * r^2*h

1.) Create a function that checks user input. If the value is less than or equal to zero then display error message. 

Test data:
"""
pi = 3.14159
def main():

    height = float(input("Enter a value for the height of the cheese. "))
    height = CheckValue(height, "height of cheese")
    
    length = float(input("Enter a value for the length of the cheese. "))
    length = CheckValue(length, "length of cheese")
    
    width = float(input("Enter a value for the width of the cheese. "))
    width = CheckValue(width, "width of cheese")
    
    

    numsphere = float(input("How many spherical bubbles are present?"))
    numsphere = CheckValue(numsphere, "number of spheres")
    
    radiusSphere = float(input("What is the radius of the spherical bubbles in centimeters? "))
    radiusSphere = CheckValue(radiusSphere, "radius of sphere")

    numCylinder = float(input("How many cylinders are present?"))
    numCylinder = CheckValue(numCylinder, "number of cylinders")

    radiusCylinder = float(input("What is the radius of the cylinders in centimeters? "))
    radiusCylinder = CheckValue(radiusCylinder, "radius of cylinder")

    heightCylinder = float(input("What is the height of the cylinders in centimeters?"))
    heightCylinder = CheckValue(heightCylinder, "height of the cylinder")
    
    sphereVolume = numsphere * 4/3 * pi * (radiusSphere**3)
    print(sphereVolume, numsphere, radiusSphere, radiusSphere**3)
    rectangleVolume = height * width * length
    print(rectangleVolume)
    cylinderVolume = numCylinder * pi * radiusCylinder ** 2 * heightCylinder
    print(cylinderVolume)
    cheeseVolume = rectangleVolume - cylinderVolume - sphereVolume
    print("The total volume of the cheese present is ", cheeseVolume, "cubic centimeters. ")
    
def CheckValue(value, what):
    while value < 0:
        print("The value for the", what, "The value must be greater than zero!")
        value = float(input("Enter a value greater than or equal to zero. " + what))
    return value

main()

