# triangleArea.py
# Created by Lauren, Kit, An, and Jo

# This program is to calcuate the area of a triangle based on the length
#   of it's three sides, using heron's formula

from math import *

def main ():
    a, b, c = eval (input ("To find the area of your Triangle please enter the length of the 3 sides seperated by a comma: "))

    #s is equal the perimeter divided by 2
    s = 1/2 * (a + b + c)

    # we apply the value of s to Heron's formula to calcuate area
    area = sqrt ( s * (s - a) * (s - b) * (s - c))
    area = round (area, 2)

    #outputs the calcuated value of area 
    print ("The area of a triangle with the sides", a, b, sep = ", ", end = " ")
    print ("and", c , "is:", area, end = ".\n")

main ()
