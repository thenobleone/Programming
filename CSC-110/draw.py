# drawShape.py
# Created by Jo Narvaez-Jensen
# program designed to create a window (500x500) that is displaying a rectanle that is 400 x 200 (blue outline, orange filling) with a green oval inside using the same coordinates as the rectanle

from graphics import *

display = GraphWin ("Drawing Window", 500,500)

def main ():
    p1 = Point (50, 150)
    p2 = Point (450, 300)

    rShape = Rectangle (p1,p2)
    rShape.setOutline ("blue")
    rShape.setFill ("orange")
    rShape.setWidth ("5")

    oShape = Oval (p1, p2)
    oShape.setOutline ("green")
    oShape.setFill ("green")
    

    rShape.draw (display)
    oShape.draw (display)

main ()
