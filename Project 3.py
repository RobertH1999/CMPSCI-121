"""
Robert Hsu
CMPSCI 121 - Fall 2017

Purpose: Estimate the volume of the Swiss cheese. The shape of the Swiss cheese is a rectangular hunk with spherical and cylindrical holes. 
To estimate the volume of Swiss cheese, we need to calculate the rectangular volume and subtract the holes from the rectangular volume. 
Input needed: 1. Height, length, and width of rectangle
              2. Number of spheres and cylinders
              3. Radius of cylinder and radius
              4. Height of Cylinder
Expected output: Volume of the cheese.
Algorithm:
Volume of cheese: Volume of rectangle - volume of spheres - volume of cylinder
Volume of rectangle: length * width * height. 
Volume of spheres: 4/3 * pi * r**2.
Volume of cylinder: pi * r**2 * h.

In addition to the main function, there are 6 additional functions to be created as follows 
In main function:
    1. Ask user to input the (1)height, (2)length, and (3) width for the rectangular hunk of Swiss cheese, (4)number of spheres, (5)radius of spheres (6)number of cylinders,
       (7)radius of cylinder, and (8)height of cylinder.
       Check if each value is greater than zero. If the value is less than zero, then display error message and prompt user to enter a valid input. 
       In a function called volumeSphere, receive the parameters nspheres and rspheres. Calculate the formula using sphereVolume = nsphere *4/3 * pi *rsphere ** 3.
       Afterwards, return the value sphereVolume.
    2. Call the cheeseVolume function.
    3. Display the total volume of the cheese in cubic centimeters.
In volumeSphere function:
    1. Receive the parameters nsphere and rsphere.
    2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3.
    3. Return the value back to sphereVolume.

In volumeCylinder function:
    1. Receive the parameters nCylinder and rCylinder, and hCylinder.
    2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3.
    3. Return the value back to sphereVolume.

In volumeRectangle function:
    1. Receive the parameters nsphere and rsphere.
    2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3.
    3. Return the value back to RectangleVolume.
In volumeCheese function:
    1. Receive the parameters hRectangle,wRectangle,lRectangle, numSphere, radSphere, numcylinder, radiuscylinder, heightcylinder.
    2. Call the functions from above.
    3. cheesevolume = rVolume - cVolume - sVolume, where rVolume is the volume of the rectangle, cVolume is the volume of cylinders, and sVolume is the volume of sphere.
In CheckValue function:
    1. Receive the value.
    2. If the value is less than 0, display error message and ask user to reenter a valid input.
    3. Return to value. 
In BubbleCheck function:
    1. Receive the nbubbles value.
    2. If the value is less than 0, display error message and ask user to reenter a valid input.
    3. Return to nbubbles.

Execute the main function.

Test Data:
    height: 25.8
    length: 40.67
    width: 35.5
    numsphere: 10
    radiusSphere: 1.2
    numCylinder: 8
    radiusCylinder: 0.8
    heightCylinder: 4

    The total volume of cheese present is 37,112.9 cubic centimeters. 
"""

# pi is a global constant. 
pi = 3.14159

# In main function, prompt user to input, height, length, width, numspheres, radiusSphere, numCylinder, heightCylinder.
# Calculate the cheese volume. 
def main():
    height = float(input("Enter the height of the hunk of cheese in centimeters. "))
    height = CheckValue(height, "height of hunk of cheese")
    
    length = float(input("Enter the length of the hunk of cheese in centimeters. "))
    length = CheckValue(length, "length of hunk of cheese")
    
    width = float(input("Enter the width of the hunk of cheese in centimeters. "))
    width = CheckValue(width, "width of hunk of cheese")

    numsphere = float(input("How many spherical bubbles are present? "))
    numsphere = BubbleCheck(numsphere, "number of spheres")
    
    radiusSphere = float(input("What is the radius of the spherical bubbles in centimeters? "))
    radiusSphere = CheckValue(radiusSphere, "radius of sphere")

    numCylinder = float(input("How many cylinders are present?"))
    numCylinder = BubbleCheck(numCylinder, "number of cylindrical holes")

    radiusCylinder = float(input("What is the radius of the cylinders in centimeters? "))
    radiusCylinder = CheckValue(radiusCylinder, "radius of cylinder")

    heightCylinder = float(input("What is the height of the cylinders in centimeters? "))
    heightCylinder = CheckValue(heightCylinder, "height of the cylinder")
    
    cheeseVolume = volumeCheese(height,width,length, numsphere, radiusSphere, numCylinder, radiusCylinder, heightCylinder)
    print("The total volume of cheese present is {:,.1f}".format(cheeseVolume), "cubic centimeters. ")

# 1. Receive the parameters nsphere and rsphere.
# 2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3
# 3. Return the value back to sphereVolume

def volumeSphere(nsphere, rsphere):
    sphereVolume = nsphere * 4/3 * pi * rsphere**3
    return sphereVolume


# 1. Receive the parameters nCylinder and rCylinder, and hCylinder.
# 2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3
# 3. Return the value back to sphereVolume

def volumeCylinder(nCylinder, rCylinder, hCylinder):
    cylinderVolume = nCylinder * pi * rCylinder ** 2 * hCylinder
    return cylinderVolume

# 1. Receive the parameters nsphere and rsphere.
# 2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3
# 3. Return the value back to RectangleVolume
def volumeRectangle(h,w,l):
    rectangleVolume = h * w * l
    return rectangleVolume

# 1. Receive the parameters hRectangle,wRectangle,lRectangle, numSphere, radSphere, numcylinder, radiuscylinder, heightcylinder.
# 2. Call the functions from above.
# 3. cheesevolume = rVolume - cVolume - sVolume, where rVolume is the volume of the rectangle, cVolume is the volume of cylinders, and sVolume is the volume of sphere. 
def volumeCheese(hRectangle,wRectangle,lRectangle, numSphere, radSphere, numcylinder, radiuscylinder, heightcylinder):
    sVolume = volumeSphere(numSphere, radSphere)
    cVolume = volumeCylinder(numcylinder, radiuscylinder, heightcylinder)
    rVolume = volumeRectangle(hRectangle,wRectangle,lRectangle)

    cheesevolume = rVolume - cVolume - sVolume
    return cheesevolume

# Check if the inputted value is greater than zero. If not, then display error message and tell user to enter a valid value. 
def CheckValue(value, what):
    while value < 0:
        print("The", what, "must be greater than zero!")
        value = float(input("Please re-enter the " + what + " of hunk of cheese. "))
    return value

# Check if the inputted value is greater than zero. If not, then display error message and tell user to enter a valid value. 
def BubbleCheck(nbubbles, thing):
    while nbubbles < 0:
        print("The", thing, "must be greater than zero!")
        nbubbles = float(input("Please re-enter the number of " + thing + ". "))
    return nbubbles
main()
