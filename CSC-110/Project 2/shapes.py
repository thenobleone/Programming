# shapes.py
# Created by Jo Narvaez-Jense
# Project 2A
# create a window that disples 5 shapes (rectangle, oval, triangle, circle, square) with 50px of space in between each spaace (2 rows, 2 on top, 3 on the bottom) with a boundary width of 5px

from graphics import *

def drawRectangle (rShape):
    rp1 = Point (50, 350)
    rp2 = Point (275, 225)

    rShape = Rectangle (rp1, rp2)
    rShape.setFill ("red")
    drawDisplay(rShape)

def drawOval (oShape):
    op1= Point (325, 350)
    op2 = Point (550, 225)

    oShape = Rectangle (op1, op2)
    oShape.setFill ("blue")
    rdrawDisplay(oShape)

def drawTriangle (tShape):
    tp1 = Point (100, 175)
    tp2 = Point (50, 50)
    tp3 = Point (175, 50)

    tShape = Triangle (tp1, tp2, tp3)
    tShape.setFill ("green")
    drawDisplay(tShape)

def drawCircle (cShape):
    cp1 = Point (300, 100)

    cShape = Cirlce (cp1, 75)
    cShape.setFill ("yellow")
    drawDisplay(cShape)

def drawSquare (sShape):
    sp1 = Point (425, 175)
    sp2 = Point (550, 50)

    sShape = Rectangle (sp1, sp1)
    sShape.setFill ("purple")
    drawDisplay(sShape)


def drawDisplay ():
    .draw (window)

def main ():
    window = GraphWin ("Shapes", 600, 400)
    window.setCoords(0,0, 1000,1000)
    drawDisplay ()


main ()
