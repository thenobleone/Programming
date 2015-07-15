# graphLine.py
# Create by Jo Narvaez-Jensen

from graphics import *

def main ():
    # Creates GUI window for the user
    gWin = GraphWin ("Graphing Window", 500, 500)
    #gWin.setBackground ("black")
    gWin.setCoords(0,0, 100,100)

    # Sets up the initial and exiting messages
    mPoint = Point (50, 90)
    message = Text (mPoint, "Click Two Points!")
    message.setFill ("blue")
    message.setSize (14)
    message.setStyle ("bold")
    message.draw (gWin)

    # Gets the two X, Y values from the user's mouse clicks and draws them as cirlces for bette viewing by the user
    p1 = gWin.getMouse ()
    pMarker = Circle (p1, .75)
    pMarker.setFill("red")
    pMarker.draw (gWin)
    p2 = gWin.getMouse ()
    pMarker = Circle (p2, .75)
    pMarker.setFill("red")
    pMarker.draw (gWin)

    # Draws a line between the user's mouse clicks
    connect = Line (p1, p2)
    connect.setFill ("green")
    connect.draw (gWin)

    #Pulls out the needed values and initalizes variables in order to calcuate the slope
    x1, y1 = p1.getX (),p1.getY ()
    x2, y2 = p2.getX (), p2.getY ()

    # Cacluates the slop and rounds it to a single digit and then makes it a string literal to work with the Text function imported by graphics
    slope = str (round((y2-y1)/(x2-x1),1))

    # Outputs the resulting slope between two points
    sPoint = Point (30, 7)
    answer = Text (sPoint, "The slope of the line is: " + slope)
    answer.setFill ("purple")
    answer.setSize (14)
    answer.draw (gWin)

    # Ends the program
    message.setText ("Click anywhere to exit")
    gWin.getMouse ()
    gWin.close ()

main ()
