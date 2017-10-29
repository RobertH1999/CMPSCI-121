"""
Purpose: Estimate the volume of the Swiss cheese. The shape of the Swiss cheese is a rectangular hunk with spherical and cylindrical holes. 
To estimate the volume of Swiss cheese, we need to calculate the rectangular volume and subtract the holes from the rectangular volume. 
Input needed: 1. Rectangle: height, length, and width
              2. Sphere: number of sphere, radius of sphere
              3. Cylinder: number of cylinders, radius of cylinder, height of cylinder
Expected output: Volume of the cheese in cubic centimeters.
Algorithm:
Volume of cheese: Volume of rectangle - volume of spheres - volume of cylinder
Volume of rectangle: length * width * height. 
Volume of spheres: 4/3 * pi * rSphere**2.
Volume of cylinder: pi * rCylinder**2 * hCylinder.

In addition to the main function, there are 6 additional functions to be created as follows 
In main function:
    1. (a) Ask user to input the (1)height, (2)length, and (3) width for the rectangular hunk of Swiss cheese, (4)number of spheres, (5)radius of spheres (6)number of cylinders,
           (7)radius of cylinder, and (8)height of cylinder.
       
       (b) Check if each value is greater than zero. If the value is less than zero, then display error message and prompt user to enter a valid input.
       
       (c) In a function called volumeSphere, receive the parameters nspheres and rspheres. Calculate the formula using sphereVolume = nsphere *4/3 * pi *rsphere ** 3.
       
       (d) Afterwards, return the value sphereVolume.
    2. Call the cheeseVolume function.
    3. Display the total volume of the cheese in cubic centimeters.
    
In volumeSphere function which is to calculate the total volume of sphere in the Swiss cheese:
    1. Receive the parameters nsphere and rsphere, where nsphere is the number of spheres and rsphere is the radius of the sphere
    2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3.
    3. Return sphereVolume.

In volumeCylinder function which is to calculate the total volume of cylinder in the Swiss cheese:
    1. Receive the parameters nCylinder and rCylinder, and hCylinder,
       where nCylinder is the number of cylinders, rCylinder is the radius of a cylinder, and hCylinder is the height of a cylinder.
    2. Use the equation cylinderVolume = nCylinder * pi * hCylinder * rCylinder**2.
    3. Return cylinderVolume.

In volumeRectangle function which is to calculate the total volume of rectangle in the Swiss cheese:
    1. Receive the parameters h , w, l, where h is the height of the rectangle, w is the width of the rectangle, and l is the length of the rectangle. 
    2. Use the equation rectangleVolume = h * w * l
    3. Return the value back to rectangleVolume.
    
In volumeCheese function which is to calculate the total volume of Swiss cheese:
    1. Receive the parameters hRectangle,wRectangle,lRectangle, numSphere, radSphere, numcylinder, radiuscylinder, heightcylinder.
    2. Call the functions from above.
    3. cheesevolume = rVolume - cVolume - sVolume, where rVolume is the volume of the rectangle, cVolume is the volume of cylinders, and sVolume is the volume of sphere.
    4. return cheesevolume
    
In CheckDimValue function which is to check value is greater than zero:
    1. Receive the value.
    2. If the value is less than or equal to 0, display error message and ask user to reenter a valid input.
    3. Return value.
    
In BubbleCheck function which is to check value is greater than zero:
    1. Receive the nbubbles value.
    2. If the value is less than or equal to 0, display error message and ask user to reenter a valid input.
    3. Return nbubbles.

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
    height = CheckDimValue(height, "height of hunk of cheese")
    
    length = float(input("Enter the length of the hunk of cheese in centimeters. "))
    length = CheckDimValue(length, "length of hunk of cheese")
    
    width = float(input("Enter the width of the hunk of cheese in centimeters. "))
    width = CheckDimValue(width, "width of hunk of cheese")

    numsphere = float(input("How many spherical bubbles are present? "))
    numsphere = BubbleCheck(numsphere, "number of spheres")
    
    radiusSphere = float(input("What is the radius of the spherical bubbles in centimeters? "))
    radiusSphere = CheckDimValue(radiusSphere, "radius of sphere")

    numCylinder = float(input("How many cylinders are present? "))
    numCylinder = BubbleCheck(numCylinder, "number of cylindrical holes")

    radiusCylinder = float(input("What is the radius of the cylinders in centimeters? "))
    radiusCylinder = CheckDimValue(radiusCylinder, "radius of cylinder")

    heightCylinder = float(input("What is the height of the cylinders in centimeters? "))
    heightCylinder = CheckDimValue(heightCylinder, "height of the cylinder")
    
    cheeseVolume = volumeCheese(height,width,length, numsphere, radiusSphere, numCylinder, radiusCylinder, heightCylinder)
    print("The total volume of cheese present is {:.1f} cubic centimeters. ".format(cheeseVolume))

# 1. Receive the parameters nsphere and rsphere, where nsphere is the number of spheres and rsphere is the radius of the sphere
# 2. Use the equation sphereVolume = nsphere * 4/3 * pi * rsphere**3
# 3. Return sphereVolume

def volumeSphere(nsphere, rsphere):
    sphereVolume = nsphere * 4/3 * pi * rsphere**3
    return sphereVolume

# 1. Receive the parameters nCylinder and rCylinder, and hCylinder,
#    where nCylinder is the number of cylinders, rCylinder is the radius of a cylinder, and hCylinder is the height of a cylinder.
# 2. Use the equation cylinderVolume = nCylinder * pi * hCylinder * rCylinder**2.
# 3. Return cylinderVolume.

def volumeCylinder(nCylinder, rCylinder, hCylinder):
    cylinderVolume = nCylinder * pi * rCylinder ** 2 * hCylinder
    return cylinderVolume

# 1. Receive the parameters h , w, l, where h is the height of the rectangle, w is the width of the rectangle, and l is the length of the rectangle. 
# 2. Use the equation rectangleVolume = h * w * l
# 3. Return the value back to rectangleVolume.

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

# 1. Receive the value.
# 2. If the value is less than or equal to 0, display error message and ask user to reenter a valid input.
# 3. Return value. 
def CheckDimValue(value, what):
    while value <= 0:
        print("The", what, "must be greater than zero!")
        value = float(input("Please re-enter the " + what + " of hunk of cheese. "))
    return value

# 1. Receive the nbubbles value.
# 2. If the value is less than or equal to 0, display error message and ask user to reenter a valid input.
# 3. Return nbubbles. 
def BubbleCheck(nbubbles, thing):
    while nbubbles <= 0:
        print("The", thing, "must be greater than zero!")
        nbubbles = float(input("Please re-enter the number of " + thing + ". "))
    return nbubbles
main()

