# convert_gui.py

from graphics import *

def main ():
    win = GraphWin ("Temperature Converter", 400, 300)
    win.setCoords (0,0,3,4)
    win.setBackground ("DarkGray")


    Text (Point (1, 3), "     Celsius Temperature:").draw (win)
    Text (Point (1, 1), "  Fahrenheit Temperature:").draw (win)

    input = Entry (Point(2, 3), 5)
    input.setText ("  ")
    input.draw (win)

    output = Text (Point (2, 1), " ")
    output.draw (win)

    button = Text (Point (1.5, 2.0), "Convert It")
    button.draw (win)
    Rectangle (Point (1, 1.5), Point (2, 2.5)). draw (win)

    win.getMouse ()

    celsius = eval (input.getText())
    fahrenheit = 9/5 * celsius + 32

    output.setText (fahrenheit)
    button.setText ("Quit")

    win.getMouse ()
    win.close ()

main ()
