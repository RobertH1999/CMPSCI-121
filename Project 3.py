"""
Purpose: Estimate the volume of the rectangular chunk of Swiss cheese. Assume the holes
are spherical or cylinders. 
Input needed: The dimensions of the cheese, the radius of the holes,
              radius and height of cylinder.  
              the number of number of holes.  
Expected output: Volume of the cheese.
Algorithm:
Volume of cheese: length * width * height.
Volume of spheres: 4/3 * pi * r^2.
Volume of cylinder: pi * r^2*h.

In main function:
    1. Ask input to input the height, length, number of spheres, number of cylinders, radius of cylinder, and height of cylinder.
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
"""
# pi is a global constant. 
pi = 3.14159

# In main function, prompt user to input, height, length, width, numspheres, radiusSphere, numCylinder, heightCylinder.
# Calculate the cheese volume. 
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

    heightCylinder = float(input("What is the height of the cylinders in centimeters? "))
    heightCylinder = CheckValue(heightCylinder, "height of the cylinder")
    
    cheeseVolume = volumeCheese(height,width,length, numsphere, radiusSphere, numCylinder, radiusCylinder, heightCylinder)
    print("The total volume of the cheese present is {:,.1f}".format(cheeseVolume), "cubic centimeters. ")

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
        print("The ", what, " must be greater than zero!")
        value = float(input("Enter a value greater than or equal to zero. " + what))
    return value

# Check if the inputted value is greater than zero. If not, then display error message and tell user to enter a valid value. 
def BubbleCheck(nbubbles, thing):
    while nbubbles < 0:
        print("The ", thing, " must be greater than zero!")
        nbubbles = float(input("Enter a value greater than or equal to zero. " + thing))
    return nbubbles
main()
