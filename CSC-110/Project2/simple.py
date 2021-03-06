# shapes.py
# Created by Jo Narvaez-Jense
# Project 2A
# create a window that disples 5 shapes (rectangle, oval, triangle, circle, square) with 50px of space in between each spaace (2 rows, 2 on top, 3 on the bottom) with a boundary width of 5px

from graphics import *

def main ():
    window = GraphWin ("Shapes", 600, 400)
    window.setCoords(0,0, 600, 400)
    #window.setBackground ("black")

    rp1 = Point (50, 350)
    rp2 = Point (250, 250)
    rShape = Rectangle (rp1, rp2)
    rShape.setFill ("red")
    rShape.setOutline ("orange")
    rShape.setWidth (5)
    rShape.draw (window)


    op1= Point (350, 350)
    op2 = Point (550, 250)
    oShape = Oval (op1, op2)
    oShape.setFill ("blue")
    oShape.setOutline ("purple")
    oShape.setWidth (5)
    oShape.draw (window)


    tp1 = Point (100, 150)
    tp2 = Point (50, 50)
    tp3 = Point (150, 50)
    tShape = Polygon (tp1, tp2, tp3)
    tShape.setFill ("green")
    tShape.setOutline ("blue")
    tShape.setWidth (5)
    tShape.draw (window)


    cp1 = Point (300, 100)
    cShape = Circle (cp1, 50)
    cShape.setFill ("yellow")
    cShape.setOutline ("green")
    cShape.setWidth (5)
    cShape.draw (window)


    sp1 = Point (450, 150)
    sp2 = Point (550, 50)
    sShape = Rectangle (sp1, sp2)
    sShape.setFill ("black")
    sShape.setOutline ("purple")
    sShape.setWidth (5)
    sShape.draw (window)

    guide = Line (tp1, sp1)
    guide.draw (window)
    guide2 = Line (tp3, sp2)
    guide2.draw (window)

main ()
