"""
Purpose: Estimate the volume of the rectangular chunk of Swiss cheese. Assume the holes
are sphereical or cylinders. 
Input needed: The dimensions of the cheese, the radius of the holes,
              radius and height of cylinder.  
              the number of number of holes.  
Expected output: Volume of the cheese.
Algorithm:
Volume of cheese: length * width * height
Volume of spheres: 4/3 * pi * r^2
Volume of cylinder: pi * r^2*h

In main function:
    1. Ask input to input the height, length, number of spheres, number of cylinders, radius of cylinder, and height of cylinder
       Check if each value is greater than zero. If the value is less than zero, then display error message and prompt user to enter a valid input. 
       In a function called volumeSphere, receive the parameters nspheres and rspheres. Calculate the formula using sphereVolume = nsphere *4/3 * pi *rsphere ** 3
       Afterwards, return the value sphereVolume.
    2. Call the cheeseVolume function
    3. Display the total volume of the cheese in cubic centimeters.
In volumeSphere function:
    1. Receive the parameters nsphere and rsphere.
    2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3
    3. Return the value back to sphereVolume

In volumeCylinder function:
    1. Receive the parameters nCylinder and rCylinder, and hCylinder.
    2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3
    3. Return the value back to sphereVolume

In volumeRectangle function:
    1. Receive the parameters nsphere and rsphere.
    2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3
    3. Return the value back to RectangleVolume
In volumeCheese function:
    1. Receive the parameters hRectangle,wRectangle,lRectangle, numSphere, radSphere, numcylinder, radiuscylinder, heightcylinder.
    2. Call the functions from above.
    3. cheesevolume = rVolume - cVolume - sVolume, where rVolume is the volume of the rectangle, cVolume is the volume of cylinders, and sVolume is the volume of sphere.
In CheckValue function:
    1. Receive the value
    2. If the value is less than 0, display error message and ask user to reenter a valid input.
    3. Return to value. 
In BubbleCheck function:
    1. Receive the nbubbles value and enter what you are comparing(number of spheres / cylinders) and
    2. If the value is less than 0, display error message and ask user to reenter a valid input.
    3. Return to nbubbles
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
    numsphere = BubbleCheck(numsphere, "number of spheres")
    
    radiusSphere = float(input("What is the radius of the spherical bubbles in centimeters? "))
    radiusSphere = CheckValue(radiusSphere, "radius of sphere")

    numCylinder = float(input("How many cylinders are present?"))
    numCylinder = BubbleCheck(numCylinder, "number of cylinders")

    radiusCylinder = float(input("What is the radius of the cylinders in centimeters? "))
    radiusCylinder = CheckValue(radiusCylinder, "radius of cylinder")

    heightCylinder = float(input("What is the height of the cylinders in centimeters?"))
    heightCylinder = CheckValue(heightCylinder, "height of the cylinder")
    
    cheeseVolume = volumeCheese(height,width,length, numsphere, radiusSphere, numCylinder, radiusCylinder, heightCylinder)
    print("The total volume of the cheese present is ", cheeseVolume, "cubic centimeters. ")

# Receive the parameters and find the volume of the sphere.
# Volume of a sphere is number of spheres * 4/3 * pi * radius of sphere ^ 3
# Return the value to sphereVolume.

def volumeSphere(nsphere, rsphere):
    sphereVolume = nsphere * 4/3 * pi * rsphere**3
    return sphereVolume

# Receive the parameters and find the volume of the cylinder.
# Volume of a cylinder is number of cylinders * pi * radius of cylinder ^ 2 * height of cylinder
# Return the value to cylinderVolume.

def volumeCylinder(nCylinder, rCylinder, hCylinder):
    cylinderVolume = nCylinder * pi * rCylinder ** 2 * hCylinder
    return cylinderVolume

# Receive the parameters and find the volume of the rectangle.
# Volume of rectangle is height * width * length
# Return the value to rectangleVolume. 
def volumeRectangle(h,w,l):
    rectangleVolume = h * w * l
    return rectangleVolume

# Receive the parameters and find the volume of the cheese. Return the value to volume. 
def volumeCheese(hRectangle,wRectangle,lRectangle, numSphere, radSphere, numcylinder, radiuscylinder, heightcylinder):
    sVolume = volumeSphere(numSphere, radSphere)
    cVolume = volumeCylinder(numcylinder, radiuscylinder, heightcylinder)
    rVolume = volumeRectangle(hRectangle,wRectangle,lRectangle)

    cheesevolume = rVolume - cVolume - sVolume
    return cheesevolume

# Check if the inputted value is greater than zero. If not, then display error message and tell them to enter a valid value. 
def CheckValue(value, what):
    while value < 0:
        print("The value for the", what, "The value must be greater than zero!")
        value = float(input("Enter a value greater than or equal to zero. " + what))
    return value

# Check the number of bubbles for sphere and cylinder
def BubbleCheck(nbubbles, thing):
    while nbubbles < 0:
        print("The value for the", thing, "The value must be greater than zero!")
        nbubbles = float(input("Enter a value greater than or equal to zero. " + thing))
    return nbubbles
main()

