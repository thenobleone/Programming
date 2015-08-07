# convertMiles_gui.py
# Created by Jo Narvaez-Jensen
# Project 2B

# This program converts distance in miles (inputed by user) into kilometeres
#   using a graphic window

from graphics import *

def main ():
    window = GraphWin ("Converter", 310, 150)
    window.setCoords (0, 0, 100, 100)
    window.setBackground ("Gray")

    title = Text (Point (50, 90), "Welcome!")
    title2 = Text (Point (50, 77), "Miles Converter!")
    mDisplay = Text (Point (19, 55), "        Miles:")
    kmDisplay = Text (Point (18, 28), "Kilometeres:")

    title.setSize (19)
    title.setStyle ('bold')
    title.setFill ("blue")
    title.draw (window)

    title2.setSize (19)
    title2.setStyle ('bold')
    title2.setFill ("blue")
    title2.draw (window)

    mDisplay.setSize (17)
    mDisplay.setStyle ('bold')
    mDisplay.setFill ("blue")
    mDisplay.draw (window)

    kmDisplay.setSize (17)
    kmDisplay.setStyle ('bold')
    kmDisplay.setFill ("blue")
    kmDisplay.draw (window)

    input = Entry (Point (45, 55), 5)
    input.setText ("  ")
    input.setSize (12)
    input.draw (window)
    input.setFill ("LightBlue")

    outputBox = Rectangle (Point (38.5, 35), Point (52, 20))
    outputBox.setFill ("LightGreen")
    outputBox.setWidth (1)
    outputBox.setOutline ("white")
    outputBox.draw (window)

    output = Text (Point (45, 26)," ")
    output.draw (window)

    buttonShape = Rectangle (Point (70, 50), Point (90, 30))
    buttonShape.setFill ("black")
    buttonShape.draw (window)

    buttonName = Text (Point (80, 40), "Convert")
    buttonName.setSize (16)
    buttonName.setStyle ("bold")
    buttonName.setFill ("white")
    buttonName.draw (window)

    window.getMouse ()

    miles = eval (input.getText())
    kM = round (1.60934 * miles, 2)

    output.setText (kM)
    buttonName.setText ("Quit")

    window.getMouse ()
    window.close ()

main ()
