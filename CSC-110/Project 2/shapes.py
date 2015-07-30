# shapes.py
# Created by Jo Narvaez-Jensen
# Project 2A
# create a window that disples 5 shapes (rectangle, oval, triangle, circle, square) with 50px of space in between each spaace (2 rows, 2 on top, 3 on the bottom) with a boundary width of 5px.

from graphics import *
import random

# Method with the common elements of each shape
def drawShape (shape, window):
    shape.setFill (color_rgb (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255)))
    shape.setOutline (color_rgb (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255)))
    shape.setWidth (5)
    shape.draw (window)

# Method sets the location of the recetangle within the graphic window
def drawRectangle (window):
    rp1 = Point (50, 350)
    rp2 = Point (250, 250)
    rShape = Rectangle (rp1, rp2)
    drawShape (rShape, window)

# Method sets the location of the oval within the graphic window
def drawOval (window):
    op1= Point (350, 350)
    op2 = Point (550, 250)
    oShape = Oval (op1, op2)
    drawShape (oShape, window)

# Method sets the location of the triangle within the graphic window
def drawTriangle (window):
    tp1 = Point (100, 150)
    tp2 = Point (50, 50)
    tp3 = Point (150, 50)
    tShape = Polygon (tp1, tp2, tp3)
    drawShape (tShape, window)

# Method sets the location of the cirlce within the graphic window
def drawCircle (window):
    cp1 = Point (300, 100)
    cShape = Circle (cp1, 50)
    drawShape (cShape, window)

# Method sets the location of the square within the graphic window
def drawSquare (window):
    sp1 = Point (450, 150)
    sp2 = Point (550, 50)
    sShape = Rectangle (sp1, sp2)
    drawShape (sShape, window)

# Creates a graphic window and call methods for each individual shape
def main ():
    i = 5
    window = GraphWin ("Shapes", 600, 400)
    window.setCoords(0, 0, 600, 400)
    window.setBackground ("LightBlue4")

    # Sets a message centered in window giving instructions to the user
#    message = Text( Point(300, 200),"Click to See Shapes and Colors!")
#    message.setStyle("bold")
#    message.setSize (18)
#    message.setTextColor ("white")
#    message.draw (window)

    # Loop lets the user check out different randomized color combinations
    for i in range (5):
        window.getMouse ()

        drawRectangle (window)
        drawOval (window)
        drawTriangle (window)
        drawCircle (window)
        drawSquare (window)

        # Lets the user know how many more times the loop will run
        #message.setText ("Click {0:0} more times to see more.".format(4 - i))

    # Informs the user how to close the window
    message.setText ("Click to close!")
    window.getMouse ()
    window.close ()

main ()
