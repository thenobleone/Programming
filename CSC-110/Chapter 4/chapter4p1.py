# chapter4p1.py
# Created by Jo Narvaez-Jensen

from graphics import *

def main ():
    win = GraphWin ()
    shape = Rectangle (Point (30,30), Point (40,40))
    shape.setOutline ("blue")
    shape.setFill ("blue")
    shape.draw (win)

    for i in range (10):
        p = win.getMouse ()
        c = shape.getCenter()
        newSquare = shape.clone ()
        dx = p.getX () - c.getX ()
        dy = p.getY () - c.getY ()
        newSquare.draw (win)
        newSquare.move (dx, dy)

    exit = Text (Point (100, 20), "Click to exit!")
    exit.draw (win)
    win.getMouse ()
    win.close ()

main ()
