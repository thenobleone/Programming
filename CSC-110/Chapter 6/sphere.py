# sphere.py
# Created by Jo Narvaez-Jensen

# Get's a sphere's radius from the user and output it's surface area and volume

from math import *

def getRadius ():
    try:
        r = eval (input ("Radius of sphere: "))
        if r > 0:
            return r
        else:
            print ("Not a valid input.")
            getRadius ()
    except:
        print ("Not a valid input.")
        getRadius ()


def volume (radius): #4/3pir^3
    v = round ((4/3 * pi * radius ** 3), 2)
    return v

def surfaceArea (radius): #4pir^2
    sa = round ((4 * pi * radius ** 2), 2)
    return sa

def results (v, a):
    print ("The surface area is " + str (a))
    print ("The volume is " + str (v))

def main ():
    r = getRadius ()
    v = volume (r)
    sa = surfaceArea (r)

    results (v, sa)

main ()
